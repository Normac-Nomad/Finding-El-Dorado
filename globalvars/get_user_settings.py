FILE_NAME = 'user_settings.txt' 

def get_user_settings(list_name): 

    with open(FILE_NAME, 'r') as user_file:
        read_user_file = user_file.readlines() 
        
        for line in read_user_file: 
            list_name.append(line.strip())  
    
    return (list_name)

def update_user_settings(line, content):
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        lines[line] = content + "\n"
    with open(FILE_NAME, "w") as file:
        file.write("".join(lines)) 



