import tkinter as tk

class Gif():
    def __init__(self, gifPath, frames):
        self.gifPath = gifPath
        self.frames = frames
        self.gifArray = [tk.PhotoImage(file=gifPath, format='gif -index %i' %(i)) for i in range(frames)]
