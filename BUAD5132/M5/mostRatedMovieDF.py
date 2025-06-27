from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.appName("MostRatedMovDF").getOrCreate()

def loadMovieNames():
    movieNames = {}
    with open("movies.csv", errors='ignore') as f:
        for line in f:
            fields = line.split(',')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

nameDict = loadMovieNames()

ratingsDF = spark.read.format("csv").option("header", "false")\
                                    .option("inferSchema", "true")\
                                    .load("ratings.csv")


ratingsDF = ratingsDF.toDF('userID', 'movieID', 'rating', 'timeStamp')

topMovieIDs = ratingsDF.groupBy("movieID").count().orderBy("count", ascending=False)

top10 = topMovieIDs.take(10)

# Print the results
print("\n")
for result in top10:
  print("%s: %d" % (nameDict[result[0]], result[1]))

# Stop the session
spark.stop()

# spark-submit mostRatedMovieDF.py
# spark-submit mostRatedMovieDF.py 2>/dev/null




