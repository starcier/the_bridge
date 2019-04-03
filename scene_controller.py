from scenes.bridge_scene import BridgeScene
from scenes.first_question_scene import FirstQuestionScene
from scenes.second_question_scene import SecondQuestionScene
from scenes.third_question_scene import ThirdQuestionScene
from scenes.player_death_scene import PlayerDeathScene
from scenes.player_win_bk_dies_scene import PlayerWinBKDiesScene
from scenes.player_win_bk_lives_scene import PlayerWinBKLivesScene
from scenes.end_scene import EndScene


class SceneController(object):

    scenes = {}
    end_scenes = []
    start_scene = None
    next_scene_name = None

    def __init__(self, console, player):
        self.c = console
        self.p = player

        self.add_scene('bridge', BridgeScene(self.c), end_scene=0)
        self.add_scene('first_question', FirstQuestionScene(self.c, self.p), end_scene=0)
        self.add_scene('second_question', SecondQuestionScene(self.c), end_scene=0)
        self.add_scene('third_question', ThirdQuestionScene(self.c), end_scene=0)
        self.add_scene('player_death', PlayerDeathScene(self.c), end_scene=1)
        self.add_scene('player_win_bk_dies', PlayerWinBKDiesScene(self.c), end_scene=1)
        self.add_scene('player_win_bk_lives', PlayerWinBKLivesScene(self.c), end_scene=1)
        self.add_scene('end_scene', EndScene(self.c))

        self.start_scene('bridge')


    def add_scene(self, name, key, end_scene=0):

        if end_scene:
            self.end_scenes.append(key)

        self.scenes[name] = key

    def start_scene(self, name):
        self.start_scene_name = name

    def load_scene(self, name):
        self.next_scene_name = self.scenes[name].run()
