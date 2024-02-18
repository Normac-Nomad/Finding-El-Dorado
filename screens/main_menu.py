from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *
from screens.levels import *

from objects.game_objects import * 
from objects.button import *  
from objects.game_image import * 

def main_menu():  
    """  
    Name: main_menu
    Location: .../finding-el-dorado/functions/window_display_functions
    Purpose: Runs the main menu screen for the user
    Return: Depending which button the user clicks, it will return the name of desired screen
    """     
    start_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - MENU_BUTTON_DISTANCE, START_IMAGE, HOVER_START_IMAGE, MENU_BUTTON_SCALE) 
    levels_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + MENU_BUTTON_DISTANCE, LEVELS_IMAGE, HOVER_LEVELS_IMAGE, MENU_BUTTON_SCALE)
    characters_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + (MENU_BUTTON_DISTANCE * 3), CHARACTERS_IMAGE, HOVER_CHARACTERS_IMAGE, MENU_BUTTON_SCALE)
    video_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + (MENU_BUTTON_DISTANCE * 5), VIDEO_IMAGE, HOVER_VIDEO_IMAGE, MENU_BUTTON_SCALE)
    options_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + (MENU_BUTTON_DISTANCE * 7), OPTIONS_IMAGE, HOVER_OPTIONS_IMAGE, MENU_BUTTON_SCALE)
    exit_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + (MENU_BUTTON_DISTANCE * 9), EXIT_IMAGE, HOVER_EXIT_IMAGE, MENU_BUTTON_SCALE)
    
    title_image = GameImage(TITLE_IMAGE, CENTER_MENU_BUTTON_X - MENU_BUTTON_X_OFFSET + 
                            (-600 * 0.8 * MENU_BUTTON_SCALE), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 9), MENU_BUTTON_SCALE * 0.8)

    while True:  
     
        WINDOW_DISPLAY.fill((255, 220, 0)) 
        title_image.draw()

        if (start_button.draw()): 
            return ("Game") 
        if (levels_button.draw()): 
            return("Levels") 
        if (characters_button.draw()): 
            return("Characters")
        if (video_button.draw()): 
            return("Video")
        if (options_button.draw()): 
            return("Options") 
        if (exit_button.draw()):
            quit_program()

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program()

        pygame.display.update()  
