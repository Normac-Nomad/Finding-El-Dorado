from modules.modules import * 
from globalvars.globalvars import *   
from objects.player import * 

def handle_vertical_collision(player, objects, dy): 
    collided_objects = [] 
    for obj in objects: 
        if pygame.sprite.collide_mask(player, obj): #if the player is colliding with an object
            if dy > 0: #if we are moving down on the screen
                player.rect.bottom = obj.rect.top #the players feet will be on the top of the object; it's advantageous to use rectangle because it makes calculations for collision easier (will be harder with mask)
                player.landed()
            if dy < 0: 
                player.rect.top = obj.rect.bottom 
                player.hit_head() 

            collided_objects.append(obj)
    
    return collided_objects 

def collide(player, objects, dx): #comment up @1:33:32
    player.move(dx, 0)
    player.update()  
    collided_objects = None
    for obj in objects: 
        if pygame.sprite.collide_mask(player, obj): 
            collided_objects = obj 
            break 
    
    player.move(-dx, 0)
    player.update()
    return collided_objects