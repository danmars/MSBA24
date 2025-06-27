from mrjob.job import MRJob

class NYSE(MRJob):

    def mapper(self, _, line):
        (ticker, day, tradePrice) = line.split(',')    
        yield ticker, int(tradePrice)

    def reducer(self, ticker, Prices):        
        yield ticker, max(Prices)

if __name__ == '__main__':
    NYSE.run() 

#!python NYSE.py NYSE_DATA.txt
#python NYSE.py NYSE_DATA.txt

