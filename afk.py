from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyController, Listener
import random
import time
from pyfiglet import Figlet
import sys
import os

mouse = MouseController()

keyboard = KeyController()

format = Figlet(font='Big')

GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
RESET = "\033[0m"

creator = "Created By - BackwoodsCart🍃"

mouse_command_list = ["180", "360", "90Left", "90Right"]

key_command_list = ["Sprint", "SlideR", "SlideL", "Crouch", "LayDown", "Back", "Inspect", "Jump", "Slide", "SlideBack"]

mouse_click_list = ["Shoot", "Aim", "Both"]

paused = False

def on_press(key):
    global paused
    try:
        if key == Key.f7: # Change this key for Pause Hotkey
            paused = True
            print("Paused")
        elif key == Key.f8: # Change this key for Resume Hotkey
            paused = False
            print("Resumed")
    except Exception as e:
        print(f"Error: {e}")


def main():
    global paused

    header()
    time.sleep(3)
    input("\n\nPress Enter to continue...")
    clear_console()

    mouse.position = (960, 540)
    time.sleep(3)

    while True:
        if paused:
            time.sleep(0.1)
            continue

        # select loadout
        mouse.position = (192, 123)
        mouse.press(Button.left)
        mouse.release(Button.left)

        # skip killcam
        keyboard.press("e")
        keyboard.release("e")

        # +++Not Functional+++ : smc = get_mouse_commands(mouse_command_list)
        
        skd = get_key_commands(key_command_list)
        # +++Not Functional+++ : do_mouse_command(smc)
        do_key_command(skd)
        shoot(mouse_click_list)
        print("---------------------------------\n")
        time.sleep(1.5)
        keyboard.press("e")
        keyboard.release("e")
        continue


def header():
    print(format.renderText("  AFK   Bot"))
    print(creator.center(43))

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_mouse_commands(mouse_command_list):
    random_mouse_movement = random.choice(mouse_command_list)
    return random_mouse_movement

def get_key_commands(key_command_list):
    random_key_movement = random.choice(key_command_list)
    return random_key_movement

# +++Not Functional+++: def do_mouse_command(smc):
    if smc == "180":
        return mouse.move(50, -50)
    elif smc == "360":
        return mouse.move(100, -100)
    elif smc == "90Left":
        return mouse.move(-25, 25)
    elif smc == "90Right":
        return mouse.move(25, -25)
    else:
        pass

def do_key_command(skd):
    if skd == "Sprint":
        print("Sprint")
        with keyboard.pressed(Key.shift):
            keyboard.press("w")
            time.sleep(3)
            keyboard.release("w")
    elif skd == "SlideR":
        print("Slide Right")
        with keyboard.pressed(Key.shift):
            keyboard.press("d")
            time.sleep(1)
            keyboard.press("q")
            time.sleep(.5)
            keyboard.release("d")
            keyboard.release("q")
    elif skd == "Slide":
        print("Sprint and Slide")
        with keyboard.pressed(Key.shift):
            keyboard.press("w")
            time.sleep(1)
            keyboard.press("q")
            time.sleep(.5)
            keyboard.release("w")
            keyboard.release("q")
    elif skd == "SlideL":
        print("Slide Left")
        with keyboard.pressed(Key.shift):
            keyboard.press("a")
            time.sleep(1)
            keyboard.press("q")
            time.sleep(.5)
            keyboard.release("a")
            keyboard.release("q")
    elif skd == "SlideBack":
        print("Slide Back")
        with keyboard.pressed(Key.shift):
            keyboard.press("s")
            time.sleep(1)
            keyboard.press("q")
            time.sleep(.5)
            keyboard.release("s")
            keyboard.release("q")
    elif skd == "Crouch":
        print("Crouch")
        keyboard.press("q")
        keyboard.release("q")
    elif skd == "LayDown":
        print("Lay Down")
        keyboard.press(Key.ctrl)
        time.sleep(.5)
        keyboard.release(Key.ctrl)
    elif skd == "Back":
        print("Sprint Backwards")
        with keyboard.pressed(Key.shift):
            keyboard.press("s")
            time.sleep(1)
            keyboard.release("s")
    elif skd == "Inspect":
        print("Inspect")
        keyboard.press("f")
        keyboard.release("f")
        time.sleep(5)
    elif skd == ("Jump"):
        print("Run and Jump")
        with keyboard.pressed(Key.shift):
            keyboard.press("w")
            time.sleep(1)
            keyboard.press(Key.space)
            time.sleep(.5)
            keyboard.release("w")
            keyboard.release(Key.space)
    else:
        pass


def shoot(mouse_click_list):
    YesNo = random.choices([True, False], weights=[.7, .3])[0]
    if YesNo:
        shoot = random.choice(mouse_click_list)
        if shoot == "Shoot":
            print("Shoot")
            mouse.press(Button.left)
            time.sleep(2)
            mouse.release(Button.left)
        elif shoot == "Aim":
            print("Aim")
            mouse.press(Button.right)
            time.sleep(2)
            mouse.release(Button.right)
        elif shoot == "Both":
            print("Aim and Shoot")
            mouse.press(Button.right)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(2)
            mouse.release(Button.left)
            mouse.release(Button.right)
    else:
        print("Dont Aim or Shoot")
        



if __name__ == "__main__":
    
    listener = Listener(on_press=on_press)
    listener.start()
    
    main()
