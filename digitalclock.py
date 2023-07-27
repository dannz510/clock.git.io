from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date

root = Tk()
root.title("DIGITAL CLOCK")
root.iconbitmap('clock2.ico')
root.geometry("690x125")

def clock():
	string = strftime('%H:%M:%S:%p')
	label.config(text = string)
	label.after(1000, clock)


label = Label(root, font = ("vndi01.ttf",90), background = 'black', foreground = 'skyblue')

label.pack(anchor = 'center')

clock()
root.mainloop() 