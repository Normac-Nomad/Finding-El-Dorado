from modules.modules import * 
from globalvars.globalvars import *

def get_background(background_name): #Name is the asset name; function returns a background containing a list (which is the background)
    """  
    Name: get_background
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Creates the background with the passed background name
    Return: Returns the individual background tiles and background image
    """
    background_tile = pygame.image.load(join("assets", "Background", background_name)) 
    _, _, width, height = background_tile.get_rect() # the two underscores would usually contain the X and Y coordinates of the image. We don't need those at the moment
    background = [] 

    for i in range(WINDOW_WIDTH // width + 1): #// is integer divide. Cool innit? 
        for j in range(WINDOW_HEIGHT // height + 1):#these two snippets of code give us an idea of how many of the background asset we need to create the whole background. The +1 is to ensure that there are no gaps in the background
            pos = (i * width, j * height) #this gives us the location of the top right corner of the background asset we are currently printing on to the background.
            background.append(pos) #appending the current background asset to our list 

    return background, background_tile

def draw_window(WINDOW_DISPLAY, background, background_tile, player, objects, offset_x): 
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

    player.draw(WINDOW_DISPLAY, offset_x)

    pygame.display.update()