from modules.modules import *
from globalvars.get_user_settings import *

pygame.init()

get_user_settings()
USER_FPS = int(USER_SETTINGS_RAW_LIST[0][5:]) 
USER_WIDTH = int(USER_SETTINGS_RAW_LIST[1][7:])
USER_HEIGHT = int(USER_SETTINGS_RAW_LIST[2][8:])
USER_CHARACTER = USER_SETTINGS_RAW_LIST[3][11:] 
USER_LEVEL = int(USER_SETTINGS_RAW_LIST[4][7:]) 

GAME_CLOCK = pygame.time.Clock() 
GAME_IS_RUNNING = None 
GAME_FPS = USER_FPS  

LEVEL_NUMBER = USER_LEVEL

WINDOW_DISPLAY = None
WINDOW_CAPTION = "Finding El Dorado!"
WINDOW_WIDTH = USER_WIDTH
WINDOW_HEIGHT = USER_HEIGHT
WINDOW_SCROLL_BOUNDARY_X = 200 
WINDOW_SCROLL_BOUNDARY_Y = 150 

PLAYER_VELOCITY = 5 
PLAYER_SPRINT_SPEED = 5
GRAVITY = 1

PLAYER_CHARACTER = USER_CHARACTER
BLOCK_SIZE = 96 

pygame.display.set_caption(WINDOW_CAPTION) 
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #creates the game interface

MENU_BUTTON_WIDTH = 200 
MENU_BUTTON_HEIGHT = 50
MENU_BUTTON_SCALE = (WINDOW_HEIGHT + WINDOW_WIDTH) / 2200
MENU_BUTTON_DISTANCE = 31 * MENU_BUTTON_SCALE
MENU_BUTTON_X_OFFSET = -100 * MENU_BUTTON_SCALE
MENU_BUTTON_Y_OFFSET = -50 * MENU_BUTTON_SCALE
CENTER_MENU_BUTTON_X = (WINDOW_WIDTH / 2) + MENU_BUTTON_X_OFFSET 
CENTER_MENU_BUTTON_Y = (WINDOW_HEIGHT / 2) + MENU_BUTTON_Y_OFFSET  

TITLE_IMAGE = pygame.image.load("assets/MyAssets/finding_el_dorado.png").convert_alpha()

###### MAIN MENU BUTTONS ######
START_IMAGE = pygame.image.load("assets/MyAssets/start.png").convert_alpha()  
HOVER_START_IMAGE = pygame.image.load("assets/MyAssets/start_hover.png").convert_alpha() 
EXIT_IMAGE = pygame.image.load("assets/MyAssets/quit_game.png").convert_alpha()  
HOVER_EXIT_IMAGE = pygame.image.load("assets/MyAssets/quit_game_hover.png").convert_alpha()
MAIN_MENU_IMAGE = pygame.image.load("assets/MyAssets/main_menu.png").convert_alpha()  
HOVER_MAIN_MENU_IMAGE = pygame.image.load("assets/MyAssets/main_menu_hover.png").convert_alpha()
OPTIONS_IMAGE = pygame.image.load("assets/MyAssets/options.png").convert_alpha()  
HOVER_OPTIONS_IMAGE = pygame.image.load("assets/MyAssets/options_hover.png").convert_alpha()
VIDEO_IMAGE = pygame.image.load("assets/MyAssets/video.png").convert_alpha()  
HOVER_VIDEO_IMAGE = pygame.image.load("assets/MyAssets/video_hover.png").convert_alpha()
LEVELS_IMAGE = pygame.image.load("assets/MyAssets/levels.png").convert_alpha()  
HOVER_LEVELS_IMAGE = pygame.image.load("assets/MyAssets/levels_hover.png").convert_alpha()
CHARACTERS_IMAGE = pygame.image.load("assets/MyAssets/characters.png").convert_alpha()  
HOVER_CHARACTERS_IMAGE = pygame.image.load("assets/MyAssets/characters_hover.png").convert_alpha() 

###### LEVEL BUTTONS ###### 
LEVEL_SELECT_IMAGE = pygame.image.load("assets/MyAssets/level_select.png").convert_alpha()
HOVER_LEVEL_SELECT_IMAGE = pygame.image.load("assets/MyAssets/level_select_hover.png").convert_alpha() 
SIGN_1 = pygame.image.load("assets/Menu/Levels/01.png").convert_alpha() 
SIGN_2 = pygame.image.load("assets/Menu/Levels/02.png").convert_alpha()