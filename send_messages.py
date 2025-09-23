from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def send_whatsapp_messages(phone_number, messages):
    phone_number = phone_number.replace('+', '').replace(' ', '')
    
    # Setup Brave browser options
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/brave-browser"  # Path to Brave browser
    
    # Initialize Brave browser
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        for i, message in enumerate(messages, 1):
            url = f'https://web.whatsapp.com/send?phone={phone_number}&text={message}'
            driver.get(url)
            
            chat_box = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]'))
            )
            
            time.sleep(2)  # Wait for chat box to be fully ready
            chat_box.click()
            chat_box.send_keys(Keys.ENTER)
            
            print(f"Message {i} sent successfully!")
            time.sleep(5)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        driver.quit()

# Example usage
phone_number = "+31625633319"  # Replace with actual number
messages = [
    "Hello! This is message 1",
    "How are you? This is message 2",
    "This is message 3",
    "Message number 4",
    "Final message 5"
]

send_whatsapp_messages(phone_number, messages)