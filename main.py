# from Replayer file import Replayer class
import threading
from Replayer import Replayer
from Recorder import Recorder

from tkinter import Tk, Label, Button, StringVar, Frame

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple Minecraft mining bot")

        self.label_text = StringVar()
        self.label_text.set("Choose an option: ")
        self.label = Label(master, textvariable=self.label_text)
        self.label.pack()

        self.button_frame = Frame(master)
        self.button_frame.pack()
        
        self.record_button = Button(master, text="Record", command=self.record)
        self.record_button.pack(in_=self.button_frame, side="left")
        self.replay_button = Button(master, text="Replay", command=self.replay)
        self.replay_button.pack(in_=self.button_frame, side="right")
        
        self.status_label_text = StringVar()
        self.status_label = Label(master, textvariable=self.status_label_text)
        self.status_label.pack()

    def record(self):
        self.status_label_text.set("Start the recording with \"g\" and stop it with \"h\"")
        self.recorder = Recorder()
        self.recorder.record()
        

    def replay(self):
        self.status_label_text.set("Start the replaying with \"g\" and stop it with \"h\"")
        self.replayer = Replayer(self.recorder)
        self.replayer.replay()

root = Tk()
root.geometry("400x100")
my_gui = GUI(root)
root.mainloop()