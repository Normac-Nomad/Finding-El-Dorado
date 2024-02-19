from modules.modules import * 
from globalvars.globalvars import *  
from functions.sprite_functions import *  
from functions.window_display_functions import * 

class Player(pygame.sprite.Sprite): 
    """  
    Name: Player
    Location: .../finding-el-dorado/objects/player 
    Purpose: Playable character used by the user
    Return: N/a
    """   
    player_animation_delay = 3
    player_gravity = GRAVITY

    def __init__(self, x, y, width, height):
        """
        Name: __init__
        Location: .../finding-el-dorado/objects/player 
        Purpose: Initializes a Player instance
        Parameters:
            - x: X-coordinate of the player
            - y: Y-coordinate of the player
            - width: Width of the player
            - height: Height of the player
        Return: N/a
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0 
        self.mask = None 
        self.direction = "left" 
        self.animation_count = 0   
        self.fall_count = 0 
        self.jump_count = 0  
        self.hit = False 
        self.hit_count = 0  
        
        user_settings = []   
        user_settings = get_user_settings(user_settings)
        self.player_sprite = load_sprite_sheets("MainCharacters", user_settings[3][11:], 32, 32, True)

    def update(self): 
        """
        Name: update
        Location: .../finding-el-dorado/objects/player 
        Purpose: Updates the player's position and mask
        Return: N/a
        """
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y)) 
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x, offset_y): 
        """
        Name: draw
        Location: .../finding-el-dorado/objects/player 
        Purpose: Draws the player on the game window
        Parameters:
            - win: Game window surface
            - offset_x: X offset
            - offset_y: Y offset
        Return: N/a
        """
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))

    def move(self, dx, dy):
        """
        Name: move
        Location: .../finding-el-dorado/objects/player 
        Purpose: Moves the player by the specified amount
        Parameters:
            - dx: Change in x-coordinate
            - dy: Change in y-coordinate
        Return: N/a
        """
        self.rect.x += dx 
        self.rect.y += dy  

    def move_left(self, vel): 
        """
        Name: move_left
        Location: .../finding-el-dorado/objects/player 
        Purpose: Moves the player to the left with the specified velocity
        Parameters:
            - vel: Velocity of the player
        Return: N/a
        """
        self.x_vel = -vel 
        if self.direction != "left":
            self.direction = "left" 
            self.animation_count = 0  
            
    def move_right(self, vel): 
        """
        Name: move_right
        Location: .../finding-el-dorado/objects/player 
        Purpose: Moves the player to the right with the specified velocity
        Parameters:
            - vel: Velocity of the player
        Return: N/a
        """
        self.x_vel = vel 
        if self.direction != "right":
            self.direction = "right" 
            self.animation_count = 0   

    def jump(self):  
        """
        Name: jump
        Location: .../finding-el-dorado/objects/player 
        Purpose: Initiates a jump for the player
        Return: N/a
        """
        self.y_vel = -self.player_gravity * 8 
        self.animation_count = 0 
        self.jump_count += 1
        if self.jump_count == 1: 
            self.fall_count = 0  

    def landed(self): 
        """
        Name: landed
        Location: .../finding-el-dorado/objects/player 
        Purpose: Handles the player landing after a jump
        Return: N/a
        """
        self.fall_count = 0 
        self.y_vel = 0 
        self.jump_count = 0 

    def hit_head(self): 
        """
        Name: hit_head
        Location: .../finding-el-dorado/objects/player 
        Purpose: Handles the player hitting their head on an obstacle
        Return: N/a
        """
        self.count = 0 
        self.y_vel *= -1

    def make_hit(self): 
        """
        Name: make_hit
        Location: .../finding-el-dorado/objects/player 
        Purpose: Marks the player as hit
        Return: N/a
        """
        self.hit = True 
        self.hit_count = 0

    def loop(self, fps):  
        """
        Name: loop
        Location: .../finding-el-dorado/objects/player 
        Purpose: Handles the player's movement and animation
        Parameters:
            - fps: Frames per second
        Return: N/a
        """
        self.y_vel += min(1, (self.fall_count / fps) * self.player_gravity) 
        self.move(self.x_vel, self.y_vel)  

        if self.hit: 
            self.hit_count += 1 
        if self.hit_count > fps * 2: 
            self.hit = False 
            self.hit_count = 0

        self.fall_count += 1  
        self.update_sprite()
    
    def update_sprite(self): 
        """
        Name: update_sprite
        Location: .../finding-el-dorado/objects/player 
        Purpose: Updates the player's sprite based on their actions
        Return: N/a
        """
        sprite_sheet = "idle"  
        if self.hit:
            sprite_sheet = "hit" 
        elif self.y_vel < 0: 
            if self.jump_count == 1: 
                sprite_sheet = "jump" 
            elif self.jump_count == 2: 
                sprite_sheet = "double_jump" 
        elif self.y_vel > self.player_gravity * 2: 
            sprite_sheet = "fall"        
        elif self.x_vel != 0: 
            sprite_sheet = "run" 

        sprite_sheet_name = sprite_sheet + "_" + self.direction 
        sprites = self.player_sprite[sprite_sheet_name] 
        sprite_index = (self.animation_count // self.player_animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index] 
        self.animation_count += 1  
        self.update()
