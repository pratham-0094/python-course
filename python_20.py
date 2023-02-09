# long method
l1 = ['ram', 'rohan', 'shyam', 'sita', 'gita']

i = 1
for name in l1:
    if i % 2 == 0:
        print(name)
    i += 1

# using enumerator function
for index, name in enumerate(l1):
    if index % 2 != 0:
        print(index, "  ", name)

str1 = "hello world"

for index, name in enumerate(str1):
    print(index, "  ", name)

# -------------------------------------

# long method
l1 = [21, 34, 11, 2, 6]
l2 = ['ram', 'rohan']

for i in range(5):
    print(l1[i], "  ", l2[i])

# using zip function
z1 = list(zip(l1, l2))
print(z1)

for i in zip(l1, l2):
    print(i[0], '  ', i[1])

for i, j in zip(l1, l2):
    print(i, '  ', j)
