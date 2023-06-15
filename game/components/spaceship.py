import pygame
from game.utils.constants import SPACESHIP
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    X_OFFSET = 40
    Y_OFFSET = 60
    X_POS = (SCREEN_WIDTH // 2) - X_OFFSET
    Y_POS = 500
    SPEED = 10
    
    def __init__(self) -> None:
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
            
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

#añadir velocidad dependiente del hilp principal