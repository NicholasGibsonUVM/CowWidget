import random
import tkinter as tk
from PIL import Image, ImageTk
import platform
import pyautogui  

cycle = 0
check = 1
left =[1,2,3,4]
right = [5,6,7,8]
up = [9,10,11,12]
down = [13,14,15,16]
width, height= pyautogui.size()
x = (int) (width / 2)
y = (int) (height - 160 - 50)
event_number = random.randrange(1,3,1)
impath = 'Gifs\\'
window = tk.Tk()

def loadGif(animation, framesTotal, image):
    for x in range(framesTotal):
        frame = ImageTk.PhotoImage(image.copy())
        animation.append(frame)
        image.seek(x)

def gif_work(cycle,frames,event_number,first_num,last_num):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
  if (event_number < 5):
    event_number = random.randrange(first_num,5+1,1)
  else:
    event_number = random.randrange(4, last_num + 1, 1)
 return cycle,event_number

def event(cycle,check,event_number,x):
    if event_number in left:
        check = 1
        print('left')
        window.after(100,update,cycle,check,event_number,x)
    elif event_number in right:
        check = 2
        print('right')
        window.after(100, update, cycle, check, event_number, x)


def update(cycle,check,event_number,x):
    if (x <= 0) :
        check = 2
    elif (x >= width):
        check = 1
    if check==1:
        frame = walk_left[cycle]
        cycle , event_number = gif_work(cycle,walk_left,event_number,1,8)
        x -= 3
    elif check==2:
        frame = walk_right[cycle]
        cycle , event_number = gif_work(cycle,walk_right,event_number,1,8)
        x += 3

    window.geometry('160x160+'+str(x)+'+'+str(y))
    if (platform.system() == 'Windows'):
        label.configure(image=frame)
    else:
        label.pack_forget()
        label.config(image=frame)
        label.pack()
    window.after(1,event,cycle,check,event_number,x)   

#call cows's action .gif to an array
walk_right = []
loadGif(walk_right, 19, Image.open(impath+"Right-Cow-Transparent.gif"))
walk_left = []
loadGif(walk_left, 20, Image.open(impath+"Left-Cow-Transparent.gif"))

if (platform.system() == 'Windows'):
    window.config(highlightbackground='yellow')
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.wm_attributes('-transparentcolor', 'yellow')
else:
    window.overrideredirect(1)
    window.overrideredirect(0)
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-transparent", True)


label = tk.Label(window,bd=0,bg='yellow')
label.pack()

window.after(1,update,cycle,check,event_number,x)
window.mainloop()