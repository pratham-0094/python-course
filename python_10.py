# Types of Function
# Built-in Function
# User-defined Function


# User-defined Function
l1 = [1, 2, 3, 4]
s1 = sum(l1)
print(s1)


# User-defined Function

# function defination
def print_hi():
    print('hello')
    print('world')

# function call
print_hi()


# passing parameter/argument to function
def div(a, b):
    return a/b

print(div(9, 2))


# Types of Argument
# Default Argument
# Keyword Argument
# Positional Argument
# Variable Length Argument

# Default Argument
def add(a=3, b=5):
    print("the sum of a and b is ", a+b)

add(1)


# Keyword Argument
def sub(a, b):
    print("the sub of a and b is ", a-b)

sub(b=1, a=1)


# Positional Argument
def mul(a, b):
    print("the mul of a and b is ", a*b)

mul(9, 2)


# Variable Length Argument
# *args **kwargs
def list_print(*a):
    for i in a:
        print(i)

list_print(1, 2)


def dict_print(**q):
    print(q['a'])
    print(q['b'])
    print(q['c'])
    print(q['d'])
    print(q['e'])

dict_print(a=1, b=2, c=3, d=10, e=30)


# Docstring
def greet():
    '''this function will greet you'''
    print("welcome to my channel")

print(greet.__doc__)
