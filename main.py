import pyautogui
import keyboard  # To detect keypresses
import time  # Optional: for delay control

try:
    while True:
        # Scroll down (negative value) and up (positive value)
        pyautogui.scroll(-100)  # Scroll down by 50 pixels
        pyautogui.scroll(70)  # Scroll up by 50 pixels

        # You can add a small delay to make the scrolling more noticeable
        time.sleep(0.2)

        # Check if any key has been pressed
        if keyboard.is_pressed('esc'):  # Use 'esc' or any other key you prefer
            print("ESC key pressed, breaking the loop.")
            break

except KeyboardInterrupt:
    print("Program interrupted by the user.")
