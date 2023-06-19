import pygame
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletPlayer(Bullet):
    WIDTH = 15
    HEIGHT = 32
    SPEED = 20
    
    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()
        super().__init__(self.image, center)
        

    def update(self, enemies, bullets):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0 - self.HEIGHT:
            self.deactive()
            
        for bullet in bullets:
            if type(bullet) == BulletEnemy:
                if self.rect.colliderect(bullet.rect):
                    self.deactive()
                    bullet.deactive()
                
        for enemy in enemies:
            super().update(enemy)
            
#Implementar método morir en player
#Agregar balas al usuario
#Cada que choque con el enemigo, el enemigo debe desaparecer
#Solamente dispara cuando se presiona la tecla espacio
#Con mouse