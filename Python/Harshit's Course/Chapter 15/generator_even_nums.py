# Program to return 
# Even numbers upto given argument as generator
# So can be used only once 

def even_nums(n):
    yield [i for i in range(2,n+1,2)]
    
evens=even_nums(7)

for i in evens:
    print(i)
for i in evens:
    print(i)
