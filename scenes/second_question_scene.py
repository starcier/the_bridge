from .scene import Scene

class SecondQuestionScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print("""
 With a sign of politeness, he grants you life as he prepares
 to ask you his second question.""")
        self.c.p_continue()

    def run(self):
        self.intro()
        self.c.print("What is your mission?\n")
        self.c.print(f"1. My mission is to find the Holy Grail!")
        self.c.print("2. Enough of this! Prepare to die!")
        self.c.print("3. Err...Maybe next time.")

        action = self.c.input("Answer (nr)")
        self.c.cls_game()

        if action == str(1):
            self.c.print("- My mission is to find the Holy Grail!")
            return 'third_question'

        elif action == str(2):
            self.c.print("- Enough of this! Prepare to die!")
            return 'player_death'

        elif action == str(3):
            self.c.print("- Err...Maybe next time.")
            return 'bridge'

        else:
            self.c.print("Does not compute!")
            return 'second_question'
