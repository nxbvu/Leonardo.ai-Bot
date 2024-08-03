import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urljoin
import random
import string
import logging

# Configuration
CRX_FILE_PATH = "./adb.crx"
CHROME_DRIVER_PATH = './chromedriver.exe'
THREAD_COUNT = 7
QUIT_COUNT = 30
PASSWORD = "hahalol12345!AHA"

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_extension(CRX_FILE_PATH)

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def click_einwilligen(driver):
    try:
        einwilligen_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button" and @role="button" and @aria-label="Einwilligen" and @tabindex="0"]'))
        )
        einwilligen_button.click()
    except Exception as e:
        logging.error(f"Error clicking Einwilligen button: {e}")

def run_code():
    driver = None
    try:
        service_object = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service_object, options=chrome_options)
        
        # Create temporary email
        driver.get("https://www.mohmal.com/de/create/random")
        time.sleep(10)
        driver.get("https://www.mohmal.com/de/create/random")
        email = driver.find_element(By.XPATH, '//div[@class="email"]').get_attribute("data-email")
        
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        
        # Sign up on Leonardo.ai
        driver.get("https://app.leonardo.ai/auth/login")
        time.sleep(0.5)
        signup = driver.find_element(By.XPATH, '//a[contains(text(), "Sign up")]')
        driver.execute_script("arguments[0].scrollIntoView(true);", signup)
        signup.click()
        time.sleep(1)
        driver.find_element(By.ID, 'email').send_keys(email)
        time.sleep(0.5)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        driver.find_element(By.XPATH, '//button[@class="chakra-button css-1qqz7y3" and contains(text(), "Sign up")]').click()
        
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

        # Click Einwilligen button
        click_einwilligen(driver)
        
        # Refresh email for verification code
        for _ in range(3):
            driver.find_element(By.CLASS_NAME, 'svg-inline--fa.fa-arrows-rotate').click()
            time.sleep(1)
        
        driver.find_element(By.XPATH, '//a[contains(text(), "Your verification code")]').click()
        time.sleep(2)
        
        # Retrieve confirmation code from iframe
        iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        full_url = urljoin("https://www.mohmal.com", iframe_element.get_attribute('src'))
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-4])
        driver.get(full_url)
        
        body_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).text
        confirmation_code = body_text[body_text.find("Your confirmation code is") + len("Your confirmation code is"):].strip() if "Your confirmation code is" in body_text else None
        
        if confirmation_code:
            driver.switch_to.window(driver.window_handles[2])
            time.sleep(0.2)
            driver.find_element(By.ID, "confirmation_code").send_keys(confirmation_code)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//button[@class="chakra-button css-1qqz7y3" and contains(text(), "Confirm account")]').click()
            time.sleep(5)
            
            # Generate username
            input_element = driver.find_element(By.XPATH, '//input[@placeholder="myawesomeusername" and @class="chakra-input css-13s0zy"]')
            random_string = generate_random_string(10)
            input_element.send_keys(random_string)
            time.sleep(1)

            # Complete account setup
            driver.find_element(By.XPATH, "//button[@class='chakra-button css-za8h6a' and text()='advertising']").click()
            time.sleep(1)
            driver.find_element(By.ID, "start-using-leonardo").click()
            time.sleep(2)
            driver.execute_script("document.querySelector('.chakra-checkbox__input').click();")
            time.sleep(1)
            driver.execute_script("document.querySelector('.chakra-button.css-89t8e5').click();")
            time.sleep(1)

            # Save account details
            logging.info("Passwort: hahalol12345!AHA")
            with open("login.txt", "a") as login_file:
                login_file.write(email + "\n")
            with open("tr.txt", "a") as login_file:
                login_file.write(email + "\n")
            time.sleep(6)
    except Exception as e:
        logging.error(f"Error in run_code: {e}")
    finally:
        if driver:
            driver.quit()

def main():
    for _ in range(QUIT_COUNT):
        threads = []

        # Create and start threads
        for _ in range(THREAD_COUNT):
            thread = threading.Thread(target=run_code)
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
