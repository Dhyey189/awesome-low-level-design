from postable_entity import PostableEntity
from tagable_entity import TagableEntity
from time_stamped_entity import TimeStampableEntity
from votable_entity import VotableEntity


class Answer(PostableEntity, TagableEntity, TimeStampableEntity, VotableEntity, Commentable):
    __comments = []

    def get_comments(self):
        return self.__comments
    
    def add_comment(self, comment):
        self.__comments.append(comment)
