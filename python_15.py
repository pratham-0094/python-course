import copy
l1 = [1, 2, 3, 4, 5]
l2 = l1  # same variable different name
print(l2)
print(id(l1))
print(id(l2))
l1[2] = 100
print(l2)


# shallow copy - copy is one level of deep, copying do not recurse
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))
l1.append([10, 11, 12])
print(l1)
print(l2)
l1[0][1] = 999
print(l1)
print(l2)

# deep copy - clone of the data copied
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.deepcopy(l1)
print(l2)
print(id(l1))
print(id(l2))
l1.append([10, 11, 12])
print(l1)
print(l2)
l1[0][1] = 999
print(l1)
print(l2)
