import pyautogui
from pynput.mouse import Button, Controller as MouseController
import keyboard
import random
import time

#################################
########## Edit these! ##########
#################################

### Keybinds ###
PAUSE_KEY = 'f2'  # Pressing this key pauses the script (REQUIRED!!!)
RESUME_KEY = 'f3'  # Pressing this key while paused resumes the script (Recomended)
QUIT_KEY = 'f5'   # Pressing this key while paused quits the script (Recomended)
### Options ###
ENABLE_CLICK = True  # Allows the script to click M1 M2 and M3
ENABLE_MOUSE_MOVE = True  # Allows the script to move your mouse cursor
ENABLE_KEYS = True  # Allows the script to press keys on your keyboard
ALLOWED_KEYS = ['w', 'a', 's', 'd']  # Tells the script what keys are allowed. (Examples: ['A', '1', '/', 'f1', 'win') (Requires EnableKeys!!!)
### Misc ###
CHANCE = 2  # The higher the number the less likely. 1 is 100% 2 is 50% ETC... (REQUIRED!!!)
DELAY = 0.5  # Delay between actions (in seconds)
RANDOM_CLICK_BUTTON = True  # Randomly choose between M1, M2, and M3 (Will default to M1 if False)

#################################
######### Code, Ignore. #########
#################################


class ScriptController:
    def __init__(self):
        self.pause_script = False
        self.end_script = False
        self.mouse = MouseController()

        if not PAUSE_KEY:
            self.end_script
        if CHANCE <= 0:
            self.end_script

    def run(self):
        print("Starting in...")

        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)

        while not self.end_script:
            while not self.pause_script:
                if keyboard.is_pressed(PAUSE_KEY):
                    self.pause_script = True
                    print("Paused")

                if ENABLE_KEYS and random.randint(1, CHANCE) == 1:
                    key_to_press = random.choice(ALLOWED_KEYS)
                    pyautogui.press(key_to_press)

                if ENABLE_MOUSE_MOVE and random.randint(1, CHANCE) == 1:
                    move_x = random.randint(-50, 50)
                    move_y = random.randint(-50, 50)
                    if random.choice([True, False]):
                        move_x = -move_x
                    if random.choice([True, False]):
                        move_y = -move_y

                    pyautogui.moveTo(pyautogui.position()[0] + move_x, pyautogui.position()[1] + move_y)
                    
                if ENABLE_MOUSE_DRAG and random.randint(1, CHANCE) == 1:
                    move_x = random.randint(-50, 50)
                    move_y = random.randint(-50, 50)
                    if random.choice([True, False]):
                        move_x = -move_x
                    if random.choice([True, False]):
                        move_y = -move_y

                    pyautogui.dragTo(pyautogui.position()[0] + move_x, pyautogui.position()[1] + move_y)

                if ENABLE_CLICK and random.randint(1, CHANCE) == 1:
                    click_button = Button.left if not RANDOM_CLICK_BUTTON else random.choice([Button.left, Button.middle, Button.right])
                    self.mouse.click(click_button)

                time.sleep(DELAY) 

            while self.pause_script:
                if keyboard.is_pressed(RESUME_KEY):
                    print("Resumed")
                    self.pause_script = False

                if keyboard.is_pressed(QUIT_KEY):
                    print("Quiting")
                    time.sleep(1)
                    self.end_script = True
                    self.pause_script = False


if __name__ == "__main__":
    try:
        controller = ScriptController()
        controller.run()
    except Exception as e:
        print(f"An error occurred: {e}")