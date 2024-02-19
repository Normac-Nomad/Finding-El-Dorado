from modules.modules import * 
from globalvars.globalvars import *  

class GameImage(): 
    """  
    Name: GameImage
    Location: .../finding-el-dorado/objects/game_image.py 
    Purpose: Represents an image in the game
    Return: N/a
    """
    def __init__(self, image, x, y, scale):
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/game_image.py 
        Purpose: Initializes a GameImage instance
        Parameters:
            - image: Image to be displayed
            - x: X-coordinate of the image
            - y: Y-coordinate of the image
            - scale: Scaling factor for the image
        Return: N/a
        """
        width = image.get_width() 
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (x, y)    

    def draw(self): 
        """
        Name: draw
        Location: .../finding-el-dorado/objects/game_image.py 
        Purpose: Draws the image on the game window
        Return: N/a
        """
        WINDOW_DISPLAY.blit(self.image, (self.image_rect.x, self.image_rect.y)) 
