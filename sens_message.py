from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import urllib.parse

def send_whatsapp_messages(phone_number, messages):
    phone_number = phone_number.replace('+', '').replace(' ', '')
    
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/brave-browser"
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # First open WhatsApp Web and wait for scan
        driver.get("https://web.whatsapp.com")
        print("Please scan QR code and press Enter after WhatsApp is loaded...")
        input()
        
        for i, message in enumerate(messages, 1):
            # Encode message for URL
            encoded_message = urllib.parse.quote(message)
            url = f'https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}'
            driver.get(url)
            
            # Wait for chat box
            chat_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]'))
            )
            
            # Wait for page to be fully loaded
            time.sleep(5)
            
            # Send message
            chat_box.send_keys(Keys.ENTER)
            
            # Wait for message to be sent
            time.sleep(3)
            
            print(f"Message {i} sent successfully!")
            
            # Additional wait between messages
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