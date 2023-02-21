# class syntax
class Student:
    marks = 30  # class variable
    pass


# creating object
ram = Student()
rohan = Student()

# object data members
# class variable
ram.name = "ram"
rohan.name = "rohan"
ram.age = 18
rohan.age = 20

# accessing object data members
print(ram.age)
print(rohan.age)
print(ram.name)
print(rohan.name)


# __dict__ is a dictionary object containing all attributes defined for that object itself
print(Student.__dict__)

# accessing class variable using object
print(ram.marks)
print(rohan.marks)
# accessing class variable using class
print(Student.marks)
Student.marks = 100

print(Student.__dict__)

# class variable can be access/modified through class or instance of that class
# if class variable is modified using object then it get copied to the object and create ita own new property
