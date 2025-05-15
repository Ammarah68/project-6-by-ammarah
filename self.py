class Student:
    def __init__(self, name, marks):
        self.name = name         
        self.marks = marks      #self use for data

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)


if __name__ == "__main__":
    # Creating student objects
    student1 = Student("Alice", 85)
    student2 = Student("Bob", 92)

    # Displaying student details
    student1.display()
    print("---------------")
    student2.display()
