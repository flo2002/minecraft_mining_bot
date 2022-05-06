# imports all necessary packages
import numpy as np
import pyautogui
import keyboard
import time
import sys
import threading
import pandas as pd
import mss
import win32api

def record_screen(fps):
    # setting up a few parameters
    ms_per_frame = 1000 / fps
    i = 0
    region = {'top': 710, 'left': 290, 'width': 500, 'height': 500}

    while True:
        # stops if "h" is pressed
        if keyboard.is_pressed("h"):
            break
        
        # notes the start time
        start = int(round(time.time() * 1000))

        # records pixel and summarizes values
        value = np.array(mss.mss().grab(region)).sum()

        # saves the values in a list
        screen_events.append({'value': value})
        
        # updates the iterator
        i = i + 1

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)
        #print(str(i) + ' ' + str(ms_per_frame) + ' ' + str(start) + ' ' + str(now) + ' ' + str(now-start) + ' ' + str((ms_per_frame - abs(start - now)) / 1000))

def record_mouse():
    # setting up a few parameters
    ms_per_frame = 5
    i = 0

    while True:
        # stops if "h" is pressed
        if keyboard.is_pressed("h"):
            break
        
        # notes the start time
        start = int(round(time.time() * 1000))

        # gets mouse position
        mouse_events.append({'x': win32api.GetCursorPos()[0],
                             'y': win32api.GetCursorPos()[1],
                             'left': win32api.GetKeyState(0x01),
                             'right': win32api.GetKeyState(0x02)})
      
        # updates the iterator
        i = i + 1

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        #print(str(i) + ' ' + str(ms_per_frame) + ' ' + str(start) + ' ' + str(now) + ' ' + str(now-start) + ' ' + str((ms_per_frame - abs(start - now)) / 1000))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)


if __name__ == '__main__':
    print('Starting...')

    # setting up the frames per second and two lists for the mouse, keyboard and screen data
    FPS = 30
    mouse_events = []
    keyboard_events = []
    screen_events = []

    # records if "g" is pressed
    keyboard.wait("g")
    record_mouse_thread = threading.Thread(target = lambda: record_mouse())
    record_screen_thread = threading.Thread(target = lambda: record_screen(FPS))
    record_screen_thread.start()
    record_mouse_thread.start()
    keyboard.start_recording()

    # wait until "h" is pressed
    record_screen_thread.join()
    record_mouse_thread.join()
    keyboard_events = keyboard.stop_recording()
        
    # save record
    mouse_events = pd.DataFrame(mouse_events)
    keyboard_events = pd.DataFrame(keyboard_events)
    screen_events = pd.DataFrame(screen_events)
    mouse_events.to_csv('example1/mine_mouse_events.csv')
    keyboard_events.to_csv('example1/mine_keyboard_events.csv')
    screen_events.to_csv('example1/mine_screen_events.csv')

    # terminate the script if it has finished
    sys.exit()
        
