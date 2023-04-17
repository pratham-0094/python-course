class Student:
    def  __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    # method overloading 
    def add(self,a,b,c=None):
        if c==None:
            return a+b
        else:
            return a+b+c
    
    # operator overloading using dunder methods
    def __add__(self,other):
        return self.marks+other.marks

    def __floordiv__(self,other):
        return self.marks//other.marks

s1=Student("rohan",19,100)
s2=Student("mohan",18,90)

print(s1.add(10,20,30))

print(s1+s2)
print(s2//s1)
