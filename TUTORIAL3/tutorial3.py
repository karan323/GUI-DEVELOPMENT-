from tkinter import *
import tkinter as tk
import tkinter.font




# create main window 
win = Tk()
c = Canvas(win, bg="coral", height=600, width=1000)
win.title("MY GUI")
c.pack()

#design a label
label = tk.Label(win, height=2, width=50, fg= "gray30", bg= "green yellow", borderwidth=10, relief="raised")
label.place(x=100, y=0)
label.config(font=("times", 18, "bold"))
label.config(text=str('MY FIRST LABEL'))


