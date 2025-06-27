from mrjob.job import MRJob
from mrjob.step import MRStep

class mostRatedMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapperGetRatings,
                   reducer=self.reducerCountRatings),
            MRStep(mapper=self.mapperCreateNewPairs,
                   reducer = self.reducerFindMax)
        ]

    def mapperGetRatings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split(',')
        yield movieID, 1

    def reducerCountRatings(self, key, values):
        yield key, sum(values)
        
    def mapperCreateNewPairs(self, key, value):
        yield None, (value, key)
    
    def reducerFindMax(self, key, values):
        yield max(values)

if __name__ == '__main__':
    mostRatedMovie.run()  

# !python MostRatedMovie.py ratings.csv
# !python MostRatedMovie.py ratings_small.csv
