import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_FINAL, BULLET_BOSS_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class EvilCat(Enemy):
    WIDTH = 80
    HEIGHT = 120
    SPEED_X = 10
    SPEED_Y = 5
    SHOOTING_TIME = 5
    LIVES = 30
    BULLET_TYPE =  BULLET_BOSS_TYPE
    UP = "up"
    LEFT = "left"
    RIGHT = "right"
    DOWN = "down"
    
    def __init__(self):
        self.image = ENEMY_FINAL
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.mov_y = self.DOWN
        self.can_move_y = True
        self.can_move_x = True
        self.when_static_y = random.randint(5000, 10000)
        self.when_static_x = random.randint(5000, 10000)
        super().__init__(self.image)
    
    def move(self):
        if self.can_move:
            
            
            if pygame.time.get_ticks() > self.when_static_y:
                self.can_move_y = True
                if pygame.time.get_ticks() > self.when_static_x:
                    self.when_static_x += random.randint(5000, 10000)
                    self.when_static_y += random.randint(2000, 3000)
                    self.can_move_x = False
                    self.can_move_y = False
                else:
                    self.can_move_x = True
            
            if self.can_move_x:
                if self.mov_x == self.LEFT:
                    self.rect.x -= self.speed_x
                    if self.index > self.interval or self.rect.x <= 0:
                        self.mov_x = self.RIGHT
                        self.index = 0
                        self.interval = random.choice(self.INTERVAL_LIST)
                else:
                    self.rect.x += self.speed_x
                    if self.index > self.interval or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                        self.mov_x = self.LEFT
                        self.index = 0
                        self.interval = random.choice(self.INTERVAL_LIST)
                
            if self.can_move_y:
                if self.mov_y == self.UP:
                    self.rect.y -= self.speed_x
                    if self.index > self.interval or self.rect.y <= 0:
                        self.mov_y = self.DOWN
                        self.index = 0
                        self.interval = random.choice(self.INTERVAL_LIST)
                else:
                    self.rect.y += self.speed_x
                    if self.index > self.interval or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
                        self.mov_y = self.UP
                        self.index = 0
                        self.interval = random.choice(self.INTERVAL_LIST)
            self.index += 1