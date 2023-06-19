import pygame
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE, BULLET_BOSS_TYPE, SHOOT_SOUND
from game.components.bullets.bullet_enemy import  BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer
from game.components.bullets.bullet_boss import BulletBoss

class BulletHandler:
    def __init__(self):
        self.bullets = []
    
    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_active:
                self.remove_bullet(bullet)
            elif type(bullet) == BulletPlayer:
                bullet.update(enemies, self.bullets)
            else:
                bullet.update(player)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))
        elif type == BULLET_BOSS_TYPE:
            self.bullets.append(BulletBoss(center))
        pygame.mixer.music.load(SHOOT_SOUND)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
            
    def remove_bullet(self, enemy):
        self.bullets.remove(enemy)
    
    def reset(self):
        self.bullets = []