from modules.modules import * 
from globalvars.globalvars import * 

class Button(): 
    """  
    Name: Button
    Location: .../finding-el-dorado/objects/button.py
    Purpose: Represents a clickable button in the game
    Return: N/a
    """
    def __init__(self, x, y, image, hover, scale): 
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/button.py
        Purpose: Initializes a Button instance
        Parameters:
            - x: X-coordinate of the button
            - y: Y-coordinate of the button
            - image: Default image for the button
            - hover: Image for the button when hovered
            - scale: Scaling factor for the button images
        Return: N/a
        """
        width = image.get_width() 
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (x, y) 

        hover_width = hover.get_width() 
        hover_height = hover.get_height()
        self.hover = pygame.transform.scale(hover, (int(hover_width * scale), int(hover_height * scale))) 
        self.hover_rect = self.hover.get_rect()
        self.hover_rect.topleft = (x, y) 

        self.clicked = False
        
    def draw(self):  
        """
        Name: draw
        Location: .../finding-el-dorado/objects/button.py
        Purpose: Draws the button on the game window and handles button clicks
        Return: True if the button is clicked, False otherwise
        """
        action = False 
        pos = pygame.mouse.get_pos()  

        if self.image_rect.collidepoint(pos): 
            WINDOW_DISPLAY.blit(self.hover, (self.hover_rect.x, self.hover_rect.y)) 
            
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked: 
                self.clicked = True 
                action = True
        else: 
            WINDOW_DISPLAY.blit(self.image, (self.image_rect.x, self.image_rect.y))  

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 
        
        return action
