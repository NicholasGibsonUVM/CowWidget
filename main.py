from animations.Animation import Cow
import platform
import tkinter as tk

def update(cow):
    cow.update()
    cow.after(100, update, cow)

def main():
    cow = Cow()
    pathPrefix = ""
    if (platform.system() == "Windows"):
        pathPrefix = "Gifs\\"
    else:
        pathPrefix = "Gifs/"
    cow.addGif(pathPrefix + "Left-Cow-Transparent.gif", 19, -3, 0)
    cow.addGif(pathPrefix + "Right-Cow-Transparent.gif", 19, 3, 0)
    cow.after(100, update, cow)
    tk.mainloop()

main()