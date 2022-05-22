from tkinter import Tk, Label, Button, StringVar
import Replayer, Recorder

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple Minecraft Mining Bot")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set("Choose an option: ")
        self.label = Label(master, textvariable=self.label_text)
        self.label.pack()

        self.record_button = Button(master, text="Record", command=self.record)
        self.record_button.pack()

        self.replay_button = Button(master, text="Replay", command=self.replay)
        self.replay_button.pack()

    def record(self):
        Recorder.record()

    def replay(self):
        Replayer.replay()

root = Tk()
my_gui = GUI(root)
root.mainloop()