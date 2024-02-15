from modules.modules import * 
from globalvars.globalvars import *    
from functions.collision import *  

def handle_move(player, objects): 
    keys = pygame.key.get_pressed()#this function allows us to see what's being pressed on the keyboard, VERY COOL!

    player.x_vel = 0 
    collide_left = collide(player, objects, -PLAYER_VELOCITY * 2) #horizontal collision is a bit3111333311113322
    collide_right = collide(player, objects, PLAYER_VELOCITY * 2)

    if keys[pygame.K_LEFT] and not collide_left: 
        player.move_left(PLAYER_VELOCITY) 
    if keys[pygame.K_RIGHT] and not collide_right: 
        player.move_right(PLAYER_VELOCITY) 

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel) 
    to_check = [collide_left, collide_right, *vertical_collide] 
    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()