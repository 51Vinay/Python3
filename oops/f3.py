#class variable
class Circle:
    pi=3.14 #pi is class variable
    def __init__(self,radius):
        self.radius=radius
        #self.pi=pi
    def cal_circumference(self):
        return 2*Circle.pi*self.radius
    def cal_area(self):
        return self.radius*self.radius
    
c1=Circle(4)    
print(c1.cal_circumference())
print(c1.cal_area())
c1=Circle(18)    
print(c1.cal_circumference())
print(c1.cal_area())


    
    