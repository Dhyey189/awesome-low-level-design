from datetime import datetime


class TimeStampableEntity:
    __created_at = datetime.now()
    __modified_at = datetime.now() 

    def get_created_at(self):
        return self.__created_at
    
    def get_modified_at(self):
        return self.__modified_at