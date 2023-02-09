# string formatting
#method - 1
greet = "welcome"
hello = "hello"
str = "hello world "
print("hello world %s" % greet)

# -----------------------------------------------------

#method - 2
a = "{1} world {0}".format(hello, greet)
print(a)

# -----------------------------------------------------

#method - 3
name = "ram"
greet = "hello"
print(f"welocome {name},{greet}")


# python comprehensions
# list comprehensions
list = [i for i in range(100) if i % 3 == 0]
print(list)

# -----------------------------------------------------

# dictionary comprehensions
dict = {i: f"item{i}" for i in range(10)}
print(dict)

# exchange key value of dictionary
dict = {value: key for key, value in dict.items()}
print(dict)

# -----------------------------------------------------

# sets comprehensions
set = {i for i in [1, 1, 2, 3, 34, 2, 1, 2, 1, 1, 12, 1, 1]}
print(set)

# -----------------------------------------------------

# generator comprehensions
gen = (i for i in [1, 1, 2, 3, 34, 2, 1, 2, 1, 1, 12, 1, 1])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
