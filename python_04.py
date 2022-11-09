# list
list = ['string', 9, 10.5]
# collection of heterogenous datatype
# mutable, iterable
print(list)

print(list[2])
# accessing particular index

# string to tuple conversion
str_list = list("hello")
print(str_list)

# slicing
print(list[:])
print(list[::3])
print(len(list))

# list methods
list.append(2)
list.append([1, 3, "hello"])  # append another list - nested list
print(list)

list.pop(1)
print(list)

list.insert(2, 2)
print(list)

list.remove(2)
print(list)

list.reverse()
print(list)

list.clear()
print(list)

# tuple
t1 = (1, 1, 2, 88, 100, 1, 1, 1, 1)
# collection of heterogenous datatype
# immutable, iterable
print(type(t1))

# tuple methods
print(t1.index(1))
print(t1.count(1))

# how to append element to tuple
t1 = list(t1)
t1.append(2)
t1.append(3)
t1.append("hello")
t1 = tuple(t1)
print(t1)

# string to tuple conversion
str_tuple = tuple("hello")
print(str_tuple)
