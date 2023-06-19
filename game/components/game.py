import pygame
import math

from game.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE , WHITE_COLOR, GAME_OVER, RESET, HEALTH_0, HEALTH_1, HEALTH_2, HEALTH_3, MUSIC_SOUND
from game.components.spaceship import Spaceship
from game.components.levels.level_1 import Level1
from game.components import text_utils
from game.components.dashboard import Dashboard
from game.components.levels.level_handler import LevelHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.player = Spaceship()
        self.level_handler = LevelHandler(self.player)
        self.dashboard = Dashboard()
        self.started_at = 0
        self.finished_at = 0
        self.current_time = 0
    
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        background_music = pygame.mixer.Sound(MUSIC_SOUND)
        background_music.set_volume(0.2)
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(background_music)
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
            self.player.speed = self.level_handler.level.game_speed
            self.current_time = math.floor((pygame.time.get_ticks() -  self.started_at) / 1000)
            self.player.update(user_input, mouse_input, self.level_handler.bullet_handler)
            self.dashboard.set_score(self.level_handler.enemy_handler.number_enemy_destroyed)
            self.dashboard.set_enemies(self.level_handler.enemy_handler.destroyed_enemies)
            self.level_handler.update(self.dashboard.get_score())
            if not self.player.is_alive:
                pygame.time.delay(200)
                self.playing = False
                self.finished_at = pygame.time.get_ticks()
                self.dashboard.set_duration_time(math.floor((self.finished_at - self.started_at) / 1000))
                self.dashboard.set_deaths(self.dashboard.get_deaths() + 1)
                self.dashboard.add_data_to_history()
            
    def draw(self):
        self.level_handler.draw_background(self.screen)
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.level_handler.draw(self.screen)
            self.draw_score()
            self.draw_lives()
            self.draw_timer()
            self.draw_power_time()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Score: {self.dashboard.get_score()}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)
    
    def draw_lives(self):
        health_width = 60
        health_height = 20
        health_image = HEALTH_0
        if self.player.lives <= 0:
            health_image = HEALTH_0
        elif self.player.lives == 1:
            health_image = HEALTH_1
        elif self.player.lives == 2:
            health_image = HEALTH_2
        elif self.player.lives >= 3:
            health_image = HEALTH_3
    
        lives, lives_rect = text_utils.get_message(f'{self.player.lives}', 20, WHITE_COLOR, 130, 30)
        health_image = pygame.transform.scale(health_image, (health_width, health_height)).convert_alpha()
        self.screen.blit(lives, lives_rect)
        self.screen.blit(health_image, (50, 20))
        
    def draw_guide(self):
        title, title_rect = text_utils.get_message(f'Controls:', 20, WHITE_COLOR, 1000, 80)
        up, up_rect = text_utils.get_message(f'MOVE UP: W or UP', 20, WHITE_COLOR, 1000, 100)
        left, left_rect = text_utils.get_message(f'MOVE LEFT: A or LEFT', 20, WHITE_COLOR, 1000, 120)
        self.screen.blit(title, title_rect)
        self.screen.blit(up, up_rect)
        self.screen.blit(left, left_rect)
    
    def draw_timer(self):
        time, time_rect = text_utils.get_message(f'Time: {self.current_time} seconds', 20, WHITE_COLOR, height=20)
    
        self.screen.blit(time, time_rect)
    
    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) / 1000, 2)
            
            if power_time >= 0:
                time, time_rect = text_utils.get_message(f'{self.player.power_type.capitalize()} is enabled for {power_time}', 20, WHITE_COLOR, 150, 50)
                self.screen.blit(time, time_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()
                
    def draw_menu(self):
        if self.dashboard.get_deaths() < 1:
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            pos_detailed_score_y =  100
            pos_detailed_score_x = 150
            
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f"Your score is: {self.dashboard.get_score()}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            
            deaths, deaths_rect = text_utils.get_message(f"Number of attemps: {self.dashboard.get_deaths()}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 150)
            max_score, max_score_rect = text_utils.get_message(f"Max score: {self.dashboard.get_max_score()}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 200)
            time, time_rect = text_utils.get_message(f"Duration: {self.dashboard.get_duration_time()}", 20, WHITE_COLOR, 1000, 20)
            
            enemies = self.dashboard.get_enemies()
            for enemy in enemies:
                specific_score, specific_score_rect = text_utils.get_message(f'Killed {enemy}: {enemies[enemy]}', 20, WHITE_COLOR, pos_detailed_score_x, pos_detailed_score_y)
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
        self.level_handler.reset()
        self.dashboard.reset()
#Crear clase dashboard para guardar datos Done
#Maximo score Done
#Explosión por colisión de naves Done
#Nuevo espoder de explosion de nave enemiga con escudo False
#Disparo automático del jugador Waiting
#Numero de intentos Done
#Tiempo jugado Done
#Historial de score Done
#Mostrar numero de cada nave eliminada Done
#Enemigos aparecen después de cierto tiempo DONE
#Instructivo en pantalla de cómo jugar WAITING
#Arreglar score Done
#Tiempo a poderes en cada nivel Done
#Mejora de lógica de poderes y power_handler Done
#Colisión de escudo con bala Done
#Poder de super bala (tamaño enorme)
#Balas colisionan Done
#Minigun power
#Toro power
#Portal Handler o Cambiar mapa por nivel
#Menu de juego para jugar
#Nuevos enemigos y poderes
#Obstaculos (Obstacle handler)
#vidas al jugador y enemigo
#Efectos de sonido
#Música
#Niveles en el juego por cada tiempo
#Balas disparadas info
#Boton pausa
#Datos persistente con JSON Waiting
#Crear Readme WAITING
#En inglés WAITING