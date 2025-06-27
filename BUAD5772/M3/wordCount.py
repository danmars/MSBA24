from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("wordCount")
sc = SparkContext(conf = conf)

lines = sc.textFile("feedback.txt")

words = lines.flatMap(lambda x: x.split())

wordOne = words.map(lambda x: (x, 1))

wordCount = wordOne.reduceByKey(lambda x, y: x+y)

wordCountSorted = wordCount.sortBy(lambda x: x[1], False)

for row in wordCountSorted.collect(): 
  print(row)

# spark-submit wordCount.py
# spark-submit wordCount.py 2>/dev/null