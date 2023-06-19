import random

from game.components.levels.level_1 import Level1
from game.components.levels.level_2 import Level2
from game.components.levels.level_3 import Level3
from game.components.levels.level_4 import Level4
from game.components.levels.level_5 import Level5
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.powers.power_handler import PowerHandler

class LevelHandler:
    DEFAULT_LEVEL = Level1
    
    def __init__(self, player):
        self.player = player
        self.level = self.DEFAULT_LEVEL()
        self.current_score = 0
        self.enemy_handler = EnemyHandler(self.level.EMENY_LIMIT, self.level.ENEMY_SPAWN_DELAY, self.level.DEFAULT_ENEMIES)
        self.bullet_handler = BulletHandler()
        self.power_handler = PowerHandler(self.level.POWER_LIMIT, self.level.POWER_SPAWN_DELAY, self.level.DEFAULT_POWERS)
    
    def set_current_time(self, time):
        self.current_score = time
        
    def set_level_config(self, level):
        self.enemy_handler.set_new_level(level.EMENY_LIMIT, level.ENEMY_SPAWN_DELAY, level.DEFAULT_ENEMIES)
        self.power_handler.set_new_level(level.POWER_LIMIT, level.POWER_SPAWN_DELAY, level.DEFAULT_POWERS)
    
    def update(self, current_score):
        self.set_current_time(current_score)
        if current_score >= 10:
            self.level = Level2()
            self.set_level_config(self.level)
        elif current_score >= 20:
            self.level = Level3()
            self.set_level_config(self.level)
        elif current_score >= 30:
            self.level = Level4()
            self.set_level_config(self.level)
        
        elif current_score >= 40:
            self.level = Level5()
            self.set_level_config(self.level)
            
            
        self.enemy_handler.update(self.player, self.bullet_handler, self.level.game_speed)
        self.bullet_handler.update(self.player, self.enemy_handler.enemies)
        self.power_handler.update(self.player)

    def draw(self, screen):
        self.enemy_handler.draw(screen)
        self.bullet_handler.draw(screen)
        self.power_handler.draw(screen)
    
    
    def draw_background(self, screen):
        self.level.draw_background(screen)
    
    def reset(self):
        self.level = self.DEFAULT_LEVEL()
        self.set_level_config(self.level)
        self.current_score = 0
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handler.reset()