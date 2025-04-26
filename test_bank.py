import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount()
        acc.deposit(100)
        self.assertEqual(acc.get_balance(), 100)

    def test_withdraw(self):
        acc = BankAccount()
        acc.deposit(200)
        acc.withdraw(50)
        self.assertEqual(acc.get_balance(), 150)

    def test_invalid_withdraw(self):
        acc = BankAccount()
        with self.assertRaises(ValueError):
            acc.withdraw(100)

if __name__ == '__main__':
    unittest.main()
