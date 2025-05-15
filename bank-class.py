class Bank:
    # Class variable
    bank_name = "UBL Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")


# Example usage
if __name__ == "__main__":
    # Creating instances of Bank
    acc1 = Bank("Ahmed")
    acc2 = Bank("Bilal")

    # Display info before changing bank name
    print("Before changing bank name:")
    acc1.display_info()
    acc2.display_info()

    # Change the bank name using class method
    Bank.change_bank_name("Trustworthy Bank")

    # Display info after changing bank name
    print("\nAfter changing bank name:")
    acc1.display_info()
    acc2.display_info()
