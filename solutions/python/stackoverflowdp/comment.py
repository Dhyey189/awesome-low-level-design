from postable_entity import PostableEntity
from tagable_entity import TagableEntity
from time_stamped_entity import TimeStampableEntity
from votable_entity import VotableEntity

class Comment(PostableEntity, TimeStampableEntity):
    pass
