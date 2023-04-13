# simple inheritance
# A -> B
# class A:
#     a=10
#     def greet(self):
#         print(self.a)

# class B(A):
#     pass

# a1=A()
# a1.greet()

# b1=B()
# b1.greet()


# multiple inheritance
# A -> C
# B -> C
class A:
    a=10
    def greet(self):
        print(self.a)

class B:
    a=20
    def leaving(self):
        print(self.a)

class C(A,B):
    # a=30
    pass

# a1=A()
# a1.greet()

# b1=B()
# b1.leaving()

# c1=C()
# c1.greet()
# c1.leaving()


# multilevel inheritance
# A -> B -> C
class A:
    a=10
    def greet(self):
        print(self.a)

class B(A):
    # a=20
    pass

class C(B):
    # a=30
    pass

# a1=A()
# a1.greet()

c1=C()
c1.greet()
