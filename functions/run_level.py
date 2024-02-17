from modules.modules import * 
from globalvars.globalvars import *     

from functions.player_movement import * 
from functions.window_display_functions import *  

from screens.levels import *
   
def level_frame_update(player, fire, window, background, bg_image, objects, offset_x):
    """  
    Name: frame_update
    Location: .../finding-el-dorado/functions/run_level
    Purpose: Updates the positions and states of all games objects on screen every frame
    Return: N/a
    """ 
    player.loop(GAME_FPS) 
    fire.loop()
    handle_move(player, objects) 
    draw_window(window, background, bg_image, player, objects, offset_x)    

def play_game(window):   
    """  
    Name: play_game
    Location: .../finding-el-dorado/functions/run_level 
    Purpose: Begins the game and selected level for the user
    Return: N/a 

    Note: The player can exit the game and the program from this
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

#add quit game funtion
