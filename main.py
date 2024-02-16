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
    '''#this chunk in level 1
    background, bg_image = get_background(BACKGROUND_IMAGE_NAME) #get_background returns the list and image
    player = Player(100, 100, 50, 50)   
    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on()
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] #turn this into multiple functions, way to complicated for one line in the video @1:08:39
    objects = [*floor, Block(0, WINDOW_HEIGHT - BLOCK_SIZE * 2, BLOCK_SIZE), fire] #"*thing" breaks everything into it's individual elements and passes them into the objects list; we're just creating the different blocks ontop of the floor
    '''
    background, bg_image, player, fire, objects = level_one()

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
                if (((event.key == pygame.K_SPACE) or (event.key == pygame.K_w)) and player.jump_count < 2): 
                    player.jump()
                    
        player.loop(GAME_FPS) 
        fire.loop()
        handle_move(player, objects)
        draw_window(window, background, bg_image, player, objects, offset_x) 
        offset_x += player_close_to_boundary(player, offset_x, scroll_area_width)

    pygame.quit() 
    quit()

#the line below executes only when main is run directly prevents it from running indirectly if something is imported from main.py's event loop
if __name__ == "__main__": 
    main(WINDOW_DISPLAY) 