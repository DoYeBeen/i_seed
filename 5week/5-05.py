from tkinter import *

window = Tk()
window.title("File Viewer")

# List of file names
fnameList = ["a.jpg", "b.jpg", "c.jpg",
             "d.jpg", "e.jpg", "f.jpg",
             "g.jpg", "h.jpg", "i.jpg"]
num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    update_label()

def clickPrev():
    global num
    num = (num - 1) % len(fnameList)
    update_label()

def update_label():
    label.config(text=fnameList[num])

label = Label(window, text=fnameList[num])
label.pack(pady=20)

prevButton = Button(window, text="<이전>", command=clickPrev)
nextButton = Button(window, text="<다음>", command=clickNext)

prevButton.pack(side=LEFT, padx=20, pady=20)
nextButton.pack(side=RIGHT, padx=20, pady=20)

window.mainloop()
