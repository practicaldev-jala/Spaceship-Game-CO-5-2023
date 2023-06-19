import pygame
import random
from game.components.enemies.ship import Ship
from game.components.powers.shield import Shield
from game.components.powers.destructor import Destructor
from game.components.powers.heart import Heart
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BG, BG_LEVEL_1



class Level:
    GAME_SPEED = 10
    EMENY_LIMIT = 7
    ENEMY_SPAWN_DELAY = random.randint(1000, 3000)
    DEFAULT_ENEMIES = [Ship]
    POWER_LIMIT = 1
    POWER_SPAWN_DELAY = random.randint(3000, 7000)
    DEFAULT_POWERS = [Shield, Destructor, Heart]
    BACKGROUND = BG_LEVEL_1
    
    def __init__(self):
        self.game_speed = self.GAME_SPEED
        self.background = self.BACKGROUND
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        
    def draw_background(self, screen):
        image = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        stars = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        image_height = image.get_height()
        screen.blit(image, (0, 0))
        screen.blit(stars, (self.x_pos_bg, self.y_pos_bg))
        screen.blit(stars, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            screen.blit(stars, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed