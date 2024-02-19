FILE_NAME = 'user_settings.txt' 
USER_SETTINGS_RAW_LIST = []

def get_user_settings():
    user_file = open(FILE_NAME, 'r') 
    read_user_file = user_file.readlines() 

    for line in read_user_file: 
        USER_SETTINGS_RAW_LIST.append(line.strip()) 
    user_file.close()  

def update_user_settings(line:int, content:str):
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        lines[line] = content + "\n"
    with open(FILE_NAME, "w") as file:
        file.write("".join(lines)) 



