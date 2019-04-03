from .scene import Scene

class PlayerDeathScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print('Player dead', 1)
        self.c.print('\n')
        self.c.print('You have failed...and died!')

    def run(self):
        self.intro()
        self.c.print('There is nothing else for you to do here...')
        return 'end_scene'
