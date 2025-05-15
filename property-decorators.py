class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

item = Product(100)
print(item.price)     # Calls the getter
item.price = 150      # Calls the setter
print(item.price)
del item.price        # Calls the deleter
