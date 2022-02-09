import tkinter as tk

class Gif():
    def __init__(self, gifPath, frames):
        self.gifPath = gifPath
        self.frames = frames
        self.cycle = 0
        self.gifArray = [tk.PhotoImage(file=gifPath, format='gif -index %i' %(i)) for i in range(frames)]
        self.currentFrame = self.gifArray[0]

    def reset(self):
        self.cycle = 0
    
    def update(self):
        self.cycle += 1
        if (self.cycle >= self.frames):
            self.reset()
        self.currentFrame = self.gifArray[self.cycle]

    def getCurrentFrame(self):
        return self.currentFrame
