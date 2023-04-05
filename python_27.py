class Student:
    marks = 30

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printdetail(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    @classmethod # using class method as an alternate constructor
    def from_string(cls, string):
        arg = string.split('-')
        print(arg)
        return cls(arg[0], arg[1])

    @staticmethod # static method used as an utility mathod, it belong to the class
    def passingmarks(number):
        return number > 28


sita = Student.from_string("sita-21")

sita.printdetail()
print(Student.passingmarks(23))
