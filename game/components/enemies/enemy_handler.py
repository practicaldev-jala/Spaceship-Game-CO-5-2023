import random
from game.components.enemies.ship import Ship
from game.components.enemies.striker import Striker
from game.components.enemies.gladiator import Gladiator

class EnemyHandler:
    def __init__(self):
        self.default_enemies = [Ship, Striker, Gladiator]
        self.enemies = []
        self.number_enemy_destroyed = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.number_enemy_destroyed += 1
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 4:
            new_enemy = random.choice(self.default_enemies)
            self.enemies.append(new_enemy())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0