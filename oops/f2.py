class Person:
    count_instance=0
    def __init__(self,firstname,lastname):#here fs,ls and age are attribute
        #instance variables
        Person.count_instance += 1
        self.firstname=firstname
        self.lastname=lastname
    def full_name(self):
        return  f"{self.firstname} {self.lastname}"  
#object of this person class
#self represent the object
p1=Person('Vinay','sharma')
p2=Person('Nitin','sharma')


print(p1.firstname)
print(p2.firstname)
print(Person.full_name(p1))
print(Person.full_name(p2))
print(p1.__dict__)
print(p2.__dict__)
print(Person.count_instance)
class Laptop:
    count_instance=0
    def __init__(self,brand_name,model_name,price):
        
        Laptop.count_instance +=1
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def full_spec(self):
        return f"{self.brand_name} {self.model_name} {self.price}"
    def is_price(self):
        return self.price <= 50000
    def apply_discount(self,num):
        #self.price
        total_dicount=(num/100)*self.price
        return self.price-total_dicount
             
l1=Laptop('HP','14s',50000)#here hp,14s,50000 are aguement
l2=Laptop('Dell','Vista',45000)
print(l1.brand_name)
print(Laptop.full_spec(l1)) 
print(l2.is_price())
print(l2.brand_name)
print(Laptop.full_spec(l2)) 
print(l2.is_price()) 
print(l1.apply_discount(10))
print(l2.apply_discount(10))
print(l1.__dict__)
print(l2.__dict__) 
print(Laptop.count_instance) #total instance in laptop   