import random
import datetime
import os

# The dir() function returns all properties and methods of the specified object, without the values
print(dir(random))
print(dir(os))
print(dir(datetime.datetime))

random.seed(1)

print(random.random())  # return interger value between the range 0 to 1
# return interger value between the range specified
print(random.randint(1, 10))

print(random.randrange(10))
print(random.randrange(1, 10, 6))
# The difference between the two of them is that randint can only be used when you know both interval limits.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# select to k unique element from the sample list
print(random.sample(l1, k=2))

l2 = [1, 2]
print(random.choice(l2))  # select to k element from the sample list
# select to k element from the sample list having weightage
print(random.choices(l2, weights=[10, 1], k=10))

# shuffle the list
print(l1)
random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)
