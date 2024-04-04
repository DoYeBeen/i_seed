from tkinter import *
import random


##전역 변수 선언 부분##
btnList = [None] * 9
fnameList = ["sample1.jpg","sample2.jpg", "sample3.jpg","sample4.jpg",
             "sample5.jpg", "sample6.jpg", "sample7.jpg", "sample8.jpg", "sample9.jpg"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0
random.shuffle(fnameList)

##main code##
window = Tk()
window.geometry("210x210")
fnameList = (fnameList * 2)[:9]

for i in range(0,9):
    photoList[i] = PhotoImage(file = "jpg/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()