from tkinter import *
import tkinter.font
from PIL import ImageTk,Image




# creat main window 
win = Tk()
c = Canvas(win, bg="black", height=600, width=600)
win.title("MY GUI")
myFont = tkinter.font.Font(family = 'Times', size = 10, weight='bold')
image2 = Image.open("E:\TKinter tutorial\matrial\logo\logo1.png")
image1 = ImageTk.PhotoImage(image2)
backgroung_label = Label(win, image=image1)
backgroung_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
