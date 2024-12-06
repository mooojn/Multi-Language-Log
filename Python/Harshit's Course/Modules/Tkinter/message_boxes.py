import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win=tk.Tk()
win.title("Message Box")

# Label frame
frame=ttk.LabelFrame(win,text="User Info")
frame.grid(row=0,column=0,padx=40,pady=10)

# Labels
name_label=ttk.Label(frame,text="Enter your name : ",font=("Helvetica",14)).grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)
age_label=ttk.Label(frame,text="Enter your age : ",font=("Helvetica",14)).grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

# Entry Boxes
name_var=tk.StringVar()
name_box=ttk.Entry(frame,width=36,textvariable=name_var)
name_box.grid(row=1,column=0,padx=5,pady=5)
age_var=tk.StringVar()
age_box=ttk.Entry(frame,width=36,textvariable=age_var)
age_box.grid(row=1,column=1,padx=5,pady=5)

# Submit function
def action():
    # m_box.showinfo('Title',"content")
    name=name_var.get()
    age=age_var.get()
    if name== '' or age== '' :
        m_box.showwarning("Input missing","Please enter data in all of the fields")
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror("Invalid input","Please enter age in digits")        
        else:
            with open('data.txt','a') as f:
                f.write(name+" "+str(age)+"\n")
            
            name_box.delete(0, 'end')
            age_box.delete(0, 'end')

            # win.destroy()

# Submit button
submit_btn=ttk.Button(text="Submit",command=action).grid(row=1,columnspan=2, padx=40)

win.mainloop()
