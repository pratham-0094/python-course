class Student:
    # access specifiers
    # public - access by anyone
    a=10
    # private - access by no one
    __b=20
    # protected - access by class and sub class(Inheritance) not outside class
    _c=30

    def __init__(self,a):
        print('welcome to the school')
        self.a=a
        # print(self.__b)
    

    # dunder / special method
    def __repr__(self) :
        return f"Student({self.a})"
    
    def __str__(self): 
        return 'Student object'

s1=Student(100)
# print(s1._c)

#if repr and str both are present str is call but to call repr we use explict type casting
print(repr(s1))
