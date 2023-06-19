import pygame
import random

class EnemyHandler:
    def __init__(self, enemy_limit, spawn_delay, default_enemies):
        self.default_enemies = default_enemies
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.destroyed_enemies = {}
        self.enemy_limit = enemy_limit
        self.spawn_delay = spawn_delay
        self.when_appears = spawn_delay

    def update(self, player, bullet_handler, speed):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler, speed)
            player.check_collision(enemy)
            if enemy.is_destroyed:
                try:
                    self.number_enemy_destroyed += 1
                    self.destroyed_enemies[str(type(enemy).__name__)] += 1 
                except KeyError:
                    self.destroyed_enemies[str(type(enemy).__name__)] = 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)
    
    def set_new_level(self, enemy_limit, spawn_delay, default_enemies):
        self.enemy_limit = enemy_limit
        self.spawn_delay = spawn_delay
        self.default_enemies = default_enemies
        
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        current_time = pygame.time.get_ticks()
        if len(self.enemies) < self.enemy_limit and current_time >= self.when_appears:
            new_enemy = random.choice(self.default_enemies)
            self.enemies.append(new_enemy())
            self.when_appears += self.spawn_delay
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.destroyed_enemies = {}