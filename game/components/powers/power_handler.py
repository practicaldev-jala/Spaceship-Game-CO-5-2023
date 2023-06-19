import pygame
import random
from game.components.powers.shield import Shield
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SHIELD_TYPE, SPACESHIP_DESTRUCTOR, DESTRUCTOR_TYPE, HEART_TYPE

class PowerHandler:
    
    def __init__(self, power_limit, spawn_delay, default_powers):
        self.default_powers = default_powers
        self.powers = []
        self.power_limit = power_limit
        self.spawn_delay = spawn_delay
        self.when_appears = spawn_delay
        
    def add_power(self):
        new_power = random.choice(self.default_powers)
        self.powers.append(new_power())
        self.when_appears += self.spawn_delay
    
    def update(self, player):
        current_time = pygame.time.get_ticks()
        
        if len(self.powers) <= self.power_limit and current_time >= self.when_appears:
            self.add_power()
            
        for power in self.powers:
            power.update()
            
            if not power.is_active:
                self.remove_power(power)
                
            if player.rect.colliderect(power.rect) and not power.is_used:
                if power.type == SHIELD_TYPE:
                    player.set_power(power.type, SPACESHIP_SHIELD, power.duration)
                elif power.type == DESTRUCTOR_TYPE:
                    player.set_power(power.type, SPACESHIP_DESTRUCTOR, power.duration)
                elif power.type == HEART_TYPE:
                    player.increment_health()
                power.deactive()
    
    def set_new_level(self, power_limit, spawn_delay, default_powers):
        self.enemy_limit = power_limit
        self.spawn_delay = spawn_delay
        self.default_powers = default_powers
                
    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)
    
    def remove_power(self, power):
        self.powers.remove(power)
    
    def reset(self):
        self.powers = []
    
