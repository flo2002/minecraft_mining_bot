import keyboard
import mouse

class Replayer:
    def __init__(self, keyboard_events, mouse_events):
        self.keyboard_events = keyboard_events
        self.mouse_events = mouse_events

    def update(self, keyboard_events, mouse_events, status_label_text):
        if (keyboard_events == []) or (mouse_events == []):
            status_label_text.set("No recorded events. Please record first.")
        self.keyboard_events = keyboard_events
        self.mouse_events = mouse_events
    
    def replay(self):
        while True:
            if (self.keyboard_events == []) or (self.mouse_events == []):
                return
            
            keyboard.wait("g")
            print("Replaying...")
            
            
            keyboard.wait("h")
            print("stopped")
        