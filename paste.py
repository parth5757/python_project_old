import keyboard
import pyperclip

# List to store the last 10 copied texts
copied_texts = []

def on_ctrl_c(event):
    # Callback function to be triggered on Ctrl + C
    copied_text = pyperclip.paste()
    if copied_text:
        copied_texts.append(copied_text)
        # Keep only the last 10 copied texts
        copied_texts = copied_texts[-10:]

# Register the Ctrl + C hotkey
keyboard.add_hotkey('ctrl+c', on_ctrl_c)

def show_copied_texts():
    # Function to display the last 10 copied texts
    for i, text in enumerate(copied_texts):
        print(f"{i + 1}. {text}")

# Register the Shift + L hotkey
keyboard.add_hotkey('shift+l', show_copied_texts)

# Start the keyboard listener
keyboard.wait()
