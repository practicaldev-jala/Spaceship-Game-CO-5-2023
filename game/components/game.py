import pygame
import math

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE , WHITE_COLOR, GAME_OVER, RESET
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components import text_utils
from game.components.powers.power_handler import PowerHandler

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
        self.score_history = [] 
        self.score = 0
        self.detailed_score = {}
        self.number_death = 0
        self.started_at = pygame.time.get_ticks()
        self.finished_at = pygame.time.get_ticks()
        self.power_handler = PowerHandler()
    
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
                self.started_at = pygame.time.get_ticks()
                self.playing = True
                self.reset()
                
    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            mouse_input = pygame.mouse.get_pressed()
            self.player.update(user_input, mouse_input, self.bullet_handler)
            self.enemy_handler.update(self.player, self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.power_handler.update(self.player)
            self.score = self.enemy_handler.number_enemy_destroyed
            self.detailed_score = self.enemy_handler.destroyed_enemies
            if not self.player.is_alive:
                pygame.time.delay(200)
                self.finished_at = pygame.time.get_ticks()
                self.playing = False
                self.number_death += 1
                self.score_history.append(self.score)
            
    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_handler.draw(self.screen)
            self.draw_score()
            self.draw_timer()
            self.draw_power_time()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Score: {self.score}', 20, WHITE_COLOR, 1000, 40)
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
    
    def draw_guide(self):
        title, title_rect = text_utils.get_message(f'Controls:', 20, WHITE_COLOR, 1000, 80)
        up, up_rect = text_utils.get_message(f'MOVE UP: W or UP', 20, WHITE_COLOR, 1000, 100)
        left, left_rect = text_utils.get_message(f'MOVE LEFT: A or LEFT', 20, WHITE_COLOR, 1000, 120)
        self.screen.blit(title, title_rect)
        self.screen.blit(up, up_rect)
        self.screen.blit(left, left_rect)
    
    def draw_timer(self):
        current_time = math.floor((pygame.time.get_ticks() - self.started_at) / 1000)
        time, time_rect = text_utils.get_message(f'Time: {current_time} seconds', 20, WHITE_COLOR, height=20)
    
        self.screen.blit(time, time_rect)
    
    def draw_power_time(self):
        if self.player.has_power:
            power_time = round(self.player.power_time - pygame.time.get_ticks() / 1000, 2)
            
            if power_time >= 0:
                time, time_rect = text_utils.get_message(f'{self.player.power_type.capitalize()} is enabled for {power_time}', 20, WHITE_COLOR, 150, 50)
                self.screen.blit(time, time_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()
                
    def draw_menu(self):
        if self.number_death < 1:
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            pos_detailed_score_y =  100
            pos_detailed_score_x = 150
            duration = math.floor((self.finished_at - self.started_at) / 1000)
            
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f"Your score is: {self.score}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            
            deaths, deaths_rect = text_utils.get_message(f"Number of attemps: {self.number_death}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 150)
            max_score, max_score_rect = text_utils.get_message(f"Max score: {max(self.score_history)}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 200)
            time, time_rect = text_utils.get_message(f"Duration: {duration}", 20, WHITE_COLOR, 1000, 20)
            
            for enemy in self.detailed_score:
                specific_score, specific_score_rect = text_utils.get_message(f'Killed {enemy}: {self.detailed_score[enemy]}', 20, WHITE_COLOR, pos_detailed_score_x, pos_detailed_score_y)
                self.screen.blit(specific_score, specific_score_rect)
                pos_detailed_score_y += 30
            
            self.screen.blit(GAME_OVER, (SCREEN_WIDTH // 2 - 200, 100))
            self.screen.blit(RESET, (SCREEN_WIDTH // 2 - 50, 200))
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(deaths, deaths_rect)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(time, time_rect)
            
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()

#Portal Handler o Cambiar mapa por nivel
#Crear clase dashboard para guardar datos
#Maximo score Done
#Explosión por colisión de naves Done
#Numero de intentos Done
#Tiempo jugado Done
#Historial de score Done
#Mostrar numero de cada nave eliminada Done
#Instructivo en pantalla de cómo jugar WAITING
#Arreglar score Done
#Menu de juego para jugar
#Nuevos enemigos y poderes
#Obstaculos (Obstacle handler)
#vidas al jugador y enemigo
#Efectos de sonido
#Música
#Niveles en el juego
#Balas disparadas info
#Balas colisionan
#Boton pausa
#Multijugador
#Datos persistente con JSON Waiting
#Crear Readme WAITING
#En inglés WAITING