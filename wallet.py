# wallet.py
from ownable import Ownable

class Wallet(Ownable):
    def __init__(self, owner):
        super().__init__(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0
