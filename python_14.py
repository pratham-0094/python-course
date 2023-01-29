# lambda -single line / anonymous / no name function
def add(x, y):
    return x+y


def a(x, y): return x+y


print(a(1, 10))


# iterator - create itertor to iterate over iterable, it return one value at a time, lazy evaluation
l1 = [1, 2, 3, 4, 5]
iter1 = iter(l1)
print(next(iter1))


# map - mapping a value to another form
l1 = [1, 2, 3, 4, 5]
new_list = map(lambda x: x*2, l1)
print(list(new_list))


# filter - filtering / sorting value
l1 = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x < 3, l1)
print(list(new_list))


# generator function - to create an iterators
def reverse(l1):
    for i in range(len(l1)-1, -1, -1):
        yield l1[i]


l1 = [1, 2, 7, 9, 12, 44]
new_list = reverse(l1)

for i in new_list:
    print(i)
