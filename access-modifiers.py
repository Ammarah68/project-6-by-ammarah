class Employee:
    def __init__(self, name, salary, emp_id):
        self.name = name          # public variable
        self._salary = salary     # protected variable
        self.__id = emp_id        # private variable

    def show_info(self):
        print("Inside Class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("Employee ID:", self.__id)


# Example usage
if __name__ == "__main__":
    emp = Employee("Ahmed", 60000, "EMP12345")

    # Public access
    print("Name:", emp.name)  # ✅ Works

    # Protected access
    print("Salary:", emp._salary)  # ⚠️ Works, but use with caution

    # Private access attempt
    try:
        print("ID:", emp.__id)  # ❌ Raises AttributeError
    except AttributeError as e:
        print("Error:", e)

    # Access private variable with name mangling
    print("ID (via mangling):", emp._Employee__id)  # ✅ Works

    # Access all from within class
    emp.show_info()
