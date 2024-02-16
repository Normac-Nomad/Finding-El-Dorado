from modules.modules import * 
from globalvars.globalvars import *   

from functions.sprite_functions import *  
from functions.window_display_functions import *   
from functions.collision import *  
from functions.player_movement import *   
from functions.run_level import *

from objects.game_objects import * 
from objects.player import *   

from screens.levels import *

######################## MAIN ########################

def main(window):  
    
    play_game(window)

if __name__ == "__main__":
    main(WINDOW_DISPLAY)