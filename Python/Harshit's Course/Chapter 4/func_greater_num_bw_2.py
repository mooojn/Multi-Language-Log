# Program to find the greatest
# Between the two numbers

def greatest(num1,num2):
    if num1>num2:
        return num1
    return num2  

n1,n2=input("Enter two numbers sep by space : ").split()
print(greatest(int(n1),int(n2)),"is the greatest")
