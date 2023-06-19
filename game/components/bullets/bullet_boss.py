import pygame
from game.components.bullets.bullet_enemy import BulletEnemy 
from game.utils.constants import BULLET_BOSS

class BulletBoss(BulletEnemy):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
    BULLET_IMAGE = BULLET_BOSS
    def __init__(self, center):
        super().__init__(center)