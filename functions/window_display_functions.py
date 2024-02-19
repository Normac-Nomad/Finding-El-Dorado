from modules.modules import * 
from globalvars.globalvars import *  

from objects.player import *   
from objects.game_objects import *  
from objects.button import *  

from screens.levels import * 

def get_background(background_name):
    """  
    Name: get_background
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Creates the background with the passed background name
    Parameters:
        - background_name: The asset name for the background
    Return: Returns the background image and the individual background tiles in said order
    """ 
    try:
        background_tile = pygame.image.load(join("assets", "Background", background_name))  
    except: 
        background_tile = pygame.image.load(join("assets", "MyAssets", background_name)) 

    _, _, width, height = background_tile.get_rect()
    background = [] 

    for i in range(WINDOW_WIDTH // width + 1): 
        for j in range(WINDOW_HEIGHT // height + 1):  
            pos = (i * width, j * height)  
            background.append(pos)

    return (background, background_tile)

def player_close_to_x_boundary(player, offset_x, scroll_width): 
    """  
    Name: player_close_to_boundary
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Determines if a player is getting too close to the screen edge. 
                    If so, return the offset needed to keep the player in frame.
    Parameters:
        - player: Player object
        - offset_x: X offset
        - scroll_width: Width for scrolling
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
    
def player_close_to_y_boundary(player, offset_y, scroll_width): 
    """  
    Name: player_close_to_boundary
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Determines if a player is getting too close to the screen edge. 
                    If so, return the offset needed to keep the player in frame.
    Parameters:
        - player: Player object
        - offset_y: Y offset
        - scroll_width: Width for scrolling
    Return: Offset to keep the player in frame.
    """ 
    if (
        ((player.rect.top - offset_y >= WINDOW_HEIGHT - scroll_width) and player.y_vel > 0) 
        or 
        ((player.rect.bottom - offset_y <= scroll_width) and player.y_vel < 0)
    ): 
        return player.y_vel 
    else:  
        return 0  

def quit_program(): 
    """  
    Name: Quit game
    Location: .../finding-el-dorado/functions/window_display_functions
    Purpose: Completely quits the game and program 
    Parameters: N/a
    Return: N/a
    """  
    pygame.quit()
    quit()
