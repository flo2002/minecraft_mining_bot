import keyboard
import mouse

class Recorder:
    def __init__(self):
        self.mouse_events = []
        self.keyboard_events = []
        
    def record(self):
        self.keyboard_events = []
        self.mouse_events = []
            
        keyboard.wait("g")
        print("Recording...")
        keyboard.start_recording()
        mouse.hook(self.mouse_events.append)
        
        keyboard.wait("h")
        self.keyboard_events = keyboard.stop_recording()
        mouse.unhook(self.mouse_events.append)
        print("stopped")
            
        print(self.keyboard_events)
        