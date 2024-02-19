from modules.modules import * 
from globalvars.globalvars import *   

from screens.main_menu import *
from screens.levels import *  
from screens.run_level import *  
from screens.options import * 
from screens.characters import * 

######################## MAIN ########################

def main(window):  
    
    current_screen = "Main"

    while True: 
        #main menu
        if (current_screen == "Main"):
            current_screen = main_menu()
        elif (current_screen == "Game"):
            current_screen = play_game()   
        elif (current_screen == "Levels"):
            current_screen = levels() 
        elif (current_screen == "Characters"):
            current_screen = characters() 
        elif (current_screen == "Options"): 
            current_screen = options()    
        #level selection
        elif (current_screen == "Level1"):  
            current_screen = play_game_level(1) 
        elif (current_screen == "Level2"):  
            current_screen = play_game_level(2)

if __name__ == "__main__":
    main(WINDOW_DISPLAY)
