from modules.modules import * 
from globalvars.globalvars import *   


from functions.sprite_functions import *  
from functions.window_display_functions import *   
from functions.collision import *  
from functions.player_movement import *  

from objects.game_objects import * 
from objects.player import *   

from screens.levels import *

######################## MAIN ########################

def main(window):  
    
    background, bg_image, the_player, fire, objects, offset_x = get_level()

    game_is_running = True
    while game_is_running:
        GAME_CLOCK.tick(GAME_FPS)

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): #if the user X's out the window
                game_is_running = False #game is no longer running
                break    

            if (event.type == pygame.KEYDOWN): 
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and the_player.jump_count < 2): 
                    the_player.jump()
                    
        frame_update(the_player, fire, window, background, bg_image, objects, offset_x)
        offset_x += player_close_to_boundary(the_player, offset_x, WINDOW_SCROLL_BOUNDARY)

    pygame.quit()
    quit()

#the line below executes only when main is run directly; 
#prevents it from running indirectly if something is imported from main.py's event loop
if __name__ == "__main__": 
    main(WINDOW_DISPLAY)