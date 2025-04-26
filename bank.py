class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 100 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount. Need at least 100")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
