import random
from game.components.levels.level import Level
from game.components.enemies.ship import Ship
from game.components.enemies.striker import Striker
from game.components.enemies.gladiator import Gladiator
from game.components.powers.shield import Shield
from game.components.powers.destructor import Destructor
from game.components.powers.heart import Heart

from game.utils.constants import BG_LEVEL_4

class Level4(Level):
    GAME_SPEED = 13
    EMENY_LIMIT = 15
    ENEMY_SPAWN_DELAY = random.randint(500, 1000)
    DEFAULT_ENEMIES = [Ship, Gladiator, Striker]
    POWER_LIMIT = 10
    POWER_SPAWN_DELAY = random.randint(1000, 2000)
    DEFAULT_POWERS = [Shield, Destructor, Heart]
    BACKGROUND = BG_LEVEL_4
    def __init__(self):
        super().__init__()