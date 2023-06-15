import random
from game.components.enemies.ship import Ship
from game.components.enemies.striker import Striker
from game.components.enemies.gladiator import Gladiator

class EnemyHandler:
    def __init__(self):
        self.default_enemies = [Ship, Striker, Gladiator]
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Striker())
        self.enemies.append(Gladiator())
    
    def update(self):
        for enemy in self.enemies:
            if enemy.is_alive:
                enemy.update()
            else:
                current_index = self.enemies.index(enemy)
                new_enemy = random.choice(self.default_enemies)
                del self.enemies[current_index]
                self.enemies.append(new_enemy())
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)