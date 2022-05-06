# imports all necessary packages
import numpy as np
import pyautogui
import keyboard
import mouse
import time
import sys
import threading
import pandas as pd

def record_screen(fps):
    # setting up a few parameters
    ms_per_frame = 1000 / fps
    i = 0

    while True:
        # stops if "h" is pressed
        if keyboard.is_pressed("h"):
            break
        
        # notes the start time
        start = int(round(time.time() * 1000))

        # records pixel and summarizes values
        img = pyautogui.screenshot(region=(710, 290, 500, 500))
        img = np.array(img)
        value = np.array(img).sum()

        # saves the values in a list
        screen_events.append({'value': value})

        # updates the iterator
        i = i + 1

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)
        print(str(i) + ' ' + str(ms_per_frame) + ' ' + str(start) + ' ' + str(now) + ' ' + str(now-start) + ' ' + str((ms_per_frame - abs(start - now)) / 1000))


def check_errors(fps):
    # setting up a few parameters
    ms_per_frame = 1000 / fps
    i = 0
    recorded_screen_events = pd.DataFrame(screen_events)

    for i in range(len(recorded_screen_events)):
        # notes the start time
        start = int(round(time.time() * 1000))

        # records pixel and summarizes values
        img = pyautogui.screenshot(region=(710, 290, 500, 500))
        img = np.array(img)
        value = np.array(img).sum()

        recorded_value = recorded_screen_events['value'][i]
        check_value = 800000

        # checks if an anomaly is detected
        if value > recorded_value + check_value or value < recorded_value - check_value:
            print("error")

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)
        print(str(i) + ' ' + str(value) + ' ' + str(recorded_value))

        # updates the iterator
        i = i + 1



if __name__ == '__main__':
    print('Starting...')

    while True:
        # setting up the frames per second and two lists for the mouse, keyboard and screen data
        FPS = 16
        mouse_events = []
        keyboard_events = []
        screen_events = []

        # records if "g" is pressed
        keyboard.wait("g")
        mouse.hook(mouse_events.append)
        keyboard.start_recording()
        record_screen(FPS)

        # stops if "h" is pressed
        mouse.unhook(mouse_events.append)
        keyboard_events = keyboard.stop_recording()
        print("stopped")

        # replays the record if "j" is pressed
        keyboard.wait("j")
        mouse_thread = threading.Thread(target = lambda: mouse.play(mouse_events))
        keyboard_thread = threading.Thread(target = lambda: keyboard.replay(keyboard_events))
        record_screen_thread = threading.Thread(target = lambda: check_errors(FPS))
        mouse_thread.start()
        keyboard_thread.start()
        record_screen_thread.start()

        # terminate script if it has finished
        mouse_thread.join() 
        keyboard_thread.join()
        record_screen_thread.join()
        #sys.exit()
        
