import os

def read_and_update_login_file():
    login_file_path = 'tr.txt'
    last_line = None
    backup_file_path = 'tr_backup.txt'
    
    try:
        # Check if file exists
        if not os.path.exists(login_file_path):
            print(f"The file {login_file_path} does not exist.")
            return
        
        # Create a backup of the original file
        with open(login_file_path, 'r') as login_file:
            lines = login_file.readlines()
        
        with open(backup_file_path, 'w') as backup_file:
            backup_file.writelines(lines)
        
        # Read the file and get the last line
        if lines:
            last_line = lines[-1].strip()
            print("New User:", last_line)
        else:
            print("The file tr.txt is empty.")
            return

        # Write back all lines except the last one
        with open(login_file_path, 'w') as login_file:
            login_file.writelines(lines[:-1])

    except IOError as e:
        print(f"An IOError occurred: {e}")
        # Restore from backup in case of an error
        if os.path.exists(backup_file_path):
            with open(backup_file_path, 'r') as backup_file:
                lines = backup_file.readlines()
            with open(login_file_path, 'w') as login_file:
                login_file.writelines(lines)
            print("Restored the original file from backup.")

    return last_line

if __name__ == "__main__":
    read_and_update_login_file()