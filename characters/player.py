from .character import Character

class Player(Character):

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name.capitalize()
