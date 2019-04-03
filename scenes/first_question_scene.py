from .scene import Scene

class FirstQuestionScene(Scene):

    def __init__(self, console, player):
        self.c = console
        self.p = player

    def intro(self):
        self.c.print("""
 The Bridgekeeper is looking at you with a unpleasent grimm.
 Stop! - He screams. Who would cross the Bridge of Death,
 must answer me these questions three. Ere the other side he see.
 """)
        self.c.p_continue()
        self.c.print("""- Ask me the questions, Bridgekeeper. I'm not afraid!""")

    def run(self):
        self.intro()

        self.c.print("\n What is your name?\n")
        self.c.print(f"1. My name is {self.p.get_name()}")
        self.c.print("2. Not your business old slug!")
        self.c.print("3. Bye! I'll come next time.")

        action = self.c.input("Answer (nr)")
        self.c.cls_game()

        if action == str(1):
            self.c.print(f"\n- My name is {self.p.get_name()} old man!")
            return 'second_question'

        elif action == str(2):
            self.c.print(f"\n- Not your business old slug! Prepare to die!")
            return 'player_death'

        elif action == str(3):
            return 'bridge'

        else:
            self.c.print("Does not compute!")
            return 'first_question'
