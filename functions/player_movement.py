from modules.modules import * 
from globalvars.globalvars import *    
from functions.collision import *  

def handle_move(player, objects): 
    """
    Name: handle_move
    Location: .../finding-el-dorado/functions/player_movement.py
    Purpose: Handles player movement based on keyboard input and collision detection
    Parameters:
        - player: Player object
        - objects: List of objects for collision detection 
    Return: N/a
    """
    keys = pygame.key.get_pressed()  # This function allows us to see what's being pressed on the keyboard, VERY COOL!

    player.x_vel = 0 
    collide_left = collide(player, objects, -PLAYER_VELOCITY * 2) 
    collide_right = collide(player, objects, PLAYER_VELOCITY * 2)

    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]): 
        current_velocity = PLAYER_VELOCITY + PLAYER_SPRINT_SPEED 
        player.player_animation_delay = 2
    else: 
        current_velocity = PLAYER_VELOCITY 
        player.player_animation_delay = 3

    if ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and not collide_left): 
        player.move_left(current_velocity) 

    if ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right): 
        player.move_right(current_velocity)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel) 
    to_check = [collide_left, collide_right, *vertical_collide] 
    
    for obj in to_check:
        if (obj and obj.name == "fire"):
            player.make_hit() 
