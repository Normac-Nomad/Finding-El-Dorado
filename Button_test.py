import math 
import pygame 
import os 
from os import listdir 
from os.path import isfile, join
 

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000   
MENU_BUTTON_SCALE = (SCREEN_HEIGHT + SCREEN_WIDTH) / 1500 
MENU_BUTTON_DISTANCE = 75 * MENU_BUTTON_SCALE
MENU_BUTTON_X_OFFSET = -100 * MENU_BUTTON_SCALE #image width divided by two 
MENU_BUTTON_Y_OFFSET = -50 * MENU_BUTTON_SCALE#image height divided by two
CENTER_MENU_BUTTON_X = (SCREEN_WIDTH / 2) + MENU_BUTTON_X_OFFSET 
CENTER_MENU_BUTTON_Y = (SCREEN_HEIGHT / 2) + MENU_BUTTON_Y_OFFSET 


WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Button Demo') 

start_img = pygame.image.load("assets/start.png").convert_alpha()  
hover_start_img = pygame.image.load("assets/start_hover.png").convert_alpha() 
exit_img = pygame.image.load("assets/exit.png").convert_alpha()  
hover_exit_img = pygame.image.load("assets/exit_hover.png").convert_alpha() 

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
        pos = pygame.mouse.get_pos() 
        if (self.image_rect.collidepoint(pos)): 
            WINDOW.blit(self.hover, (self.hover_rect.x, self.hover_rect.y)) 
            if ((pygame.mouse.get_pressed()[0] == 1) and (self.clicked == False)): 
                self.clicked = True
        else: 
            WINDOW.blit(self.image, (self.image_rect.x, self.image_rect.y))  

        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False

start_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE, start_img, hover_start_img, MENU_BUTTON_SCALE) 
exit_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + MENU_BUTTON_DISTANCE, exit_img, hover_exit_img, MENU_BUTTON_SCALE)

while True:  
     
    WINDOW.fill((255, 220, 0)) 

    start_button.draw()
    exit_button.draw()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.QUIT  
            quit()

    pygame.display.update() 

pygame.quit() 
quit()