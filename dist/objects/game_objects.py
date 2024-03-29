from modules.modules import * 
from globalvars.globalvars import *  
from functions.sprite_functions import *

class Game_Object(pygame.sprite.Sprite):
    """  
    Name: Game_Object 
    Location: .../finding-el-dorado/objects/game_objects 
    Purpose: Non-instantiated base class for most objects in the game 
    Return: N/a
    """
    def __init__(self, x, y, width, height, name = None): 
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Initializes a Game_Object instance
        Parameters:
            - x: X-coordinate of the object
            - y: Y-coordinate of the object
            - width: Width of the object
            - height: Height of the object
            - name: Optional name for the object
        Return: N/a
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height) 
        self.image = pygame.Surface((width, height), pygame.SRCALPHA) 
        self.width = width
        self.heigth = height 
        self.name = name 

    def draw(self, display, offset_x, offset_y):  
        """  
        Name: draw
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Affixes objects onto the game window
        Parameters:
            - display: Display surface
            - offset_x: X offset
            - offset_y: Y offset
        Return: N/a
        """
        display.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))   

class Block(Game_Object):  
    """  
    Name: Block 
    Location: .../finding-el-dorado/objects/game_objects 
    Purpose: Block class for terrain blocks
    Return: N/a
    """
    def __init__(self, x, y, size): 
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Initializes a Block instance
        Parameters:
            - x: X-coordinate of the block
            - y: Y-coordinate of the block
            - size: Size of the block
        Return: N/a
        """
        super().__init__(x, y, size, size) 
        block = get_block(size) 
        self.image.blit(block, (0,0)) 
        self.mask = pygame.mask.from_surface(self.image)   

def get_block(size): # size will be the dimension of the image for the block 
    """  
    Name: get_block 
    Location: .../finding-el-dorado/objects/game_objects 
    Purpose: Retrieves the terrain sprites
    Parameters:
        - size: Dimension of the block image
    Return: The game's terrain scaled up by 2x 
    """
    path = join("assets", "Terrain", "Terrain.png") 
    image = pygame.image.load(path). convert_alpha() 
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32) 
    rect = pygame.Rect(96, 0, size, size) 
    surface.blit(image, (0, 0), rect) 

    return pygame.transform.scale2x(surface)  

class Fire(Game_Object):   
    """  
    Name: Fire
    Location: .../finding-el-dorado/objects/game_objects 
    Purpose: Fire class for fire objects in the game
    Return: N/a
    """
    fire_animation_delay = 3

    def __init__(self, x, y, width, height):
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Initializes a Fire instance
        Parameters:
            - x: X-coordinate of the fire
            - y: Y-coordinate of the fire
            - width: Width of the fire
            - height: Height of the fire
        Return: N/a
        """
        super().__init__(x, y, width, height, "fire") 
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)   
        self.image = self.fire["off"][0] 
        self.mask = pygame.mask.from_surface(self.image) 
        self.animation_count = 0 
        self.animation_name = "off" 

    def on(self): 
        """  
        Name: on
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Changes the fire sprite animation to on
        Return: N/a
        """
        self.animation_name = "on" 

    def off(self):  
        """  
        Name: off
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Changes the fire sprite animation to off
        Return: N/a
        """ 
        self.animation_name = "off" 

    def loop(self):
        """  
        Name: loop
        Location: .../finding-el-dorado/objects/game_objects 
        Purpose: Handles the fire sprite animation and contains the fire mask for pixel perfect collision
        Return: N/a
        """
        sprites = self.fire[self.animation_name]  
        sprite_index = (self.animation_count // self.fire_animation_delay) % len(sprites) #dynamically looping through the different images in the sprite sheet
        self.image = sprites[sprite_index] 
        self.animation_count += 1 

        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y)) 
        self.mask = pygame.mask.from_surface(self.image) #This line ensures we have pixel perfect collison, we are extracting only the pixels to the mask, that way we are no including the empty pixels in the sprite sheet

        if ((self.animation_count // self.fire_animation_delay) > len(sprites)): 
            self.animation_count = 0
