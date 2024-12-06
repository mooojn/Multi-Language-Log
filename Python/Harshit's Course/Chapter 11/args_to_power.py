# Program to return 
# The numbers provided as list or tuple 
# To the power given at the function

def to_power(n,*args):
    if args:
        return [i**n for i in args]
    return "Hey, You did'nt pass any arguments"

n=3
nums=[1,2,3]
print(to_power(n,*nums))
