# Discussion Code
# Name the file "friendRec.py"
# Execution Statement
# !python friendRec.py connections.txt > output.txt
# Note, this took about 10 minutes to run on the course author's work CPU

from mrjob.job import MRJob
from mrjob.step import MRStep

class FriRec(MRJob):

    def steps(self):
        return  [
            MRStep(mapper = self.mapper1,
                   reducer = self.reducer1),
            MRStep(mapper = self.mapper2, 
                   reducer = self.reducer2)
            ]
    
    def mapper1(self, _, line):
        user_id, friends = line.split("\t")
        friend_ids = friends.split(",")
        
        for friend in friend_ids:
            yield (user_id + "," + friend, 0)
        for friend_i in friend_ids:
            for friend_j in friend_ids:
                if friend_i == friend_j:
                    continue
                yield (friend_i + "," + friend_j, 1)
   
    def reducer1(self, friend_pair, values):
        if not (0 in values):
            yield (friend_pair, sum(values))
            
    def mapper2(self, friend_pair, value_sum):
        user_id, friend_id = friend_pair.split(",")
        yield (user_id, friend_id + "," + str(value_sum))
    
    def reducer2(self, user_id, values):
        all_friends = []
        for value in values:
            friend_id, value_sum = value.split(",")
            friend_id = int(friend_id)
            value_sum = int(value_sum)
            all_friends.append((value_sum, friend_id))
            
        most_common_friends = sorted(all_friends, reverse = True)
        if len(most_common_friends) > 10:
            most_common_friends = most_common_friends[:10]
    
        friend_id_strs = []
        for fri in most_common_friends:
            friend_id_strs.append(str(fri[1]))
        yield (user_id, ",".join(friend_id_strs))

if __name__ == '__main__':
    FriRec.run()