from .scene import Scene

class ThirdQuestionScene(Scene):

    def __init__(self, console):
        self.c = console

    def intro(self):
        self.c.print("""
 Amused by your answer the old wizzard prepares
 to ask you his final question.""")
        self.c.p_continue()

    def run(self):
        self.intro()
        self.c.print("?\n")
        self.c.print(f"1. Blue!")
        self.c.print("2. Wait, what is...")
        self.c.print("3. I don't know!")
        self.c.print("4. See ya!")

        action = self.c.input("Answer (nr)")
        self.c.cls_game()

        if action == str(1):
            self.c.print("- Blue!")
            return 'player_win_bk_lives'

        elif action == str(2):
            self.c.print("- Wait, what is...!")
            return 'player_win_bk_dies'

        elif action == str(3):
            self.c.print("- I...I don't know!")
            return 'player_death'

        elif action == str(4):
            self.c.print("- See ya!")
            return 'bridge'

        else:
            self.c.print("Does not compute!")
            return 'third_question'
