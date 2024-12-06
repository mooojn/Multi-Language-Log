# Program to return number of letters
# In a name without repetition

name=input("Enter your name : ")
nw=""

for i in name:
    if i in nw:
        continue
    print(i,':',name.count(i))
    nw+=i
