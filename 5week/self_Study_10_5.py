from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageOps

# 함수 선언
def func_open():
    filename = askopenfilename(parent=window, filetypes=(("jpg파일", "*.jpg"),
                                                         ("모든 파일", "*.*")))
    if filename:
        img = Image.open(filename)
        img = img.resize((400, 400), Image.Resampling.LANCZOS)
        photo = convert_image_to_greyscale(img)
        imgTk = ImageTk.PhotoImage(image=photo)
        pLabel.configure(image=imgTk)
        pLabel.image = imgTk

def convert_image_to_greyscale(img):
    width, height = img.size
    result = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            grey = int((r + g + b) / 3)
            result.putpixel((x, y), grey)
    return result

def func_exit():
    window.quit()
    window.destroy()

# main code
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
