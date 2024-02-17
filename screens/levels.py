from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *  
from objects.game_objects import *   
from objects.player import *

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

def get_level(): 
    if (LEVEL_NUMBER == 1):
        return level_one()
    elif (LEVEL_NUMBER == 2): 
        return level_two() 
    else: 
        return level_test()

def level_one():   
    
    background, bg_image = get_background("Sky.png")  
    player = Player(100, 100, 50, 50) 

    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on()
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects, 0) 

def level_two():   
    
    background, bg_image = get_background("Yellow.png")  
    player = Player(100, 100, 50, 50)    

    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on() 
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects, 0)

def level_test():   
    
    background, bg_image = get_background("Gray.png")  
    player = Player(100, 100, 50, 50)    

    fire = Fire(100, - WINDOW_HEIGHT, 16, 32)
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(10)] 
    block_wall_left = [Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    block_wall_right = [Block(960 - 97, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    
    objects = [*floor, *block_wall_left, *block_wall_right, fire]  

    return (background, bg_image, player, fire, objects, 0)