from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import threading

def replace_characters_script():
    return '''
        var spans = document.querySelectorAll('.sign');
        spans.forEach(function(span) {
            var charactersToReplace = 'abcdefghijklmnopqrstuvwxyzäöüß ';
            if (
                charactersToReplace.includes(span.innerText.toLowerCase()) || span.innerText === '\u00A0'
            ) {
                span.innerText = 'w';
                span.classList = ['sign', 'w', 'hit'];
            }
        });
        arguments[0]();
    '''

def replace_characters():
    while True:
        driver.execute_async_script(replace_characters_script())

# WebDriver-Setup
chrome_options = webdriver.ChromeOptions()
service_object = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.get("https://www.tippenakademie.de/schreibtrainer/tipp-test")
time.sleep(5)  # Wait for the page to fully load

# Start a separate thread for replacing characters
thread = threading.Thread(target=replace_characters)
thread.start()

# Continue with the main thread
try:
    while True:
        # Your main thread logic goes here
        time.sleep(1)
finally:
    # Make sure to quit the driver when the program is interrupted
    driver.quit()
