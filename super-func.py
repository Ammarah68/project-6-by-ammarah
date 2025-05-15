class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject
        print(f"Teacher specializes in: {self.subject}")

t = Teacher("Ali", "Mathematics")
