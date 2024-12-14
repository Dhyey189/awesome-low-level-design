
class PostableEntity:
    def __init__(self, content, author):
        self.__content = content
        self.__author = author
        
    def get_content(self):
        return self.__content
    
    def get_author(self):
        return self.__author
    
    
