import tkinter as tk
import platform
from matplotlib import animation
import pyautogui  
import random
import time
from .gifs.Gifs import Gif

###
#   TODO:
#   Add Clickable Function   
#   Add Message Function   
#  
###

class Cow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.system = platform.system() 
        self.label = tk.Label(self, bd=0)
        self.maxWidth , self.maxHeight = pyautogui.size()
        self.xPos = (int) (self.maxWidth / 2)
        self.yPos = (int) (200)
        self.event = 0
        self.changeEvent = 0
        self.maxOff = 20
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

    def addGif(self, gifPath, frames, xChange, yChange, eventLength = 80, canReplay = True, speed = 100):
        gifArray = dict()
        gifArray["gif"] = Gif(gifPath, frames)
        gifArray["xChange"] = xChange
        gifArray["yChange"] = yChange
        gifArray["eventLength"] = eventLength
        gifArray["canReplay"] = canReplay
        gifArray["animationSpeed"] = speed
        self.gifs.append(gifArray)

    def getAnimationSpeed(self):
        return self.gifs[self.event]["animationSpeed"]

    def setEvent(self):
        #Get New Event and Reset gif if neccesary
        newEvent = self.event
        if (self.changeEvent > self.gifs[self.event]["eventLength"]):
            self.changeEvent = 0
            #Generate new event and make sure that it's different if gif can't replay
            newEvent = random.randrange(0, len(self.gifs))
            while(not(self.gifs[self.event]["canReplay"]) and newEvent == self.event):
                newEvent = random.randrange(0, len(self.gifs))
            if (newEvent != self.event):
                self.gifs[self.event]["gif"].reset()
                self.event = newEvent
        self.changeEvent += 1

    def setLabel(self):
        self.gifs[self.event]["gif"].update()
        self.label.config(image=(self.gifs[self.event]["gif"].getCurrentFrame()))

    def moveWindow(self):
        #Update location
        self.xPos += self.gifs[self.event]["xChange"]
        self.yPos += self.gifs[self.event]["yChange"]
        #Check bounds
        if (self.xPos >= (self.maxWidth + self.maxOff)):
            self.xPos = (int) (-160 + self.maxOff)
        elif (self.xPos <= -160-self.maxOff):
            self.xPos = (int) (self.maxWidth - self.maxOff)
        if (self.yPos >= (self.maxHeight + self.maxOff)):
            self.yPos = (int) (-160 + self.maxOff)
        elif (self.yPos <= -160-self.maxOff):
            self.yPos = (int) (self.maxHeight - self.maxOff)
        #change Position
        super().geometry('160x160+'+str(self.xPos)+'+'+str(self.yPos))

    def updateWindow(self):
        self.label.pack_forget()
        self.label.pack()

    def update(self):
        self.setEvent()
        self.moveWindow()
        self.setLabel()
        self.updateWindow()

