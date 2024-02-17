from modules.modules import *

pygame.init()

GAME_CLOCK = pygame.time.Clock() 
GAME_IS_RUNNING = None
GAME_FPS = 60  

LEVEL_NUMBER = 2

WINDOW_DISPLAY = None
WINDOW_CAPTION = "Finding El Dorado!"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_SCROLL_BOUNDARY = 200 

MENU_BUTTON_SCALE = (WINDOW_HEIGHT + WINDOW_WIDTH) / 1500 
MENU_BUTTON_DISTANCE = 75 * MENU_BUTTON_SCALE
MENU_BUTTON_X_OFFSET = -100 * MENU_BUTTON_SCALE
MENU_BUTTON_Y_OFFSET = -50 * MENU_BUTTON_SCALE
CENTER_MENU_BUTTON_X = (WINDOW_WIDTH / 2) + MENU_BUTTON_X_OFFSET 
CENTER_MENU_BUTTON_Y = (WINDOW_HEIGHT / 2) + MENU_BUTTON_Y_OFFSET 

PLAYER_VELOCITY = 5 
PLAYER_SPRINT_SPEED = 5
GRAVITY = 1

BLOCK_SIZE = 96 

pygame.display.set_caption(WINDOW_CAPTION) 
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #creates the game interface

START_IMAGE = pygame.image.load("assets/MyAssets/start.png").convert_alpha()  
HOVER_START_IMAGE = pygame.image.load("assets/MyAssets/start_hover.png").convert_alpha() 
EXIT_IMAGE = pygame.image.load("assets/MyAssets/exit.png").convert_alpha()  
HOVER_EXIT_IMAGE = pygame.image.load("assets/MyAssets/exit_hover.png").convert_alpha()

#+#+#+#+#+#+# -- USER SETTINGS -- #+#+#+#+#+#+#