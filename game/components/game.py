import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE , WHITE_COLOR
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components import text_utils
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.score = 0
        self.number_death = 0
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()
                
    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            mouse_input = pygame.mouse.get_pressed()
            self.player.update(user_input, mouse_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.number_enemy_destroyed
            if not self.player.is_alive:
                pygame.time.delay(200)
                self.playing = False
                self.number_death += 1
            
    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is {self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)
    
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f"Your score is {self.score}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
    def reset(self):
        self.number_death = 0
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        
        
#Maximo score
#Numero de intentos
#Tiempo jugado
#Historial de score
#Mostrar numero de cada nave eliminada
#Instructivo en pantalla de cómo jugar
#Arreglar score
#Datos persistente con JSON
#Crear Readme
#En inglés