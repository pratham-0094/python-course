class Student:
    marks = 30

    # constructor is used to construct/initialized an object/instance of class
    def __init__(self, name, age):
        self.name = name  # self point to that instance of class that call the specific method
        self.age = age


ram = Student("harry", 21)
rohan = Student("rohan", 19)  # object initializing using constructor

print(ram.name)
print(ram.age)
print('-------------------------')
print(rohan.name)
print(rohan.age)
