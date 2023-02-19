# class - template/blueprint
# object - instance of class

# object-oriented programming follow DRY (do not repeat yourself) approach

# if we don't know the implementation of any block now, but we have to run the code to check if it's working fine untill now
# for this we can use pass keyword to complete the block
def fun():
    pass

# class syntax


class Student:
    pass


# creating object
ram = Student()
rohan = Student()

# object data members
ram.name = "ram"
rohan.name = "rohan"
ram.age = 18
rohan.age = 20

# print(id(ram))
# print(id(rohan))

# accessing object data members
print(ram.age)
print(rohan.age)
print(ram.name)
print(rohan.name)
