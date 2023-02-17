# opening file in write mode
f = open("hello.txt", "w")

# opening file in append mode
f = open("hello.txt", "a")

# opening file in read and write mode
f = open("hello.txt", "r+")

# writing to file
f.write("good morning\n")

content = f.read()
print(content)

# get location of pointer
loc = f.tell()
print(loc)

# set pointer to specific location
f.seek(10)

loc = f.tell()
print(loc)

f.close()  # closing file

# opening file using with block
with open("hello.txt") as f:
    a = f.read()
    print(a)
# automatically close the file after block end
