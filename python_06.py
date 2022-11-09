# user input - input()
var1 = input("enter a number")  # default take input as string
print(type(var1))

# if else
age = int(input("enter your age"))

if age > 18:
    print("you can vote")
else:
    print("you can't vote")

# if elif else - if else ladder
v1 = 30
v2 = 20
if v1 > v2:
    print("v1 is smaller")
elif v1 == v2:
    print("value same")
else:
    print("v1 is greater")


print("v1 is greater") if v1 > v2 else print("v1 is smaller")  # short hand if else notation
