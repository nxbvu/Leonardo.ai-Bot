import threading
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Prompt the user for input
prompt = input("Prompt: ")

# Set your download path here
download_path = r"YOUR_DOWNLOAD_PATH_HERE"  # Replace with your actual download path
lock = threading.Lock()
downloaded_images_count = 0

def find_password_input(driver):
    try:
        password_input = driver.find_element(By.CSS_SELECTOR, '[autocomplete="current-password"]')
        return password_input
    except Exception as e:
        print(f"Error finding password input: {e}")
        return None

def download_images(urls):
    global downloaded_images_count
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_extension = os.path.splitext(url.split("/")[-1].split("?")[0])[1]
                random_number = random.randint(1, 10000)
                filename = os.path.join(download_path, f"{url.split('/')[-1].split('?')[0]}_{random_number}{file_extension}")
                allowed_prefix = "Default"
                if not os.path.basename(filename).startswith(allowed_prefix):
                    print(f"Exception for filename: {filename}")
                    continue  
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print(f"Image downloaded: {filename}")

                downloaded_images_count += 1
            else:
                print(f"Error downloading image from URL: {url}")
        except requests.RequestException as e:
            print(f"Request exception while downloading image: {e}")
        except Exception as e:
            print(f"General exception while downloading image: {e}")

def run_code():
    global downloaded_images_count

    login_file_path = 'login.txt'
    with lock:
        with open(login_file_path, 'r') as login_file:
            lines = login_file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print("New User:", last_line)
                print("Password: hahalol12345!AHA")
            else:
                print("No login information found.")
                return
        with open(login_file_path, 'w') as login_file:
            login_file.writelines(lines[:-1])
    
    service_object = Service('./chromedriver.exe')
    prefs = {"download.default_directory": download_path}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=service_object, options=chrome_options)
    driver.get("https://app.leonardo.ai/auth/login")
    time.sleep(1)
    
    embox = driver.find_element(By.CSS_SELECTOR, '[autocomplete="username"]')
    embox.send_keys(last_line)
    time.sleep(0.2)
    
    password_input = find_password_input(driver)
    if password_input:
        print("Password input found!")
        password_input.send_keys("hahalol12345!AHA")
    else:
        print("Password input not found!")
        driver.quit()
        return

    sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].chakra-button.css-1qqz7y3')
    sign_in_button.click()

    time.sleep(3)
    driver.get("https://app.leonardo.ai/ai-generations")
    time.sleep(4)
    try:
        driver.execute_script("document.querySelector('.chakra-button.AlchemyTrialIntroModal--doneButton.css-cud252').click();")
    except Exception as e:
        print(f"Error clicking done button: {e}")
    time.sleep(1)

    textarea = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Type a prompt ..."]')
    textarea.send_keys(prompt)
    time.sleep(1)

    try:
        driver.execute_script("document.querySelector('.chakra-button.css-1kj5m7e').click();")
    except Exception as e:
        print(f"Error clicking generate button: {e}")

    time.sleep(35)
    images = driver.find_elements(By.CSS_SELECTOR, 'img.chakra-image')
    image_urls = [img.get_attribute("src") for img in images]  
    download_images(image_urls)
    
    time.sleep(50)
    driver.quit()

quit = 1
for alpha in range(quit):
    thread_count = 1
    threads = []

    for _ in range(thread_count):
        thread = threading.Thread(target=run_code)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
