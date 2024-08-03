def read_and_update_login_file():
    login_file_path = 'tr.txt'
    last_line = None
    try:
        # Read the file and get the last line
        with open(login_file_path, 'r') as login_file:
            lines = login_file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print("New User: ", last_line)
                print("Password: hahalol12345!AHA")
            else:
                print("The file tr.txt is empty.")
        
        # Write back all lines except the last one
        with open(login_file_path, 'w') as login_file:
            login_file.writelines(lines[:-1])
    except FileNotFoundError:
        print(f"The file {login_file_path} does not exist.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
    
    return last_line

if __name__ == "__main__":
    read_and_update_login_file()
