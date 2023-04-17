from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod 
    # must be overrided in child class
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self,name,a,b):
        self.name=name
        self.a=a
        self.b=b

    @property
    def area(self):
        return self.a*self.b
    
    @area.setter
    def area(self,a):
        self.a=2
        self.b=a/2

    @area.deleter
    def area(self):
        self.a=0
        self.b=0

    def printarea(self):
        return self.area

# s1=Shape() we cannot create object of abstract class
b1=Rectangle('r1',10,20)
print(b1.printarea())

# @property - getter, setter, deleter
print(b1.area)
print(b1.a,b1.b)
b1.area=2000
print(b1.a,b1.b)
del b1.area
print(b1.a,b1.b)
