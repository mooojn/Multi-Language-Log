import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("MenuBar")

def func():                         # Called when any of the option from
    print("Hi")                     # The menu is clicked

main_menu=tk.Menu(win)

# File Menu
file_menu=tk.Menu(main_menu,tearoff=False)            # Tearoff removes a line
                                                      # From the menu bar
file_menu.add_command(label="New File",command=func)   
file_menu.add_command(label="Open File",command=func)
file_menu.add_separator()                             # Separate by line
file_menu.add_command(label="Save",command=func)
# Edit Menu
edit_menu=tk.Menu(main_menu,tearoff=False)            

edit_menu.add_command(label="Undo",command=func)
edit_menu.add_command(label="Redo",command=func)
edit_menu.add_separator()                             # Separate by line 
edit_menu.add_command(label="Copy",command=func)
edit_menu.add_command(label="Paste",command=func)

main_menu.add_cascade(label="File",menu=file_menu)    # Adding labels 
main_menu.add_cascade(label="Edit",menu=edit_menu)    # On top window
   
win.config(menu=main_menu)                            # To display menu
                                                      # Bars created
win.mainloop()
