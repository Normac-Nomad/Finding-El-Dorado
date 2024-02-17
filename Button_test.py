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
exit_img = pygame.image.load("assets/exit.png").convert_alpha() 

class Button(): 
    def __init__(self, x, y, image, scale): 
        width = image.get_width() 
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width* scale), int(height * scale))) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) 

    def draw(self):  
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos): 
            #self.image = 
            print("HOVER")

        WINDOW.blit(self.image, (self.rect.x, self.rect.y))  

start_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE, start_img, MENU_BUTTON_SCALE) 
exit_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + MENU_BUTTON_DISTANCE, exit_img, MENU_BUTTON_SCALE)

while True:  
     
    WINDOW.fill((202, 228, 241)) 

    start_button.draw()
    exit_button.draw()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.QUIT  
            quit()

    pygame.display.update() 

pygame.quit() 
quit()