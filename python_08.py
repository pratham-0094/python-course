# break - end the loop
i = 0
while True:
    if(i > 10):
        break
    print(i)
    i = i + 1

# ontinue - jump to the next iteration
i = 0
while i <= 10:
    i = i+1
    if i < 5:
        continue
    print(i)

# program - not over untill you enter number greater than 100
while True:
    number = int(input("enter no. greater than 100\n"))
    if number < 100:
        print("tryagain with larger no\n")
        continue
    else:
        print("success\n")
        break
