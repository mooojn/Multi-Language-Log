# Program to return 
# The number of lists 
# Present in a list

def sublist_detector(lst):
    count=0
    for i in lst:
        if type(i) is list:
            count+=1
    return count

lst=[1,[2,3],[4,5],6]
print(sublist_detector(lst))
