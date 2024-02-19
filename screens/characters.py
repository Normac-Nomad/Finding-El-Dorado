from modules.modules import * 
from globalvars.globalvars import * 
   
from functions.window_display_functions import *
from screens.levels import *

from objects.game_objects import * 
from objects.button import *  

def characters():  

    ingame_menu_button = Button((WINDOW_WIDTH - (WINDOW_WIDTH - 5)), (WINDOW_HEIGHT - (WINDOW_HEIGHT - 5)), 
                         MAIN_MENU_IMAGE, HOVER_MAIN_MENU_IMAGE, MENU_BUTTON_SCALE / 1.5) 
    mask_dude = Button(CENTER_MENU_BUTTON_X - (MENU_BUTTON_DISTANCE * 9), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 10), MASK_BUTTON, MASK_JUMP_BUTTON, MENU_BUTTON_SCALE * 5)
    ninja_frog = Button(CENTER_MENU_BUTTON_X - (MENU_BUTTON_DISTANCE * 3), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 10), FROG_BUTTON, FROG_JUMP_BUTTON, MENU_BUTTON_SCALE * 5) 
    pink_man = Button(CENTER_MENU_BUTTON_X - (MENU_BUTTON_DISTANCE * -3), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 10), PINK_BUTTON, PINK_JUMP_BUTTON, MENU_BUTTON_SCALE * 5) 
    virtual_guy = Button(CENTER_MENU_BUTTON_X - (MENU_BUTTON_DISTANCE * -9), CENTER_MENU_BUTTON_Y - (MENU_BUTTON_DISTANCE * 10), VIRTUAL_BUTTON, VIRTUAL_JUMP_BUTTON, MENU_BUTTON_SCALE * 5) 
    
    while True:  
     
        WINDOW_DISPLAY.fill((255, 220, 0))

        if (mask_dude.draw()):  
            update_user_settings(3, "CHARACTER: MaskDude")
            return("Game") 
        elif (ninja_frog.draw()):  
            update_user_settings(3, "CHARACTER: NinjaFrog")
            return("Game") 
        elif (pink_man.draw()):  
            update_user_settings(3, "CHARACTER: PinkMan")
            return("Game") 
        elif (virtual_guy.draw()):  
            update_user_settings(3, "CHARACTER: VirtualGuy")
            return("Game")

        if (ingame_menu_button.draw()):
            return("Main")

        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                quit_program() 

        pygame.display.update()