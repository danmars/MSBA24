from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("mostRated")
sc = SparkContext(conf = conf)

def loadMovieNames():
    movieNames = {}
    with open("movies.csv") as f:
        for line in f:
            fields = line.split(',')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

nameDict = sc.broadcast(loadMovieNames())

lines = sc.textFile("ratings.csv")

movies = lines.map(lambda x: (int(x.split(',')[1]), 1))

movieCounts = movies.reduceByKey(lambda x, y: x + y)

flipped = movieCounts.map( lambda x : (x[1], x[0]))
sortedMovies = flipped.sortByKey(ascending= False)

sortedMoviesWithNames = sortedMovies.map(lambda countMovie : (nameDict.value[countMovie[1]], countMovie[0]))

results = sortedMoviesWithNames.take(10)
for result in results:
  print(result)

# spark-submit mostRatedMovie.py
# spark-submit mostRatedMovie.py 2>/dev/null

