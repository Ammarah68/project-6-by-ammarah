class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):  # Diamond Inheritance
    pass


d = D()
d.show()

# To see the MRO:
print("Method Resolution Order:", D.__mro__)
