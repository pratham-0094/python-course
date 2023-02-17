'''
Different mode to open a file
read - r
write - w
create file if not exists - x
append - a
text - t
binary - b
+ - read and write
'''
# open a file
# f = open("hello.txt","rb")
f = open("hello.txt")  # default mode rt - read and text mode

# read content of file
content = f.read()
print(content)

#reading in parts
# content = f.read(5)
# print(content)
# content = f.read(10000)
# print(content)

# print content character by character
for char in content:
    print(char)

# print content line by line
for line in f:
    print(line)

# another method to print content line by line
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)

# get list of line present in file
l1 = f.readlines()
print(l1)

f.close()  # closeing file
