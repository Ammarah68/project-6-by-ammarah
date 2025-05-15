# Class decorator definition
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.greet())
