str = "this is my first program"

print(len(str))
# len() used to get the length of an object

# indexing
print(str[5])
print(str[-1])

# string slicing
print(str[0:5:2])
print(str[30])  # error index out of range
print(str[0:30])
print(str[0:])  # default take end index
print(str[:3])  # default take strat index
print(str[1:3:])  # default take step count 1
print(str[-8:-3])
print(str[::-1])  # reverseing a string
# default [start:end:1]

# string methods
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.replace("this", "the"))
print(str.count("m"))

# bool methods - True/False
print(str.endswith("program"))
print(str.startswith("this"))
print(str.isalnum())
print(str.isalpha())

str1 = "hello"
print(str1.isalpha())
