class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Using Employee's method

# Example usage
emp = Employee("Ali")  # Employee exists independently
dept = Department("HR", emp)
dept.show_details()
