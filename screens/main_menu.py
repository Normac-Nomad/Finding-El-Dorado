from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import * 
from objects.game_objects import *   
from objects.player import *  
from screens.levels import * 

def main_menu(window):  
    """  
    Name: main_menu
    Location: .../finding-el-dorado/functions/window_display_functions
    Purpose: Runs the main menu screen for the user
    Return: N/a
    """    
    background, bg_image, the_player, fire, objects, offset_x = get_level()

    while True:
        GAME_CLOCK.tick(GAME_FPS)

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT):
                quit_program()

            if (event.type == pygame.KEYDOWN): 
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and the_player.jump_count < 2): 
                    the_player.jump()
                    
        level_frame_update(the_player, fire, window, background, bg_image, objects, offset_x)
        offset_x += player_close_to_boundary(the_player, offset_x, WINDOW_SCROLL_BOUNDARY)

def main_menu_update(background, background_tile): 
    for tile in background:
        WINDOW_DISPLAY.blit(background_tile, tile)