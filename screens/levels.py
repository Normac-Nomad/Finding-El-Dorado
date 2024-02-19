from modules.modules import * 
from globalvars.globalvars import * 

from objects.game_objects import *   
from objects.game_image import * 
from objects.player import * 
from objects.button import *   

def get_background(background_name):
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

def levels(): 

    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)), 
                         MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5) 
    level_1 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 3), LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_1 = GameImage(SIGN_1, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)), (CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 3) + (4 * MENU_BUTTON_SCALE)), MENU_BUTTON_SCALE * 2.5)
    level_2 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE, LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_2 = GameImage(SIGN_2, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)), (CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE + (4 * MENU_BUTTON_SCALE)), MENU_BUTTON_SCALE * 2.5)


    while True:  
     
        WINDOW_DISPLAY.fill((255, 220, 0))

        if (level_1.draw()):  
            update_user_settings(4, "LEVEL: 1")
            return("Level1") 
        
        elif (level_2.draw()): 
            update_user_settings(4, "LEVEL: 2")
            return("Level2")
        
        sign_1.draw() 
        sign_2.draw() 

        if (ingame_menu_button.draw()):
            return("Main")

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                pygame.quit() 
                quit()  

        pygame.display.update()  

def get_level(level_number): 

    if (level_number == 1):
        return level_one()
    elif (level_number == 2): 
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

    return (background, bg_image, player, fire, objects) 

def level_two():   
    background, bg_image = get_background("Yellow.png")  
    player = Player(100, 100, 50, 50)     

    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on() 
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects)

def level_test():   
    
    background, bg_image = get_background("Gray.png")  
    player = Player(100, 100, 50, 50)  

    fire = Fire(100, - WINDOW_HEIGHT, 16, 32)
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(10)] 
    block_wall_left = [Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    block_wall_right = [Block(960 - 97, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    
    objects = [*floor, *block_wall_left, *block_wall_right, fire]  

    return (background, bg_image, player, fire, objects)