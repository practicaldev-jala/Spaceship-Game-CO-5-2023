import pygame
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, EXPLOSION_SHEET_1, DEFAULT_TYPE, SHIELD_TYPE, DESTRUCTOR_TYPE, HEART_TYPE
from game.components.sprite_sheet import SpriteSheet

class Spaceship:
    X_OFFSET = 40
    Y_OFFSET = 60
    X_POS = (SCREEN_WIDTH // 2) - X_OFFSET
    Y_POS = 500
    SPEED = 10
    SHOOTING_TIME = 500
    LIVES = 3
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET)).convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.lives = self.LIVES
        self.is_alive = True
        self.can_shoot = False
        self.shooting_time = pygame.time.get_ticks() + self.SHOOTING_TIME
        self.explosion_sprite_pos = 0
        self.explosion_sprite = SpriteSheet(EXPLOSION_SHEET_1)
        self.can_explode = False
        self.can_move = True
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0
        self.speed = self.SPEED
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def check_is_alive(self):
        if self.is_alive and self.can_explode:
            self.explode()
    
    def explode(self):
        self.can_move = False
        self.explosion_sprite_pos += 0.5
        frame = self.explosion_sprite.get_from_image((int(self.explosion_sprite_pos), int(self.explosion_sprite_pos)), 100, 100, 1, (0,0,0))
        self.image = frame.convert_alpha()
        if self.explosion_sprite_pos >= 5:
            self.is_alive = False
            
    
    def update(self, user_input, mouse_input, bullet_handler):
        
        self.check_is_alive()
        
        if user_input[pygame.K_SPACE] or mouse_input[0]:
            self.shoot(bullet_handler)
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
            
    def move_left(self):
        if self.can_move:
            limit = 0 - self.X_OFFSET
            if self.rect.left > limit:
                self.rect.x -= self.speed
            elif self.rect.left <= limit:
                self.rect.x = SCREEN_WIDTH + self.X_OFFSET
            
    def move_right(self):
        if self.can_move:
            limit = SCREEN_WIDTH + self.X_OFFSET
            if self.rect.right < limit:
                self.rect.x += self.speed
            elif self.rect.right >= limit:
                self.rect.x = 0 - self.X_OFFSET

    def move_up(self):
        if self.can_move:
            if self.rect.y > SCREEN_HEIGHT // 2:
                self.rect.y -= self.speed
    
    def move_down(self):
        if self.can_move:
            if self.rect.y < SCREEN_HEIGHT - self.Y_OFFSET:
                self.rect.y += self.speed
                
    def check_collision(self, object):
        if self.rect.colliderect(object.rect):
            if self.has_power and self.power_type == SHIELD_TYPE:
                pass
            elif self.has_power and self.power_type == DESTRUCTOR_TYPE:
                object.kill()
            elif self.has_power and self.power_type == HEART_TYPE:
                    pass
            else:
                object.kill()
                self.kill()
                
    def shoot(self, bullet_handler):
        if self.can_shoot and not self.can_explode:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
            self.can_shoot = False
        elif not self.can_shoot:
            if pygame.time.get_ticks() > self.shooting_time:
                self.shooting_time = pygame.time.get_ticks() + self.SHOOTING_TIME
                self.can_shoot = True
                
    def kill(self):
        if self.lives > 0:
            self.lives -= 1
        if self.lives <= 0:
            self.can_explode = True
    
    def reset(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.X_OFFSET, self.Y_OFFSET))
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.lives = self.LIVES
        self.is_alive = True
        self.can_shoot = True
        self.shooting_time = pygame.time.get_ticks() + self.SHOOTING_TIME
        self.explosion_sprite_pos = 0
        self.can_explode = False
        self.can_move = True
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0
    
    def set_power(self, power_type, power_image, power_duration):
        self.power_type = power_type
        self.has_power = True
        self.power_time = pygame.time.get_ticks() + (power_duration * 1000)
        self.image = power_image
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET)).convert_alpha()

    def increment_health(self):
        self.lives += 1

    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET)).convert_alpha()

#añadir velocidad dependiente del hilp principal