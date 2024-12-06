# Program to return lenght of your name 
# And number of specified char present in your name
# Case insensitive

name,char=input("Enter your name and a single character comma sep : ").split(",")
print(f"Lenght of your name {len(name)}")
print(f"Number of {char} in your name : {name.lower().count(char.lower())}")
