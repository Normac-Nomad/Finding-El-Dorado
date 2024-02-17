from modules.modules import * 
from globalvars.globalvars import * 
 

WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('Button Demo') 

class Button(): 
    def __init__(self, x, y, image, hover, scale): 
        width = image.get_width() 
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width* scale), int(height * scale))) 
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (x, y) 
        self.clicked = False

        hover_width = hover.get_width() 
        hover_height = hover.get_height()
        self.hover = pygame.transform.scale(hover, (int(hover_width* scale), int(hover_height * scale))) 
        self.hover_rect = self.hover.get_rect()
        self.hover_rect.topleft = (x, y)
        
    def draw(self):  
        action = False 
        pos = pygame.mouse.get_pos() 
        if (self.image_rect.collidepoint(pos)): 
            WINDOW_DISPLAY.blit(self.hover, (self.hover_rect.x, self.hover_rect.y)) 
            if ((pygame.mouse.get_pressed()[0] == 1) and (self.clicked == False)): 
                self.clicked = True 
                action = True
        else: 
            WINDOW_DISPLAY.blit(self.image, (self.image_rect.x, self.image_rect.y))  

        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False 
        
        return action
