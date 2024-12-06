import tkinter as tk 
import ttkbootstrap as tb

root=tb.Window(themename="superhero")
root.title("Check Buttons")
root.geometry('500x400')

# label
my_label=tb.Label(text="Click boxes below",font=("Helvetica",12))
my_label.pack(pady=(40,10))

# functions if box is checked
def checked():
    pass

# check button
var1=tk.IntVar()
my_check=tb.Checkbutton(text="CheckButton!!",
                        bootstyle="info",
                        variable=var1,
                        offvalue=0,
                        onvalue=1,
                        command=checked
                        )
my_check.pack(pady=10)

# tool button
var2=tk.IntVar()
my_tool=tb.Checkbutton(text="ToolButton!!",
                        bootstyle="info,toolbutton",
                        variable=var2,
                        offvalue=0,
                        onvalue=1,
                        command=checked
                        )
my_tool.pack(pady=10)

# outlined tool button
var3=tk.IntVar()
my_outlinetool=tb.Checkbutton(text="Outlined ToolButton!!",
                        bootstyle="warning,outline toolbutton",
                        variable=var3,
                        offvalue=0,
                        onvalue=1,
                        command=checked
                         )
my_outlinetool.pack(pady=10)

# round toggle button
var4=tk.IntVar()
my_roundtoggle=tb.Checkbutton(text="Round ToggleButton!!",
                        bootstyle="success,round toggle",
                        variable=var4,
                        offvalue=0,
                        onvalue=1,
                        command=checked
                         )
my_roundtoggle.pack(pady=10)

# square toggle button 
var5=tk.IntVar()
my_squaretoggle=tb.Checkbutton(text="Square ToggleButton!!",
                        bootstyle="info, square toggle",
                        variable=var5,
                        offvalue=0,
                        onvalue=1,
                        command=checked
                         )
my_squaretoggle.pack(pady=10)


root.mainloop()
