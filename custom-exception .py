# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        super().__init__(message)

# Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        print("Age is valid.")

# Example usage with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid number.")
