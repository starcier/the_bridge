from .scene import Scene
from sys import exit

class EndScene(Scene):

    def __init__(self, console):
        self.c = console

    def run(self):
        self.c.print("Terminate game.", 1)
        exit(0)
