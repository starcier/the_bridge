from .scene import Scene

class PlayerWinBKDiesScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print('\n')
        self.c.print("Aaargh!")
        self.c.print("-1117hp. Bridgekeeper has died", 1)
        self.c.print("Wizzard dies in vain!!")
        self.c.p_continue()

    def run(self):
        self.intro()

        self.c.print('You pass the bridge.')
        return 'end_scene'
