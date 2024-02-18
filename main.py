from modules.modules import * 
from globalvars.globalvars import *   

from screens.main_menu import *
from screens.levels import *  
from screens.run_level import *  
from screens.options import * 
from screens.characters import * 
from screens.video_settings import *

######################## MAIN ########################

def main(window):  
    
    current_screen = "Main"

    while True: 
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
        elif (current_screen == "Video"):
            current_screen = video() 

if __name__ == "__main__":
    main(WINDOW_DISPLAY)
