import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletPlayer(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
    
    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        

    def update(self, enemies):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0 - self.HEIGHT:
            self.deactive()
        for enemy in enemies:
            super().update(enemy)
#Implementar método morir en player
#Agregar balas al usuario
#Cada que choque con el enemigo, el enemigo debe desaparecer
#Solamente dispara cuando se presiona la tecla espacio
#Con mouse