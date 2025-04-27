class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 50:
            raise ValueError("Please git add .
git commit -m "OPS-7: Implement deposit and withdrawal limits"
git push origin OPS-7-Add-Withdraw-and-Deposit-Limits
Deposit at least 50.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 50 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount. Please Withdraw a minimum of USD 50")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
