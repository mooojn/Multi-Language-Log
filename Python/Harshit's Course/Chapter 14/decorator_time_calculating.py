# Program to return 
# The time taken by function 
# To complete task using decorator

from functools import wraps
import time

def time_cal(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        t1=time.time()
        ans=func(*args,**kwargs)
        t2=time.time()
        TimeTaken=t2-t1
        print("This function took : ",TimeTaken,"sec")
        return ans
    return wrapper_func

@time_cal
def sq(n):
    return [i**2 for i in range(n+1)]

sq(10000000)
