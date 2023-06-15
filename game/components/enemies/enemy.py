import pygame
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE, EXPLOSION_SHEET_1

class Enemy:
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL_LIST = [50, 100, 150, 200]
    SHOOTING_TIME = 30
    
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.interval = random.choice(self.INTERVAL_LIST)
        self.index = 0
        self.is_alive = True
        self.shooting_time = 0
        self.explosion_sprite = 0
        self.can_explode = False

    def check_is_alive(self):
        if self.is_alive and self.can_explode:
            self.explode()
    
    def explode(self):
        self.explosion_sprite += 0.2
        frame = self.get_from_image(EXPLOSION_SHEET_1, int(self.explosion_sprite), 100, 100, 1, (0,0,0))
        self.image = frame
        if self.explosion_sprite >= 5:
            self.explosion_sprite = 0
            self.is_alive = False
            
    def get_from_image(self, sheet, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), (frame * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        
        return image
    
    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT + self.rect.height:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)
        self.check_is_alive()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.SPEED_Y
            
        if self.mov_x == self.LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.interval or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
                self.interval = random.choice(self.INTERVAL_LIST)
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.interval or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0
                self.interval = random.choice(self.INTERVAL_LIST)
        self.index += 1
    
    def kill(self):
        self.can_explode = True
        
    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)