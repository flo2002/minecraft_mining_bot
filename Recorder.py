import threading

class Recorder:
    def __init__(self):
        threading.Thread.__init__(self)
        
        
    def record(self):
        print("Recording...")