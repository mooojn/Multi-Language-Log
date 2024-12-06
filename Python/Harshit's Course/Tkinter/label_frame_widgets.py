import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Label Frame")

frame=ttk.LabelFrame(win,text="Enter data below ")      # Frame
frame.grid(row=0,column=0,padx=50)                          

# The whole code below is from the widgets_loop.py program 
# Which is in the same folder as this program is

labels=['Name','Age','Gender','City','Country']

for i in range(len(labels)):
    cur_label=ttk.Label(frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=4,pady=4)

user_info={
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'city' : tk.StringVar(),
    'country' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_box=ttk.Entry(frame,width=16,textvariable=user_info[i])
    cur_box.grid(row=counter,column=1,padx=4,pady=4)
    counter+=1

def submit():
    for i in user_info:
        print(user_info[i].get())        
    win.destroy()

submit_btn=ttk.Button(win,text="Submit",command=submit)
submit_btn.grid(row=1,column=0)

win.mainloop()
