import keyboard
import mouse
import multiprocessing as mp

class Replayer:
    def __init__(self, keyboard_events, mouse_events):
        self.keyboard_events = keyboard_events
        self.mouse_events = mouse_events
        self.isReplaying = False

    def update(self, keyboard_events, mouse_events, status_label_text):
        if (keyboard_events == []) or (mouse_events == []):
            status_label_text.set("No recorded events. Please record first.")
        self.keyboard_events = keyboard_events
        self.mouse_events = mouse_events
    
    def replay(self):
        keyboard.wait("g")
        
        process_loop_breaker_listener = mp.Process(target=self.loop_breaker_listener)
        self.isReplaying = True
        process_loop_breaker_listener.start()
        process_replaying_loop = mp.Process(target=self.replaying_loop)
        process_replaying_loop.start()
        
        while True:
            if not self.isReplaying:
                process_loop_breaker_listener.terminate()   # SIGTERM
                #loop_breaker_listener.close()      # for the garbage collector
                process_replaying_loop.terminate()
                #replaying_loop.close()
                break
                print("stopped")

    def replaying_loop(self):
        print("replaying_loop started")
        while True:
            print("Replaying...")
            if (self.keyboard_events == []) or (self.mouse_events == []):
                return
            mouse_thread = mp.Process(target = lambda: mouse.play(self.mouse_events))
            keyboard_thread = mp.Process(target = lambda: keyboard.replay(self.keyboard_events))
            mouse_thread.start()
            keyboard_thread.start()
            mouse_thread.join() 
            keyboard_thread.join()

    def loop_breaker_listener(self):
        print("loop_breaker started")
        while True:
            if keyboard.is_pressed("h"):
                self.isReplaying = False
                break