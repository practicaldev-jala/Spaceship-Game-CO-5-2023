import pygame
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, EXPLOSION_SHEET_1

class Spaceship:
    X_OFFSET = 40
    Y_OFFSET = 60
    X_POS = (SCREEN_WIDTH // 2) - X_OFFSET
    Y_POS = 500
    SPEED = 10
    SHOOTING_TIME = 20
    
    def __init__(self) -> None:
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.can_shoot = True
        self.shooting_time = 0
        self.explosion_sprite = 0
        self.can_explode = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def check_is_alive(self):
        if self.is_alive and self.can_explode:
            self.explode()
    
    def explode(self):
        self.explosion_sprite += 0.2
        frame = self.get_from_image(EXPLOSION_SHEET_1, int(self.explosion_sprite), 100, 100, 1, (0,0,0))
        self.image = frame
        if self.explosion_sprite >= 5:
            self.explosion_sprite = 0
            self.is_alive = False
            
    def get_from_image(self, sheet, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), (frame * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        
        return image
    
    def update(self, user_input, mouse_input, bullet_handler):
        if user_input[pygame.K_SPACE] or mouse_input[0]:
            self.shoot(bullet_handler)
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        self.wait_to_shoot()
        self.check_is_alive()
            
    def move_left(self):
        limit = 0 - self.X_OFFSET
        if self.rect.left > limit:
            self.rect.x -= self.SPEED
        elif self.rect.left == limit:
            self.rect.x = SCREEN_WIDTH + self.X_OFFSET
            
    def move_right(self):
        limit = SCREEN_WIDTH + self.X_OFFSET
        if self.rect.right < limit:
            self.rect.x += self.SPEED
        elif self.rect.right == limit:
            self.rect.x = 0 - self.X_OFFSET

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SPEED
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.Y_OFFSET:
            self.rect.y += self.SPEED
    
    def wait_to_shoot(self):
        if self.can_shoot == False:
            self.shooting_time += 1
            if self.shooting_time % self.SHOOTING_TIME == 0:
                self.can_shoot = True
    
    def shoot(self, bullet_handler):
        if self.can_shoot:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
            self.can_shoot = False
    
    def kill(self):
        self.can_explode = True
#añadir velocidad dependiente del hilp principal