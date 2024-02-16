from modules.modules import *

pygame.init()

GAME_CLOCK = pygame.time.Clock() 
GAME_IS_RUNNING = None
GAME_FPS = 60 

WINDOW_DISPLAY = None
WINDOW_CAPTION = "Finding El Dorado!"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400 
WINDOW_SCROLL_BOUNDARY = 200

PLAYER_VELOCITY = 5 
PLAYER_SPRINT_SPEED = 5
GRAVITY = 1

BLOCK_SIZE = 96 

pygame.display.set_caption(WINDOW_CAPTION) 
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #creates the game interface