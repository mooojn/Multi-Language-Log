# Program to return 
# The reverse of list

def rev_lst(lst):
    rev=[]
    for i in range(len(lst)):
        rev.append(lst.pop())
    return rev

lst=[1,2,3,'moon']
print(rev_lst(lst))
