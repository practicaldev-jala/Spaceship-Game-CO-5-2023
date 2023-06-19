import pygame
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE, EXPLOSION_SHEET_1, WHITE_COLOR
from game.components.sprite_sheet import SpriteSheet
from game.components import text_utils

class Enemy:
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    Y_POS = 20
    SPEED_X = 3
    SPEED_Y = 1
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL_LIST = [50, 100, 150, 200]
    SHOOTING_TIME = 30
    LIVES = 1
    BULLET_TYPE = BULLET_ENEMY_TYPE
    
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.interval = random.choice(self.INTERVAL_LIST)
        self.index = 0
        self.lives = self.LIVES
        self.is_alive = True
        self.is_destroyed = False
        self.shooting_time = 0
        self.explosion_sprite_pos = 0
        self.explosion_sprite = SpriteSheet(EXPLOSION_SHEET_1)
        self.can_explode = False
        self.can_move = True
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

    def check_is_alive(self):
        if self.is_alive and self.can_explode:
            self.explode()
    
    def explode(self):
        self.can_move = False
        self.explosion_sprite_pos += 0.5
        frame = self.explosion_sprite.get_from_image((int(self.explosion_sprite_pos), int(self.explosion_sprite_pos)), 100, 100, 1, (0,0,0))
        self.image = frame
        if self.explosion_sprite_pos >= 5:
            self.is_alive = False
            self.is_destroyed = True
            self.explosion_sprite_pos = 0
            
    def update(self, bullet_handler, speed):
        if self.rect.y >= SCREEN_HEIGHT + self.rect.height:
            self.is_alive = False
        self.shooting_time += 1
        self.speed_x = self.SPEED_X + speed
        self.speed_y = self.SPEED_Y + (speed // 2)
        self.move()
        self.shoot(bullet_handler)
        self.check_is_alive()
        
    def draw(self, screen):
        self.draw_lives(screen)
        screen.blit(self.image, self.rect)
    
    def draw_lives(self, screen):
        if self.lives > 0:
            pos_x = self.rect.x + (self.rect.width // 2)
            lives, lives_rect = text_utils.get_message(f'{self.lives}', 20, WHITE_COLOR, pos_x, self.rect.y - 5, antialias=False)
            screen.blit(lives, lives_rect)
        
    def move(self):
        if self.can_move:
            self.rect.y += self.speed_y // 2
                
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
            self.index += 1
        
    def kill(self):
        if self.lives > 0:
                self.lives -= 1
        if self.lives <= 0:
            self.can_explode = True
            self.explosion_sprite_pos = 0
            
    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(self.BULLET_TYPE, self.rect.center)