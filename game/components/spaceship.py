import pygame
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, EXPLOSION_SHEET_1, DEFAULT_TYPE
from game.components.sprite_sheet import SpriteSheet

class Spaceship:
    X_OFFSET = 40
    Y_OFFSET = 60
    X_POS = (SCREEN_WIDTH // 2) - X_OFFSET
    Y_POS = 500
    SPEED = 10
    SHOOTING_TIME = 20
    
    def __init__(self) -> None:
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.can_shoot = True
        self.shooting_time = 0
        self.explosion_sprite_pos = 0
        self.explosion_sprite = SpriteSheet(EXPLOSION_SHEET_1)
        self.can_explode = False
        self.can_move = True
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def check_is_alive(self):
        if self.is_alive and self.can_explode:
            self.explode()
    
    def explode(self):
        self.can_move = False
        self.explosion_sprite_pos += 0.5
        frame = self.explosion_sprite.get_from_image((int(self.explosion_sprite_pos), int(self.explosion_sprite_pos)), 100, 100, 1, (0,0,0))
        self.image = frame
        if self.explosion_sprite_pos >= 5:
            self.is_alive = False
            
    
    def update(self, user_input, mouse_input, bullet_handler):
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
        self.wait_to_shoot()
        self.check_is_alive()
            
    def move_left(self):
        if self.can_move:
            limit = 0 - self.X_OFFSET
            if self.rect.left > limit:
                self.rect.x -= self.SPEED
            elif self.rect.left == limit:
                self.rect.x = SCREEN_WIDTH + self.X_OFFSET
            
    def move_right(self):
        if self.can_move:
            limit = SCREEN_WIDTH + self.X_OFFSET
            if self.rect.right < limit:
                self.rect.x += self.SPEED
            elif self.rect.right == limit:
                self.rect.x = 0 - self.X_OFFSET

    def move_up(self):
        if self.can_move:
            if self.rect.y > SCREEN_HEIGHT // 2:
                self.rect.y -= self.SPEED
    
    def move_down(self):
        if self.can_move:
            if self.rect.y < SCREEN_HEIGHT - self.Y_OFFSET:
                self.rect.y += self.SPEED
                
    def check_collision(self, object):
        if self.rect.colliderect(object.rect):
                self.kill()
                object.kill()
                
    def wait_to_shoot(self):
        if self.can_shoot == False:
            self.shooting_time += 1
            if self.shooting_time % self.SHOOTING_TIME == 0:
                self.can_shoot = True
    
    def shoot(self, bullet_handler):
        if self.can_shoot and not self.can_explode:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
            self.can_shoot = False
    
    def kill(self):
        self.can_explode = True
    
    def reset(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.X_OFFSET, self.Y_OFFSET))
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.can_shoot = True
        self.shooting_time = 0
        self.explosion_sprite_pos = 0
        self.can_explode = False
        self.can_move = True
        
    def set_power_image(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET))

    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.X_OFFSET, self.Y_OFFSET))

#añadir velocidad dependiente del hilp principal