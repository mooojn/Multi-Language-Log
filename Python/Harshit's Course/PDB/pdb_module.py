# This module is used for debugging errors 
# Or to find the location of the error

import pdb

pdb.set_trace()                     # Used for the start location
                                    # Of the debugger
name=input("Enter your name : ")        
age=input("Enter your age : ")
age2=int(age)+5

print(f"Your name is {name.title()} and you'll be {age2} after 5 years")
