class VotableEntity:
    __vote = 0

    def get_vote(self):
        return self.__vote
    
    def up_vote(self):
        self.__vote += 1

    def down_vote(self):
        self.__vote -= 1
