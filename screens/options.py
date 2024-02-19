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
    exit_button = Button(CENTER_MENU_BUTTON_X, CENTER_MENU_BUTTON_Y + (MENU_BUTTON_DISTANCE * 7), EXIT_IMAGE, HOVER_EXIT_IMAGE, MENU_BUTTON_SCALE)
    restart_image = GameImage(RESTART_IMAGE, CENTER_MENU_BUTTON_X - MENU_BUTTON_X_OFFSET + (-220 * 0.8 * MENU_BUTTON_SCALE), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 10), MENU_BUTTON_SCALE * 0.8)


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
            restart_image.draw() 

            if (exit_button.draw()): 
                quit_program()

        if (ingame_menu_button.draw()):
            return("Main")

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program()  

        pygame.display.update()  