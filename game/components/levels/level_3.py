import random
from game.components.levels.level import Level
from game.components.enemies.striker import Striker
from game.components.powers.shield import Shield
from game.components.powers.destructor import Destructor
from game.components.powers.heart import Heart

from game.utils.constants import BG_LEVEL_3

class Level3(Level):
    GAME_SPEED = 12
    EMENY_LIMIT = 12
    ENEMY_SPAWN_DELAY = random.randint(1000, 1500)
    DEFAULT_ENEMIES = [Striker]
    POWER_LIMIT = 5
    POWER_SPAWN_DELAY = random.randint(1000, 1500)
    DEFAULT_POWERS = [Shield, Destructor, Heart]
    BACKGROUND = BG_LEVEL_3
    def __init__(self):
        super().__init__()