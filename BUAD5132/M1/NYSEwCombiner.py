from mrjob.job import MRJob

class NYSE_wCombiner(MRJob):

    def mapper(self, _, line):
        (ticker, day, tradePrice) = line.split(',')    
        yield ticker, int(tradePrice)
        
    def combiner(self, ticker, Prices):        
        yield ticker, max(Prices)

    def reducer(self, ticker, Prices):        
        yield ticker, max(Prices)

if __name__ == '__main__':
    NYSE_wCombiner.run()
    
#!python NYSEwCombiner.py NYSE_DATA.txt