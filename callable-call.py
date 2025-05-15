class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

# Testing callable
print("Is 'double' callable?", callable(double))  # True

# Calling the object like a function
print("double(5):", double(5))  # 10
print("triple(4):", triple(4))  # 12
