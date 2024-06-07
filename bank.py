
class Account:
    def __int__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self ._balance:
            self._balance -= amount
            return True
        else:
            print("insufficient funds!")
            return False

    def get_balance(self):
        return self._balance



class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <= 700000:
            super().deposit(amount)
            self._balance *= 1.005  # 0.5% interest
        else:
            print("Deposit limit exceeded for Savings Account")
