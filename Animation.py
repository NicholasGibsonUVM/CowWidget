import tkinter as tk
import platform
import pyautogui  
import random
from .Gifs import Gif

class Cow(tk.Tk):
    def __init__(self):
        super().__init__(self)
        self.system = platform.system() 
        self.label = tk.Label(super(), bd=0)
        self.maxWidth , self.maxHeight = pyautogui.size()
        self.xPos = self.maxWidth / 2
        self.yPos = self.maxHeight - 200
        self.event = 0
        self.changeEvent = 0
        self.gifs = []
        if (self.system == "Windows"):
            super().config(highlightbackground='yellow')
            super().overrideredirect(True)
            super().wm_attributes("-topmost", True)
            super().wm_attributes('-transparentcolor', 'yellow')
            self.label.config(bg="yellow")
        else:
            super().overrideredirect(1)
            super().overrideredirect(0)
            super().wm_attributes("-topmost", True)
            super().wm_attributes("-transparent", True)
            self.label.config(bg='systemTransparent')
        self.label.pack()

    def addGif(self, gifPath, frames, xChange, yChange):
        gifArray = dict()
        gifArray["gif"] = Gif(gifPath, frames)
        gifArray["xChange"] = xChange
        gifArray["yChange"] = yChange
        self.gifs.append(gifArray)

    def update(self):
        if (self.changeEvent >= 20):
            self.changeEvent = 0
            self.event = random.randrange(0, len(self.gifs))
        self.changeEvent += 1
        
        super().after(100, self.update())

