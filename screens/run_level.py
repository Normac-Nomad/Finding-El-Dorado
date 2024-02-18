from modules.modules import * 
from globalvars.globalvars import *     

from functions.player_movement import * 
from functions.window_display_functions import *  
 
from screens.levels import *

def play_game():   
    """  
    Name: play_game
    Location: .../finding-el-dorado/functions/run_level 
    Purpose: Begins the game and selected level for the user
    Return: N/a 

    Note: The player can exit the game and the program from this
    """ 
    background, bg_image, the_player, fire, objects = get_level(LEVEL_NUMBER) 
    offset_x = 0
    offset_y = 0

    while True:
        GAME_CLOCK.tick(GAME_FPS) 

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT):
                quit_program()

            if (event.type == pygame.KEYDOWN): 
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and the_player.jump_count < 2): 
                    the_player.jump()
                    
        if level_frame_update(the_player, fire, background, bg_image, objects, offset_x, offset_y): 
            return("Main") 
        
        offset_x += player_close_to_x_boundary(the_player, offset_x, WINDOW_SCROLL_BOUNDARY_X)
        offset_y += player_close_to_y_boundary(the_player, offset_y, WINDOW_SCROLL_BOUNDARY_Y)

def play_game_level(level):   
    """  
    Name: play_game
    Location: .../finding-el-dorado/functions/run_level 
    Purpose: Begins the game and selected level for the user
    Return: N/a 

    Note: The player can exit the game and the program from this
    """ 
    background, bg_image, the_player, fire, objects = get_level(level) 
    offset_x = 0
    offset_y = 0

    while True:
        GAME_CLOCK.tick(GAME_FPS) 

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT):
                quit_program()

            if (event.type == pygame.KEYDOWN): 
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and the_player.jump_count < 2): 
                    the_player.jump()
                    
        if level_frame_update(the_player, fire, background, bg_image, objects, offset_x, offset_y): 
            return("Main") 
        
        offset_x += player_close_to_x_boundary(the_player, offset_x, WINDOW_SCROLL_BOUNDARY_X)
        offset_y += player_close_to_y_boundary(the_player, offset_y, WINDOW_SCROLL_BOUNDARY_Y)

def level_frame_update(player, fire, background, bg_image, objects, offset_x, offset_y):
    """  
    Name: frame_update
    Location: .../finding-el-dorado/functions/run_level
    Purpose: Updates the positions and states of all games objects on screen every frame
    Return: N/a
    """ 
    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)), 
                         MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5) 

    player.loop(GAME_FPS) 
    fire.loop()
    handle_move(player, objects) 
      
    for tile in background: 
        WINDOW_DISPLAY.blit(bg_image, tile)

    for obj in objects: 
        obj.draw(WINDOW_DISPLAY, offset_x, offset_y)

    
    if (ingame_menu_button.draw()):
            return(True)
    
    player.draw(WINDOW_DISPLAY, offset_x, offset_y)
    pygame.display.update()
