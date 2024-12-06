# Program to return the average of three numbers
# Entered by the User

num1,num2,num3=input("Enter three numbers separated by comma : ").split(",")
print(f"average of three numbers is : {(int(num1)+int(num2)+int(num3))//3}")
