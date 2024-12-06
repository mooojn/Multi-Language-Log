# Program to return 
# The reverse of stings 
# Present in the list

def rev_lst_str(lst):
    rev=[]
    for i in lst:
        rev.append(i[::-1])
    return rev

lst=['abc','tuv','xyz']
print(rev_lst_str(lst))
