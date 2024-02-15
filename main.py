from modules.modules import * 
from globalvars.globalvars import *  
from functions.sprite_functions import * 
from objects.game_objects import *

pygame.init() 
pygame.display.set_caption(WINDOW_CAPTION) 
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #creates the game interface

class Player(pygame.sprite.Sprite): #slightly related: a sprite is a 2D image part of a larger image
    COLOR = (255, 0, 0) 
    GRAVITY = 1 
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True) #final argument is for multidirectional sprites
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x,y, width, height) # !!!! don't understand this, later !!!! 
        self.x_vel = 0
        self.y_vel = 0 
        self.mask = None 
        self.direction = "left" 
        self.animation_count = 0   
        self.fall_count = 0 
        self.jump_count = 0  
        self.hit = False 
        self.hit_count = 0

    def jump(self): 
        self.y_vel = -self.GRAVITY * 8 
        self.animation_count = 0 
        self.jump_count +=1
        if self.jump_count == 1: #as soon as we jump
            self.fall_count = 0 #we reset the fall count to get rid of the accumulated gravity
            #change the fall count value, and boost the double jump, I don't like this mechanic

    def move(self, dx, dy): #d = displacement arguments 
        self.rect.x += dx 
        self.rect.y += dy  

    def make_hit(self): 
        self.hit = True 
        self.hit_count = 0

    def move_left(self, vel): 
        self.x_vel = -vel 
        if self.direction != "left":
            self.direction = "left" 
            self.animation_count = 0  
            
    def move_right(self, vel): 
        self.x_vel = vel 
        if self.direction != "right":
            self.direction = "right" 
            self.animation_count = 0   

    def loop(self, fps):  
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY) #gravity for our sprite
        self.move(self.x_vel, self.y_vel)  

        if self.hit: 
            self.hit_count += 1 
        if self.hit_count > fps *2: 
            self.hit = False 
            self.hit_count = 0

        self.fall_count += 1  
        self.update_sprite()
    
    def landed(self): 
        self.fall_count = 0 
        self.y_vel = 0 
        self.jump_count = 0 

    def hit_head(self): 
        self.count = 0 
        self.y_vel *= -1

    def update_sprite(self): 
        sprite_sheet = "idle"  
        if self.hit:
            sprite_sheet = "hit"
        if self.y_vel < 0: 
            if self.jump_count == 1: 
                sprite_sheet = "jump" 
            elif self.jump_count == 2: 
                sprite_sheet = "double_jump" 
        elif self.y_vel > self.GRAVITY * 2: #ensures that we have a sufficient amount of velocity before showing the fall animation
            sprite_sheet = "fall"        
        elif self.x_vel != 0: 
            sprite_sheet = "run" 

        sprite_sheet_name = sprite_sheet + "_" + self.direction 
        sprites = self.SPRITES[sprite_sheet_name] 
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites) #dynamically looping through the different images in the sprite sheet
        self.sprite = sprites[sprite_index] 
        self.animation_count += 1 
        self.update()

    def update(self): 
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y)) 
        self.mask = pygame.mask.from_surface(self.sprite) #This line ensures we have pixel perfect collison, we are extracting only the pixels to the mask, that way we are no including the empty pixels in the sprite sheet

    def draw(self, win, offset_x): 
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y)) #draws the player sprite onto the window

def get_background(name): #Name is the asset name; function returns a background containing a list (which is the background)
    
    image = pygame.image.load(join("assets", "Background", name)) 
    _, _, width, height = image.get_rect() # the two underscores would usually contain the X and Y coordinates of the image. We don't need those at the moment
    tiles = [] 

    for i in range(WINDOW_WIDTH // width + 1): #// is integer divide. Cool innit? 
        for j in range(WINDOW_HEIGHT // height + 1):#these two snippets of code give us an idea of how many of the background asset we need to create the whole background. The +1 is to ensure that there are no gaps in the background
            pos = (i * width, j * height) #this gives us the location of the top right corner of the background asset we are currently printing on to the background.
            tiles.append(pos) #appending the current background asset to our list 

    return tiles, image 

def draw_window(WINDOW_DISPLAY, background, bg_image, player, objects, offset_x): 

    for tile in background: 
        WINDOW_DISPLAY.blit(bg_image, tile) #actually drawing our background with the blit function using the tuple from get_background

    for obj in objects: 
        obj.draw(WINDOW_DISPLAY, offset_x)

    player.draw(WINDOW_DISPLAY, offset_x)

    pygame.display.update() 

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

def handle_move(player, objects): 
    keys = pygame.key.get_pressed()#this function allows us to see what's being pressed on the keyboard, VERY COOL!

    player.x_vel = 0 
    collide_left = collide(player, objects, -PLAYER_VEL * 2) #horizontal collision is a bit3111333311113322
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left: 
        player.move_left(PLAYER_VEL) 
    if keys[pygame.K_RIGHT] and not collide_right: 
        player.move_right(PLAYER_VEL) 

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel) 
    to_check = [collide_left, collide_right, *vertical_collide] 
    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()


######################## MAIN ########################

def main(window): 
    clock = pygame.time.Clock() 
    background, bg_image = get_background("Blue.png") #get_background returns the list and image

    block_size = 96

    player = Player(100, 100, 50, 50)   
    fire = Fire(100, WINDOW_HEIGHT - block_size - 64, 16, 32)
    fire.on()
    floor = [Block(i * block_size, WINDOW_HEIGHT - block_size, block_size) for i in range(-WINDOW_WIDTH // block_size, (WINDOW_WIDTH * 2) // block_size)] #turn this into multiple functions, way to complicated for one line in the video @1:08:39
    objects = [*floor, Block(0, WINDOW_HEIGHT - block_size * 2, block_size), Block(block_size * 3, WINDOW_HEIGHT - block_size * 4, block_size), fire] #"*thing" breaks everything into it's individual elements and passes them into the objects list; we're just creating the different blocks ontop of the floor

    offset_x = 0 
    scroll_area_width = 200 #when the player gets to "scroll_area_width" (200 pixels) the screen will begin scrolling

    run = True 

    while run: 
        clock.tick(FPS)#ensures that the while loop runs FPS=60, regulates frame rate 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #if the user hits the X button (quits the game)
                run = False #game is no longer running
                break    

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and player.jump_count < 2: 
                    player.jump()

        player.loop(FPS) 
        fire.loop()
        handle_move(player, objects)
        draw_window(window,background, bg_image, player, objects, offset_x) 

        if (((player.rect.right - offset_x >= WINDOW_WIDTH - scroll_area_width) and player.x_vel > 0) or ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0)): #checking the pixel length from the screen; clean this up into a function
            offset_x += player.x_vel

    pygame.quit() 
    quit()

#the line below executes only when main is run directly prevents it from running indirectly if something is imported from main.py's event loop
if __name__ == "__main__": 
    main(WINDOW_DISPLAY)