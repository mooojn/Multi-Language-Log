# Program to count 
# Instances of class objects

class Person:
    instance_count=0
    def __init__(self,name,age):
        Person.instance_count+=1
        self.name=name
        self.age=age

p1=Person('moon',21)
p2=Person('meeral',15)
p3=Person('saliq',19)
print(Person.instance_count)       
