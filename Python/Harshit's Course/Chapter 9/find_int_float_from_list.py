# Program to return 
# Integers and floats from a list

lst=[True,False,[1,2,3],4,5.0,6.7]

filtered=[str(i) for i in lst if type(i)==int or type(i)==float]
print(filtered)
