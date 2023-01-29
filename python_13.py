a = 20  # global

def greet(name):
    global a  # this is used to make this variable global
    a = a+10
    print(a)  # 30
    print("hello "+name)


greet("rohan")


# another example
def outer():
    a = 5

    def inner():
        global a  # it is not used to access the outer scope variable but to access the global scope
        a = 100
        print(a)  # 100

    inner()
    print(a)  # 5


outer()
print(a)  # 100
