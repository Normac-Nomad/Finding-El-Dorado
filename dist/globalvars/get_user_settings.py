FILE_NAME = 'user_settings.txt' 

def get_user_settings(list_name):
    """
    Name: get_user_settings
    Location: .../finding-el-dorado/functions/get_user_settings.py
    Purpose: Retrieves user settings from the specified file and appends them to a provided list
    Parameters:
        - list_name: List to which user settings will be appended
    Return: Appended list containing user settings
    """
    with open(FILE_NAME, 'r') as user_file:
        read_user_file = user_file.readlines() 
        
        for line in read_user_file: 
            list_name.append(line.strip())  
    
    return (list_name)

def update_user_settings(line, content):
    """
    Name: update_user_settings
    Location: .../finding-el-dorado/functions/get_user_settings.py 
    Purpose: Updates a specific line in the user settings file with the provided content
    Parameters:
        - line: Line number to be updated
        - content: New content to be written to the specified line
    Return: N/a
    """
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        lines[line] = content + "\n"
    with open(FILE_NAME, "w") as file:
        file.write("".join(lines))
