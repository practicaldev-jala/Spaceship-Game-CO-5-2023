import pygame
import random

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
class Power:
    POWER_WIDTH = 30
    POWER_HEIGHT = 30
    POWER_SPEED = 10
    POWER_DURATION = random.randint(3, 5)
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.duration = self.POWER_DURATION
        self.image = pygame.transform.scale(self.image, (self.POWER_WIDTH, self.POWER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = 0
        self.is_active = True
        self.is_used = False
    
    def update(self):
        self.rect.y += self.POWER_SPEED
        if self.rect.y == SCREEN_HEIGHT + self.POWER_HEIGHT:
            self.deactive()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def deactive(self):
        self.is_active = False
        self.is_used = True