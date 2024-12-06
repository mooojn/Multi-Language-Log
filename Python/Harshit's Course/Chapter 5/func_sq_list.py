# Program to return 
# The square of the list

def sq(lst):
    lst_sq=[]
    for i in lst:
        lst_sq.append(int(i)**2)
    return lst_sq

lst=input("Enter numbers : ").split()
print(sq(lst))
