# WhatsApp Message Sender

This project contains Python scripts to automate sending WhatsApp messages using Selenium and the Brave browser.

## Features

- Automates sending multiple messages to a specific phone number.
- Uses Selenium WebDriver for browser automation.
- Designed to work with the Brave browser.
- Handles message encoding and waits for elements to load.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Brave Browser](https://brave.com/)
- [Selenium](https://pypi.org/project/selenium/)

## Installation

1.  Clone this repository or download the files.
2.  Install the required Python packages:

    ```bash
    pip install selenium
    ```

3.  Ensure the Brave browser is installed at `/usr/bin/brave-browser`. If your installation path is different, you will need to update the `binary_location` in the scripts.

## Configuration

Open `sens_message.py` (or `send_messages.py`) and modify the following variables at the bottom of the file:

```python
phone_number = "+31625633319"  # Replace with the target phone number
messages = [
    "Hello! This is message 1",
    "How are you? This is message 2",
    # Add more messages as needed
]
```

## Usage

1.  Run the script:

    ```bash
    python sens_message.py
    ```

2.  A Brave browser window will open and navigate to WhatsApp Web.
3.  **Scan the QR code** with your phone to log in.
4.  Press **Enter** in the terminal console after WhatsApp Web has fully loaded.
5.  The script will proceed to send the configured messages one by one.

## Files

-   `sens_message.py`: The main script with better error handling and a pause for QR code scanning.
-   `send_messages.py`: A simpler version of the script.

## Disclaimer

This tool is for educational and personal automation purposes. Please use it responsibly and avoid spamming. WhatsApp may ban accounts that engage in automated or bulk messaging behavior.
