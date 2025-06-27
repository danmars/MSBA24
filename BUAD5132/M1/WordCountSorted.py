from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCountSorted(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapperGetWords,
                   reducer=self.reducerCountWords),
            MRStep(mapper=self.mapperMakeCountsKey,
                   reducer = self.reducerOutputWordsAndCounts)
        ]    

    def mapperGetWords(self, _, line):
        words = line.split()
        for word in words:
            yield word.lower(), 1

    def reducerCountWords(self, word, values):
        yield word, sum(values)

    def mapperMakeCountsKey(self, word, count):
        yield count, word

    def reducerOutputWordsAndCounts(self, count, words):       
        for word in words:
            yield count, word


if __name__ == '__main__':
    WordCountSorted.run()

# !python WordCountSorted.py feedback.txt 