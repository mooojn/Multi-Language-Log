# Program to return the list with first word capital 
# If 2nd argument is'nt passed. 
# If 2nd argument is passed then reverse the string 
# In list and make the 1st letter capital
 
def func(lst,**kwargs):
    if kwargs.get('reverse_string'):
        return [(i[::-1].title()) for i in lst]
    return [i.title() for i in lst]

lst=["moon","tariq"]
print(func(lst,reverse_string=True))
