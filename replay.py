# imports all necessary packages
import numpy as np
import pyautogui
import keyboard
import time
import sys
import threading
import pandas as pd
import mss
import win32gui, win32api, win32con, ctypes

def replay_screen(fps):
    # setting up a few parameters
    ms_per_frame = 1000 / fps
    i = 0
    region = {'top': 710, 'left': 290, 'width': 500, 'height': 500}

    for index, row in screen_events.iterrows():
        # stops if "h" is pressed
        if keyboard.is_pressed("h"):
            break
        
        # notes the start time
        start = int(round(time.time() * 1000))

        # records pixel and summarizes values
        value = np.array(mss.mss().grab(region)).sum()

        recorded_value = row['value']
        check_value = 100000

        # checks if an anomaly is detected
        if value > recorded_value + check_value or value < recorded_value - check_value:
            print("error")

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        #print(now-start)
        #print(str(i) + ' ' + str(value) + ' ' + str(recorded_value))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)


def replay_mouse(fps):
    # setting up a few parameters
    ms_per_frame = 100
    i = 0
    
    for index, row in mouse_events.iterrows():
        # stops if "h" is pressed
        if keyboard.is_pressed("h"):
            break

        # notes the start time
        start = int(round(time.time() * 1000))

        # replay the mouse events
        ctypes.windll.user32.SetCursorPos(int(row['x']), int(row['y']))
        if row['left'] == 0 or row['left'] == 1:
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
            print('test1')
        else:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
            print('test2')

        if row['right'] == 0 or row['right'] == 1:
            ctypes.windll.user32.mouse_event(10, 0, 0, 0, 0)
            print('test3')
        else:
            ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0)
            print('test4')

        print('test5')
        # updates the iterator
        i = i + 1

        # waits that the fps is frequently
        now = int(round(time.time() * 1000))
        print(str(i) + ' ' + str(now - start))
        time.sleep((ms_per_frame - abs(start - now)) / 1000)


if __name__ == '__main__':
    print('Starting...')

    #while True:
    # setting up the frames per second and two lists for the mouse, keyboard and screen data
    FPS = 30
    mouse_events = pd.read_csv('example1/mine_mouse_events.csv')
    screen_events = pd.read_csv('example1/mine_screen_events.csv')
    keyboard_events = pd.read_csv('example1/mine_keyboard_events.csv').values.tolist()

    # replays the record if "g" is pressed
    keyboard.wait("g")
    keyboard_thread = threading.Thread(target = lambda: keyboard.replay(keyboard_events))
    replay_mouse_thread = threading.Thread(target = lambda: replay_mouse(FPS))
    replay_screen_thread = threading.Thread(target = lambda: replay_screen(FPS))
    keyboard_thread.start()
    replay_screen_thread.start()
    replay_mouse_thread.start()

    # terminate script if it has finished
    keyboard_thread.join()
    replay_screen_thread.join()
    replay_mouse_thread.join()
    sys.exit()
        
