import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Striker(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 20
    SPEED_Y = 5
    SHOOTING_TIME = 10
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)