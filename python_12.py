# nested function
def outer():
    print("this is outer function")

    def inner():
        print("this is inner function")

    inner()
    print("this is last line")


outer()


# factorial
# 5! = 5 * 4 * 3 * 2 * 1
# fact(5)
# 5*fact(4)
# 5*4*fact(3)
# 5*4*3*fact(2)
# 5*4*3*2*fact(1)
# 5*4*3*2*1

# recursive function for factorial
def fact(n):
    if n < 0:
        return 0
    if n == 1 and n == 0:
        return 1
    return n*fact(n-1)


n = 5
result = fact(n)
print(result)


# fibonacci series for practice
# 0 1 1 2 3 5 8 13 21 .....
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))


n = 5
result = fibo(n)
print(result)
