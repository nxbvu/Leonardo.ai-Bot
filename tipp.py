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

def replace_characters(driver, stop_event):
    while not stop_event.is_set():
        try:
            driver.execute_async_script(replace_characters_script())
        except Exception as e:
            print(f"Error in replace_characters: {e}")
        time.sleep(1)  # Add a small delay to prevent excessive CPU usage

# WebDriver setup
chrome_options = webdriver.ChromeOptions()
service_object = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.get("https://www.tippenakademie.de/schreibtrainer/tipp-test")
time.sleep(5)  # Wait for the page to fully load

# Event to signal the thread to stop
stop_event = threading.Event()

# Start a separate thread for replacing characters
thread = threading.Thread(target=replace_characters, args=(driver, stop_event))
thread.start()

# Continue with the main thread
try:
    while True:
        # Your main thread logic goes here
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    # Signal the thread to stop and wait for it to finish
    stop_event.set()
    thread.join()
    driver.quit()
