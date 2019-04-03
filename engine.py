class Engine(object):

    def __init__(self):
        pass

    def intro(self):
        self.c.print("""
 Welcome to TheBridge!
 - Fallout 2 adoptation of a famous Bridgekeeper scene.""")

        self.c.print("Player name required", 1)
        self.c.print("\n What is your name?")
        self.p.name = self.c.input('Enter name')
        self.c.print(f"Player name: {self.p.get_name()}", 1)

        self.c.cls_game()

        self.c.print(f"\n Welcome {self.p.get_name()}!\n Let's get started shall we!")
        self.c.p_continue()


    def run(self, player, scene_controller, console):
        self.p = player
        self.sc = scene_controller
        self.c = console

        # Start game
        self.c.print("Engine initiated", 1)
        self.c.cls()
        self.intro()

        current_scene_name = self.sc.start_scene_name
        current_scene = self.sc.scenes[current_scene_name]

        while current_scene_name not in self.sc.end_scenes:
            self.c.print(f"Loading scene: {current_scene_name}", 1)
            self.sc.load_scene(current_scene_name)
            current_scene_name = self.sc.next_scene_name
