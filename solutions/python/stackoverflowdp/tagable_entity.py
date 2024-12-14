class TagableEntity:
    __tags = []

    def get_tags(self):
        return self.__tags
    
    def add_tag(self, new_tag):
        self.__tags.append(new_tag)
