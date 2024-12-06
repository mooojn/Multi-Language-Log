# Program to return 
# Common elements from two lists

def common_el(lst1,lst2):
    common=[]
    for i in lst1:
        if i in lst2:
            common.append(i)
    return common

lst1,lst2=[1,2,3],[2,3,4]        
print(common_el(lst1,lst2))
