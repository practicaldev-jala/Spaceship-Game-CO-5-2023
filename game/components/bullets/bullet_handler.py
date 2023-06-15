from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import  BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer

class BulletHandler:
    def __init__(self):
        self.bullets = []
    
    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_active:
                self.remove_bullet(bullet)
            elif type(bullet) == BulletPlayer:
                bullet.update(enemies)
            else:
                bullet.update(player)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        if type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))
            
    def remove_bullet(self, enemy):
        self.bullets.remove(enemy)