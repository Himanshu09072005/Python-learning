class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):

        print("Name:", self.name)
        print("Balance:", self.balance)
        print()