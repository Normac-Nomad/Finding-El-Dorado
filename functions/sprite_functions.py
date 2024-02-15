from modules.modules import * 
from globalvars.globalvars import *  

def flip_sprite(sprites):  
    """  
    Name: flip_sprites
    Location: .../finding-el-dorado/functions/sprite_functions 
    Purpose: Flips sprites
    Return: Flipped sprite
    """ 
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]  

def load_sprite_sheets(dir1, dir2, width, height, direction = False):  
    """  
    Name: load_sprite_sheets
    Location: .../finding-el-dorado/functions/sprite_functions 
    Purpose: Loads sprites sheets with passed directories and dimensions
    Return: Returns the sprites sheets frame by frame in a list
    """ 
    path = join("assets", dir1, dir2) 
    images = [f for f in listdir(path) if isfile(join(path, f))] #loads every single file in the directory to then be split 
            
    all_sprites = {} 

    for image in images: 
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()# !! DON'T UNDERSTAND !! ;convert alpha allows us to import a transparent background image

        sprites = [] 
        for i in range(sprite_sheet.get_width() // width): #chops up the sprite sheet into individual frames
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32) #creates the frame for our animation 
            rect = pygame.Rect(i * width, 0, width, height) 
            surface.blit(sprite_sheet, (0, 0), rect) 
            sprites.append(pygame.transform.scale2x(surface)) 

        if direction: 
            all_sprites[image.replace(".png", "") + "_right"] = sprites #these two functions strip the .png from the image name, and append it with right or left to constantly update the movement animation
            all_sprites[image.replace(".png", "") + "_left"] = flip_sprite(sprites) 
        else: 
            all_sprites[image.replace(".png", "")] = sprites 

    return all_sprites 
