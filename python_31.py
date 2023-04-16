# polymorphism - ability to have more than one form
class A:
    classvar1=20
    def __init__(self):
        self.classvar1=10
        pass

    def add(self,a,b):
        return a+b

class B(A):
    classvar1=40
    # method overriding - method redefined in child class having same name and arguments as in parent class
    def __init__(self):
        super().__init__()
        self.classvar1=30
        pass

    def add(self,a,b,name):
        print(f'{name} marks is')
        return super().add(a,b)

b1=B()
# print(b1.classvar1)
print(b1.add(10,20,'rohan'))
