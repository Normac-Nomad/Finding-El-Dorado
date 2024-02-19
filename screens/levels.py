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
    Parameters: 
        - background_name (str): The name of the background image file
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
    """
    Name: levels
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Allows the user to select a level
    Parameters: N/a
    Return: Returns the next screen to be displayed ('Level1', 'Level2', or 'Main')
    """
    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)),
                                MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5)
    
    level_1 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 9),
                     LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_1 = GameImage(SIGN_1, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)),
                       (CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 9) + (4 * MENU_BUTTON_SCALE)), MENU_BUTTON_SCALE * 2.5)

    level_2 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 7),
                     LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_2 = GameImage(SIGN_2, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)),
                       (CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 7) + (4 * MENU_BUTTON_SCALE)),MENU_BUTTON_SCALE * 2.5)

    level_3 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 5),
                     LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_3 = GameImage(SIGN_3, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)),
                       (CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 5) + (4 * MENU_BUTTON_SCALE)), MENU_BUTTON_SCALE * 2.5)

    level_4 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 3),
                     LEVEL_SELECT_IMAGE, HOVER_LEVEL_SELECT_IMAGE, MENU_BUTTON_SCALE)
    sign_4 = GameImage(SIGN_4, ((WINDOW_WIDTH / 2) + (40 * MENU_BUTTON_SCALE)),
                       (CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 3) + (4 * MENU_BUTTON_SCALE)), MENU_BUTTON_SCALE * 2.5)

    while True:
        WINDOW_DISPLAY.fill((255, 220, 0))

        if level_1.draw():
            update_user_settings(4, "LEVEL: 1")
            return "Level1"
        elif level_2.draw():
            update_user_settings(4, "LEVEL: 2")
            return "Level2"
        elif level_3.draw():
            update_user_settings(4, "LEVEL: 3")
            return "Level3"
        elif level_4.draw():
            update_user_settings(4, "LEVEL: 4")
            return "Level4"

        sign_1.draw()
        sign_2.draw()
        sign_3.draw()
        sign_4.draw()

        if ingame_menu_button.draw():
            return "Main"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

def get_level(level_number): 
    """
    Name: get_level
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Retrieves the specified level
    Parameters: 
        - level_number (int): The number of the level to retrieve
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """
    if level_number == 1:
        return level_one()
    elif level_number == 2:
        return level_two()
    elif level_number == 3:
        return level_three()
    elif level_number == 4:
        return last_level()
    else:
        return level_test()

def level_one(): 
    """
    Name: level_one
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Generates information for Level 1
    Parameters: N/a
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """
    background, bg_image = get_background("Sky.png")  
    player = Player(100, 100, 50, 50)  

    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on()
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects) 

def level_two():   
    """
    Name: level_two
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Generates information for Level 2
    Parameters: N/a
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """ 
    background, bg_image = get_background("Purple.png")  
    player = Player(100, 100, 50, 50)     

    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on() 
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects)

def level_three():
    """
    Name: level_three
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Generates information for the third level
    Parameters: N/a
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """ 

    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50)

    fire_1 = Fire(200, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire_2 = Fire(400, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire_3 = Fire(600, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire_4 = Fire(800, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)

    fire_1.on()

    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)]

    objects = [*floor, Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * 2), BLOCK_SIZE), fire_1, fire_2, fire_3, fire_4]

    return (background, bg_image, player, fire_1, objects) 

def last_level():
    """
    Name: last_level
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Generates the last level
    Parameters: N/a
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """ 
    background, bg_image = get_background("Yellow.png")  
    player = Player(100, 100, 50, 50)     

    fire = Fire(100, -200, 16, 32)
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    floor2 = [Block(i * BLOCK_SIZE + 2000, WINDOW_HEIGHT - BLOCK_SIZE + 200, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)]  
    objects = [*floor, *floor2, fire]  

    return (background, bg_image, player, fire, objects)

def level_test():   
    """
    Name: level_test
    Location: .../finding-el-dorado/functions/window_display_functions 
    Purpose: Generates information for a test level 
    Parameters: N/a
    Return: Returns a tuple containing information about the level (background, bg_image, player, fire, objects)
    """ 
    background, bg_image = get_background("Gray.png")  
    player = Player(100, 100, 50, 50)  

    fire = Fire(100, - WINDOW_HEIGHT, 16, 32)
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(10)] 
    block_wall_left = [Block(0, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    block_wall_right = [Block(960 - 97, WINDOW_HEIGHT - (BLOCK_SIZE * (i + 2)), BLOCK_SIZE) for i in range(WINDOW_HEIGHT // 96)]
    
    objects = [*floor, *block_wall_left, *block_wall_right, fire]  

    return (background, bg_image, player, fire, objects)
