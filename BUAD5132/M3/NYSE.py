from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("NYSE")
sc = SparkContext(conf = conf)

lines = sc.textFile("NYSE_DATA.txt")

stockRDD = lines.map(lambda line: line.split(','))

stockPricePair = stockRDD.map(lambda x: (x[0], float(x[2])))

maxPrice = stockPricePair.reduceByKey(lambda x, y: max(x,y)) 

maxPriceSortedByStock = maxPrice.sortByKey()
results1 = maxPriceSortedByStock.collect()

print("Printing the maximum stock prices sorted based on the stock name")
for result in results1:
  print(result)

maxPriceFlipped = maxPrice.map(lambda x: (x[1], x[0]))
maxPriceSortedByPrice = maxPriceFlipped.sortByKey(ascending= False)
results2 = maxPriceSortedByPrice.collect()

print("Printing the maximum stock prices sorted based on the stock price")
for result in results2:
  print(result)

# spark-submit NYSE.py
# spark-submit NYSE.py 2>/dev/null