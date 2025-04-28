class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 50:
            raise ValueError("Please Deposit at least USD 50!!!!")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 50 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount! Please Withdraw a minimum of USD 50!!")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
