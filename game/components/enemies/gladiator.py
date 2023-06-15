import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class Gladiator(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 10
    SPEED_Y = 2
    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)