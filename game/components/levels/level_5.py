import random
from game.components.levels.level import Level
from game.components.enemies.evil_cat import EvilCat

from game.components.powers.shield import Shield
from game.components.powers.destructor import Destructor
from game.components.powers.heart import Heart

from game.utils.constants import BG_LEVEL_5

class Level5(Level):
    GAME_SPEED = 13
    EMENY_LIMIT = 1
    ENEMY_SPAWN_DELAY = random.randint(10000, 10000)
    DEFAULT_ENEMIES = [EvilCat]
    POWER_LIMIT = 30
    POWER_SPAWN_DELAY = random.randint(500, 800)
    DEFAULT_POWERS = [Shield, Destructor, Heart]
    BACKGROUND = BG_LEVEL_5
    def __init__(self):
        super().__init__()