import tkinter as tk

class Gif():
    def __init__(self, root, gifPath, frames):
        self.root = root
        self.gifPath = gifPath
        self.frames = frames
        self.cycle = 0
        self.gifArray = [tk.PhotoImage(file=gifPath, format='gif -index %i' %(i)) for i in range(frames)]
        self.createLabels()
        self.currentFrame = self.gifArray[0]

    def createLabels(self):
        for i in self.gifArray:
            self.gifArray[i] = tk.Label(self.root, bd = 0, bg = 'systemTransparent', image = self.gifArray[i])

    def reset(self):
        self.cycle = 0
    
    def update(self):
        self.cycle += 1
        if (self.cycle >= self.frames):
            self.reset()
        self.currentFrame = self.gifArray[self.cycle]

    def getCurrentFrame(self):
        return self.currentFrame
