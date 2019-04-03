"""TO DO

"""

from console import Console
from engine import Engine
from scene_controller import SceneController
from characters.player import Player

# Initiate classes

c = Console()
p = Player()
sc = SceneController(c, p)
e = Engine()

e.run(p, sc, c)

while True:
    val = c.input("Write to console")
    c.print(val)
