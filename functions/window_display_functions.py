from modules.modules import * 
from globalvars.globalvars import *  

from objects.player import *   
from objects.game_objects import *  
from objects.button import *  

from screens.levels import * 

def get_background(background_name): #Name is the asset name; function returns a background containing a list (which is the background)
    """  
    Name: get_background
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Creates the background with the passed background name
    Return: Returns the background image and the individual background tiles in said order
    """ 
    try:
        background_tile = pygame.image.load(join("assets", "Background", background_name))  
    except: 
        background_tile = pygame.image.load(join("assets", "MyAssets", background_name)) 

    _, _, width, height = background_tile.get_rect()
    background = [] 

    for i in range(WINDOW_WIDTH // width + 1): #// is integer divide. Cool innit? 
        for j in range(WINDOW_HEIGHT // height + 1):#these two snippets of code give us an idea of how many of the background asset we need to create the whole background. The +1 is to ensure that there are no gaps in the background
            pos = (i * width, j * height) #this gives us the location of the top right corner of the background asset we are currently printing on to the background.
            background.append(pos) #appending the current background asset to our list 

    return background, background_tile

def draw_level_window(WINDOW_DISPLAY, background, background_tile, player, objects, offset_x): 
    """  
    Name: draw_window
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Creating and updating the game visials
    Return: N/a
    """ 
    for tile in background: 
        WINDOW_DISPLAY.blit(background_tile, tile) #actually drawing our background with the blit function using the tuple from get_background

    for obj in objects: 
        obj.draw(WINDOW_DISPLAY, offset_x) 

    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH + 10)), (WINDOW_HEIGHT - (WINDOW_HEIGHT + 10)), 
                         START_IMAGE, HOVER_START_IMAGE, MENU_BUTTON_SCALE) 
    if (ingame_menu_button.draw()):
            return(True)
    
    player.draw(WINDOW_DISPLAY, offset_x)
    pygame.display.update()

def player_close_to_boundary(player, offset_x, scroll_width): 
    """  
    Name: player_close_to_boundary
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Determines if a player is getting to close to the screen edge. 
                    If so, return the offset needed to keep the player in frame.
    Return: Offset to keep the player in frame.
    """ 
    if (
    ((player.rect.right - offset_x >= WINDOW_WIDTH - scroll_width) and player.x_vel > 0) 
    or 
    ((player.rect.left - offset_x <= scroll_width) and player.x_vel < 0)
    ): 
        return player.x_vel 
    else:  
        return 0  

def quit_program():
    """  
    Name: Quit game
    Location: .../finding-el-dorado/functions/window_display_functions
    Purpose: Completely quits the game and program
    Return: N/a
    """  
    #Add save level feature 
    #Add save user prefrences feature (maybe not here)
    pygame.quit()
    quit()
