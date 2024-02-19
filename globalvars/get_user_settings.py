user_file = open('user_settings.txt', 'r') 

read_user_file = user_file.readlines()

user_settings = []

for line in read_user_file: 
    user_settings.append(line.strip())
 
USER_FPS = int(user_settings[0][5:]) 
USER_WIDTH = int(user_settings[1][7:])
USER_HEIGHT = int(user_settings[2][8:])
USER_CHARACTER = user_settings[3][11:] 
USER_LEVEL = int(user_settings[4][7:])
