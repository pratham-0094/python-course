class Student:
    marks = 30

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printdetail(self):  # Instance Method
        print(self.name)
        print(self.age)
        print(self.marks)

    @classmethod  # It is a decorator used to add functionality such that it can access through any instance of class and able to access class variable
    def changemarks(cls):  # Class Method
        cls.marks = 999


ram = Student("harry", 21)
rohan = Student("rohan", 19)

# Student.marks=999
rohan.changemarks()
ram.printdetail()
rohan.printdetail()
