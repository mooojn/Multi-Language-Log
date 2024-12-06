# Program to return the cube 
# Upto the number output
# Provided in a dictionary

def dict_cube(num):
    cubes={}
    for i in range(1,num+1):
        cubes[i]=i**3
    return cubes

print(dict_cube(10))
