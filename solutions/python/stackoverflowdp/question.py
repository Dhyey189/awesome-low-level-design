from postable_entity import PostableEntity
from datetime import datetime
from tagable_entity import TagableEntity
from time_stamped_entity import TimeStampableEntity
from votable_entity import VotableEntity

class Question(PostableEntity, TagableEntity, TimeStampableEntity, VotableEntity):
    def __init__(self, title, content, author):
        self.__title = title
        self.__answers = []

        super(PostableEntity).__init__(content, author)

    def get_title(self):
        return self.__title
    
    def get_answers(self):
        return self.__answers
    
    def add_answer(self, answer):
        self.__answers.append(answer)

