import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')
root.geometry('500x350')

my_label=tb.Label(text="Hello World!",font=("Helvetica",12),bootstyle="default")
my_label.pack(pady=50)

count=0
def action():
    global count
    if count==0:
        my_label.config(text="Good Bye World") 
        count+=1
    else:
        my_label.config(text="Hello World")
        count-=1

my_btn=tb.Button(state="readonly",width=12,text="Click Me",command=action,bootstyle="succes, outline")
my_btn.pack(pady=20)

root.mainloop()