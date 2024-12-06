# Program to check 
# If you can watch the moive

name=input("Enter your name : ")
age=int(input("Enter your age : "))

if name.lower()[0]=='m' and age>9: # First letter of name is 'm' or 'M'
    print("You can watch movie")
else:
    print("Sorry, you cannot watch movie")
