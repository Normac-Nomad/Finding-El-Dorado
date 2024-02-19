from modules.modules import * 
from globalvars.globalvars import *  

def flip_sprite(sprites):  
    """  
    Name: flip_sprites
    Location: .../finding-el-dorado/functions/sprite_functions 
    Purpose: Flips sprites
    Parameters:
        - sprites: List of sprites to be flipped
    Return: Flipped sprite
    """ 
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]  

def load_sprite_sheets(dir1, dir2, width, height, direction=False):  
    """  
    Name: load_sprite_sheets
    Location: .../finding-el-dorado/functions/sprite_functions 
    Purpose: Loads sprites sheets with passed directories and dimensions
    Parameters:
        - dir1: First part of the directory path
        - dir2: Second part of the directory path
        - width: Width of individual sprite frames
        - height: Height of individual sprite frames
        - direction: Boolean indicating whether to create left and right sprites for movement animation
    Return: Returns the sprites sheets frame by frame in a list
    """ 
    path = join("assets", dir1, dir2) 
    images = [f for f in listdir(path) if isfile(join(path, f))]
            
    all_sprites = {} 

    for image in images: 
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = [] 
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32) 
            rect = pygame.Rect(i * width, 0, width, height) 
            surface.blit(sprite_sheet, (0, 0), rect) 
            sprites.append(pygame.transform.scale2x(surface)) 

        if (direction): 
            all_sprites[image.replace(".png", "") + "_right"] = sprites  
            all_sprites[image.replace(".png", "") + "_left"] = flip_sprite(sprites) 
        else: 
            all_sprites[image.replace(".png", "")] = sprites 

    return (all_sprites)

