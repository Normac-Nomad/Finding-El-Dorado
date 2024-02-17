from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *
from screens.levels import *

from objects.game_objects import * 
from objects.button import * 

def main_menu(window):  
    """  
    Name: main_menu
    Location: .../finding-el-dorado/functions/window_display_functions
    Purpose: Runs the main menu screen for the user
    Return: Depending which button the user clicks, it will return the name of desired screen
    """     
    start_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE, START_IMAGE, HOVER_START_IMAGE, MENU_BUTTON_SCALE) 
    exit_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + MENU_BUTTON_DISTANCE, EXIT_IMAGE, HOVER_EXIT_IMAGE, MENU_BUTTON_SCALE)

    while True:  
     
        WINDOW_DISPLAY.fill((255, 220, 0))

        if (start_button.draw()): 
            return ("Game")
        if (exit_button.draw()):
            quit_program()

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program()

        pygame.display.update()  
