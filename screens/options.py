from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *
from screens.levels import *

from objects.game_objects import * 
from objects.button import *  

def options():

    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)), 
                         MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5) 
    r1280 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 4), R1280_IMAGE, HOVER_R1280_IMAGE, MENU_BUTTON_SCALE) 
    r1024 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 2), R1024_IMAGE, HOVER_R1024_IMAGE, MENU_BUTTON_SCALE)
    r800 = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y, R800_IMAGE, HOVER_R800_IMAGE, MENU_BUTTON_SCALE)
    change_setting = False

    while True:  
     
        WINDOW_DISPLAY.fill((255, 220, 0))

        if (r1280.draw()): 
            update_user_settings(1, "WIDTH: 1280") 
            update_user_settings(2, "HEIGHT: 1024")  
            change_setting = True
        if (r1024.draw()): 
            update_user_settings(1, "WIDTH: 1024") 
            update_user_settings(2, "HEIGHT: 768") 
            change_setting = True
        if (r800.draw()): 
            update_user_settings(1, "WIDTH: 800") 
            update_user_settings(2, "HEIGHT: 600") 
            change_setting = True 
        if (change_setting): 
            print("STUFF")

        if (ingame_menu_button.draw()):
            return("Main")

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program()  

        pygame.display.update()  