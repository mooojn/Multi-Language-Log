# Program using class method 

class Laptop:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def apply_disc(self,n):                     # Discount function
        return self.price-(n/100)*self.price

l1=Laptop("dell",'latitude',60000)
l2=Laptop('hp','zbook',50000)

print(l1.brand)
print(l2.name)
print(l1.apply_disc(20))
