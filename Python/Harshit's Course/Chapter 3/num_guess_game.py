# Game to guess a number b/w 1 to 100

import random
wining_num=random.randint(1,100)
#print(wining_num) # To check wining number
count=0

for i in range(100):
    num=int(input("Enter a number b/w 1 or 100 : "))
    count+=1
    
    if num==wining_num:
        print("YOU WIN !!!")
        print("You took",count,"Tries")
        break
    else:
        if num<wining_num:   
            print("too low")
        else:
            print("too high")            
