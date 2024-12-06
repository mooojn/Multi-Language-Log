# Program to filter 
# Odd and even numbers 
# From a list and put them in
# A new list as an individual lists

def filter_odd_even(lst):
    odd,even=[],[]    
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    filtered=[odd,even]
    return filtered
        
lst=list(range(1,11))
print(filter_odd_even(lst))
