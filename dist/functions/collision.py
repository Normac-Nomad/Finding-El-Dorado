from modules.modules import * 
from globalvars.globalvars import *   
from objects.player import * 

def handle_vertical_collision(player, objects, dy): 
    """
    Name: handle_vertical_collision
    Location: .../finding-el-dorado/functions/collision.py
    Purpose: Handles vertical collision between the player and objects
    Parameters:
        - player: Player object
        - objects: List of objects for collision detection
        - dy: Vertical displacement of the player
    Return: List of collided objects
    """
    collided_objects = []  

    for obj in objects: 
        if (pygame.sprite.collide_mask(player, obj)): 
            if (dy > 0): 
                player.rect.bottom = obj.rect.top
                player.landed() 

            if (dy < 0): 
                player.rect.top = obj.rect.bottom 
                player.hit_head() 

            collided_objects.append(obj)
    
    return (collided_objects) 

def collide(player, objects, dx): 
    """
    Name: collide
    Location: .../finding-el-dorado/functions/collision.py
    Purpose: Handles collision detection between the player and objects that isn't vertical collision
    Parameters:
        - player: Player object
        - objects: List of objects for collision detection
        - dx: Horizontal displacement of the player
    Return: Collided object (if any)
    """
    player.move(dx, 0) 
    player.update()  
    collided_objects = None 

    for obj in objects:  
        if (pygame.sprite.collide_mask(player, obj)): 
            collided_objects = obj 
            break 
    
    player.move(-dx, 0)
    player.update() 

    return (collided_objects) 
