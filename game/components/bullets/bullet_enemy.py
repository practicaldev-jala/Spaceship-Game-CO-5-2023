import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY
class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
    
    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            player.is_alive = False
        
#Implementar método morir en player
#Agregar balas al usuario
#Cada que choque con el enemigo, el enemigo debe desaparecer
#Solamente dispara cuando se presiona la tecla espacio
#Con mouse