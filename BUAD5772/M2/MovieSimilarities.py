from mrjob.job import MRJob
from mrjob.step import MRStep
from math import sqrt
from itertools import combinations

class MovieSimilarities(MRJob):

    def configure_args(self):
        super(MovieSimilarities, self).configure_args()
        self.add_file_arg('--items', help='Path to movies.csv')


    def steps(self):
        return [
            MRStep(mapper=self.mapperGetInput,
                    reducer=self.reducerRatingsByUser),
            MRStep(mapper=self.mapperCreateMovieRatingPairs,
                    reducer=self.reducerComputeSimilarity),
            MRStep(mapper_init=self.loadMovieNames,
                   mapper=self.mapperSortMovies,                    
                    reducer=self.reducerMovieRecommendations)]
  
    
    # Output key-value pair: (userID)-(movieID,rating)
    def mapperGetInput(self, key, line):
        (userID, movieID, rating, timestamp) = line.split(',')
        yield  userID, (movieID, float(rating))


    #Group (MovieID,rating) pairs by userID
    def reducerRatingsByUser(self, user_id, itemRatings):
        movie_rating = []
        for movieID, rating in itemRatings:
            movie_rating.append((movieID, rating))

        yield user_id, movie_rating


    # Find every pair of movies each user has seen, and
    # yield each pair with its associated ratings
    def mapperCreateMovieRatingPairs(self, user_id, itemRatings):
        for itemRating1, itemRating2 in combinations(itemRatings, 2):
            movieID1 = itemRating1[0]
            rating1 = itemRating1[1]
            movieID2 = itemRating2[0]
            rating2 = itemRating2[1]

            yield (movieID1, movieID2), (rating1, rating2)
            yield (movieID2, movieID1), (rating2, rating1)


    # Compute the cosine similarity metric between two rating vectors
    def cosineSimilarity(self, ratingPairs):
        numPairs = 0
        sum_xx = sum_yy = sum_xy = 0
        for ratingX, ratingY in ratingPairs:
            sum_xx += ratingX * ratingX
            sum_yy += ratingY * ratingY
            sum_xy += ratingX * ratingY
            numPairs += 1

        numerator = sum_xy
        denominator = sqrt(sum_xx) * sqrt(sum_yy)

        score = 0
        if (denominator):
            score = round((numerator / (float(denominator))), 4)

        return (score, numPairs)


    # Output key-value pair: (movie pair)-(similarity score, number of co-ratings)
    def reducerComputeSimilarity(self, moviePair, ratingPairs):
        score, numPairs = self.cosineSimilarity(ratingPairs)

        if (numPairs > 100 and score > 0.95):
            yield moviePair, (score, numPairs)


    # Load database of movie names.
    def loadMovieNames(self): 
        self.movieNames = {}

        with open("movies.csv", errors='ignore') as f:
            for line in f:
                fields = line.split(',')
                self.movieNames[int(fields[0])] = fields[1]


    # Rearrange the key-value pairs and replace MovieID with Movie Names 
    # kye-value pairs: (Movie, SimilarityScore)-(SimilarMovie, # of co-ratings)
    def mapperSortMovies(self, moviePair, scores):
        score, n = scores
        movie1, movie2 = moviePair

        yield (self.movieNames[int(movie1)], score), \
            (self.movieNames[int(movie2)], n)


    # Output the recommendations
    # (Movie)-(SimilarMovie, SimilarityScore, # of co-ratings)
    def reducerMovieRecommendations(self, movieScore, similarN):
        movie1, score = movieScore
        for movie2, n in similarN:
            yield movie1, (movie2, score, n)

if __name__ == '__main__':
    MovieSimilarities.run()

# !python MovieSimilarities.py --items=movies.csv ratings.csv > sims.txt