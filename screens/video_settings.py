from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *
from screens.levels import *

from objects.game_objects import * 
from objects.button import *  

def video():  

    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)), 
                         MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5) 

    while True:
     
        WINDOW_DISPLAY.fill((255, 220, 0))

        if (ingame_menu_button.draw()):
            return("Main")

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program()  

        pygame.display.update()  