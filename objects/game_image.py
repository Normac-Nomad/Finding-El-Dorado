from modules.modules import * 
from globalvars.globalvars import *  

class GameImage(): 

    def __init__(self, image, x, y, scale):
        width = image.get_width() 
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width* scale), int(height * scale))) 
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (x, y)    

    def draw(self): 
        WINDOW_DISPLAY.blit(self.image, (self.image_rect.x, self.image_rect.y)) 