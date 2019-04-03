from .scene import Scene

class PlayerWinBKLivesScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print('\n')
        self.c.print("Correct! You can live!")
        self.c.print("Wizzard let's you pass.")
        self.c.p_continue()

    def run(self):
        self.intro()

        self.c.print('You pass the bridge.')
        return 'end_scene'
