from modules.modules import * 
from globalvars.globalvars import *  

from functions.sprite_functions import *  
from functions.window_display_functions import *   
from functions.collision import *  
from functions.player_movement import *  

from objects.game_objects import * 
from objects.player import *   

from levels.levels import *

######################## MAIN ########################

def main(window):  
    
    background, bg_image, player_zero, fire, objects = get_level()

    offset_x = 0 
    scroll_area_width = WINDOW_SCROLL_BOUNDARY #when the player gets to "scroll_area_width" (200 pixels) the screen will begin scrolling

    GAME_IS_RUNNING = True

    while GAME_IS_RUNNING:
        GAME_CLOCK.tick(GAME_FPS)

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): #if the user X's out the window
                GAME_IS_RUNNING = False #game is no longer running
                break    

            if (event.type == pygame.KEYDOWN): 
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and player_zero.jump_count < 2): 
                    player_zero.jump()
                    
        #frame_update(player_zero,)
        player_zero.loop(GAME_FPS) 
        fire.loop()
        handle_move(player_zero, objects)
        draw_window(window, background, bg_image, player_zero, objects, offset_x)  

        offset_x += player_close_to_boundary(player_zero, offset_x, scroll_area_width)

    pygame.quit() 
    quit()

#the line below executes only when main is run directly prevents it from running indirectly if something is imported from main.py's event loop
if __name__ == "__main__": 
    main(WINDOW_DISPLAY)