import random
from game.components.levels.level import Level
from game.components.enemies.gladiator import Gladiator
from game.components.powers.shield import Shield
from game.components.powers.destructor import Destructor
from game.components.powers.heart import Heart

from game.utils.constants import BG_LEVEL_2

class Level2(Level):
    GAME_SPEED = 11
    EMENY_LIMIT = 10
    ENEMY_SPAWN_DELAY = random.randint(1000, 2000)
    DEFAULT_ENEMIES = [Gladiator]
    POWER_LIMIT = 3
    POWER_SPAWN_DELAY = random.randint(1000, 1500)
    DEFAULT_POWERS = [Shield, Heart]
    BACKGROUND = BG_LEVEL_2
    def __init__(self):
        super().__init__()