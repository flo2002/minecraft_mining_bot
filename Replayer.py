import threading

class Replayer:
    def __init__(self):
        threading.Thread.__init__(self)
        
        
    def replay(self):
        print("Replaying...")