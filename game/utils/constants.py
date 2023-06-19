import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Stars.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))

HEALTH_0 = pygame.image.load(os.path.join(IMG_DIR, 'Other/health_0.png'))

HEALTH_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/health_1.png'))

HEALTH_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/health_2.png'))

HEALTH_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/health_3.png'))

FIRE = pygame.image.load(os.path.join(IMG_DIR, 'Other/fire.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
DESTRUCTOR_TYPE = 'destructor'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_DESTRUCTOR = pygame.image.load(os.path.join(IMG_DIR, 'Spaceship/spaceship_destructor.png'))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_boss.png"))


SHOOT_SOUND = os.path.join(IMG_DIR, "Sounds/shoot_sound.wav")
MUSIC_SOUND = os.path.join(IMG_DIR, "Sounds/background_music.mp3")

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

ENEMY_FINAL = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_final.png"))

EXPLOSION_SHEET_1 = pygame.image.load(os.path.join(IMG_DIR, "Effect/explosion_1.png"))

FONT_STYLE = 'freesansbold.ttf'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'
BULLET_BOSS_TYPE = 'boss'

#BACKGROUND LEVELS

BG_LEVEL_1 = pygame.image.load(os.path.join(IMG_DIR, 'Levels/Space_3.png'))
BG_LEVEL_2 = pygame.image.load(os.path.join(IMG_DIR, 'Levels/Space_2.png'))
BG_LEVEL_3 = pygame.image.load(os.path.join(IMG_DIR, 'Levels/Space_3.png'))
BG_LEVEL_4 = pygame.image.load(os.path.join(IMG_DIR, 'Levels/Space_4.png'))
BG_LEVEL_5 = pygame.image.load(os.path.join(IMG_DIR, 'Levels/Space_5.png'))

