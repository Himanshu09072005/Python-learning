class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid transaction")

    def get_balance(self):
        return self.__balance