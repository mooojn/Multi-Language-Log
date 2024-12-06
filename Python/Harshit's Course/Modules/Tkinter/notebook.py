import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Notebook")

note_book=ttk.Notebook(win)         # Page1, and Page 2 create
pg1=ttk.Frame(note_book)
pg2=ttk.Frame(note_book)

note_book.add(pg1,text="one")       # Adding pages to the notebook
note_book.add(pg2,text="two")

note_book.pack(expand=True,fill="both")

pg1_label=ttk.Label(pg1,text="Enter your name : ")  # Name label on page 1
pg1_label.grid(row=0,column=0)

pg2_label=ttk.Label(pg2,text="Enter your age : ")   # Age label on page 2
pg2_label.grid(row=1,column=0)

pg1_entrybox=ttk.Entry(pg1,width=16)                # Entry box for name
pg1_entrybox.grid(column=1,row=0)                   #      on page 1

win.mainloop()
