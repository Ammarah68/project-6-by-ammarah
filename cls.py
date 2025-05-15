class Counter:
    count = 0

    def __init__(self):
        # Increment the count each time an object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Number of objects created:", cls.count)


if __name__ == "__main__":
    # Creating multiple objects
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()

    # Display the total number of objects created
    Counter.show_count()
