from mrjob.job import MRJob
from mrjob.step import MRStep

class mostRatedMovieBetter(MRJob):
    
    def configure_args(self):
        super(mostRatedMovieBetter, self).configure_args()
        self.add_file_arg('--items', help='Path to movies.csv')
    
    def steps(self):
        return [
            MRStep(mapper=self.mapperGetRatings,
                   reducer_init=self.reducer_init,
                   reducer=self.reducerCountRatings),
            MRStep(mapper=self.mapperCreateNewPairs,
                   reducer = self.reducerFindMax)
        ]

    def mapperGetRatings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split(',')
        yield movieID, 1

    def reducer_init(self):
        self.movieNames = {}
        
        with open("movies.csv", encoding='ascii', errors='ignore') as f:
            for line in f:
                fields = line.split(',')
                self.movieNames[fields[0]] = fields[1]

    def reducerCountRatings(self, key, values):
        yield self.movieNames[key], sum(values)
        
    def mapperCreateNewPairs(self, key, value):
        yield None, (value, key)
    
    def reducerFindMax(self, key, values):
        yield max(values)

if __name__ == '__main__':
    mostRatedMovieBetter.run()

# !python MostRatedMovieBetter.py --items=movies.csv ratings_small.csv    
# !python MostRatedMovieBetter.py --items=movies.csv ratings.csv