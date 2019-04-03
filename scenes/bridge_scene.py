from .scene import Scene

class BridgeScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print("""
 As you march North, you stumble upon a pass with a bridge
 that looks like the only way you can get to the other side.
 In front of it, there is an old man, looking at you.
 You approach him.
 """)
        self.c.p_continue()

    def run(self):
        self.intro()
        return 'first_question'
