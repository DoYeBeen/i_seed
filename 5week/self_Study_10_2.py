from tkinter import *
from PIL import Image, ImageTk
import random

##전역 변수 선언 부분##
btnList = [None] * 9
fnameList = ["a.jpg","b.jpg", "c.jpg","d.jpg",
             "e.jpg", "f.jpg", "g.jpg", "h.jpg", "i.jpg"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0
random.shuffle(fnameList)

##main code##
window = Tk()
window.geometry("240x240")
fnameList = (fnameList * 2)[:9]

for i in range(0, 9):
    img = Image.open("jpg/" + fnameList[i])
    img = img.resize((70, 70), Image.Resampling.LANCZOS)
    photoList[i] = ImageTk.PhotoImage(img)
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
