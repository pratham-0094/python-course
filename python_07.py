l1 = [1, 2, 3, 4, 5, "hello", "world"]
l2 = [[1, 8], [2, 3]]
d1 = dict(l2)  # list ot dictionary conversin
print(d1)

#  a loop is a sequence of instruction's that is continually repeated until a certain condition is reached

# for loop
# print all element of list / tuple / dictionary keys
for i in l1:
    print(i)

# for loop
# print dictionary keys and values
for i, j in d1.items():
    print(i, j)

# while loop
# to print number from 10 to 1
i = 10
while i > 0:
    print(i)
    i = i - 1
