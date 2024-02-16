from modules.modules import * 
from globalvars.globalvars import *   
from functions.window_display_functions import * 
from objects.game_objects import *   
from objects.player import *  

def level_one():   
    
    background, bg_image = get_background("Sky.png")  
    player = Player(100, 100, 50, 50)   
    fire = Fire(100, WINDOW_HEIGHT - BLOCK_SIZE - 64, 16, 32)
    fire.on()
    floor = [Block(i * BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE) for i in range(-WINDOW_WIDTH // BLOCK_SIZE, (WINDOW_WIDTH * 2) // BLOCK_SIZE)] 
    objects = [*floor, Block(0, WINDOW_HEIGHT - BLOCK_SIZE * 2, BLOCK_SIZE), fire]  

    return (background, bg_image, player, fire, objects)