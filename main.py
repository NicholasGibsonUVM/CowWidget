from animations.Animation import Cow
import platform
import tkinter as tk

###
#   TODO
#   Add Feed Mechanic
#   Make a cow class that can be animated by Animation so that you can make more complex behaviors happen
#   Add a way for the cow to drag messages across the screen
#   Add a click function the speed the cow up for a period of time
###

def update(cow):
    cow.update()
    cow.after(cow.getAnimationSpeed(), update, cow)

def main():
    cow = Cow()
    pathPrefix = ""
    if (platform.system() == "Windows"):
        pathPrefix = "Gifs\\"
    else:
        pathPrefix = "Gifs/"
    cow.addGif(pathPrefix + "Left-Cow-Transparent.gif", 4, -3, 0)
    cow.addGif(pathPrefix + "Right-Cow-Transparent.gif", 4, 3, 0)
    cow.addGif(pathPrefix + "Down-Cow-Transparent.gif", 4, 0, 3)
    cow.addGif(pathPrefix + "Up-Cow-Transparent.gif", 4, 0, -3)
    cow.addGif(pathPrefix + "Eat-Cow-Transparent.gif", 14, 0, 0, eventLength=14, canReplay=False, speed=500)
    cow.after(100, update, cow)
    tk.mainloop()

main()