def main():
    login_file_path = 'tr.txt'
    last_line = None
    with open(login_file_path, 'r') as login_file:
        lines = login_file.readlines()
        if lines:
            last_line = lines[-1].strip()
            print("New User: ", last_line)
            print("Password: hahalol12345!AHA")
        else:
            print("Die Datei tr.txt ist leer.")
    
    with open(login_file_path, 'w') as login_file:
        login_file.writelines(lines[:-1])
    
    return last_line

if __name__ == "__main__":
    main()
