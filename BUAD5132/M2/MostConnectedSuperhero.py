from mrjob.job import MRJob
from mrjob.step import MRStep

class MostConnectedSuperHero(MRJob):

    def configure_args(self):
        super(MostConnectedSuperHero, self).configure_args()
        self.add_file_arg('--names', help='Path to MarvelNames.txt')

    def steps(self):
        return [
            MRStep(mapper=self.mapperCountFriendsPerLine,
                   reducer=self.reducerCombineFriends),
            MRStep(mapper_init=self.loadNameDictionary,
                   mapper=self.mapperPrepForSort,                   
                   reducer = self.reducerFindMaxFriends)
        ]

    def mapperCountFriendsPerLine(self, _, line):
        fields = line.split()
        heroID = fields[0]
        numFriends = len(fields) - 1
        yield int(heroID), int(numFriends)

    def reducerCombineFriends(self, heroID, friendCounts):
        yield heroID, sum(friendCounts)

    def loadNameDictionary(self):
        self.heroNames = {}

        with open("Marvelnames.txt", encoding='ascii', errors='ignore') as f:
            for line in f:
                fields = line.split('"')
                heroID = int(fields[0])
                self.heroNames[heroID] = fields[1]
                
    def mapperPrepForSort(self, heroID, friendCounts):
        heroName = self.heroNames[heroID]
        yield None, (friendCounts, heroName)

    def reducerFindMaxFriends(self, key, value):
        yield max(value)


if __name__ == '__main__':
    MostConnectedSuperHero.run()


#!python MostConnectedSuperhero.py --names=MarvelNames.txt MarvelGraph.txt
#!python MostConnectedSuperhero.py --names=MarvelNames.txt MarvelSmall.txt