#python_classes_and_objects
from datetime import datetime


"""
    Create a Python class representing a bank account. 
    The class should have the following attributes and methods:
    Attributes:account_holder (string): 
    The name of the account holder.balance (float): 
    The current balance of the account.Methods:__init__(self, account_holder, initial_balance): 
    A constructor that initializes the account with the account holder's name and an initial balance.deposit(self, amount): 
    A method that adds a specified amount to the account balance.withdraw(self, amount): 
    A method that subtracts a specified amount from the account balance.get_balance(self): 
    A method that returns the current balance of the account.
"""

class Bank_account:
    def __init__(self, account_holder,total_balance = 0):
        self.account_holder = account_holder
        self.total_balance = total_balance

    def deposit(self, amount):
        self.total_balance = self.total_balance + amount
        print(f"Deposit of amount {amount} was successful.\n Account Balance is: {self.total_balance}")
        return self.total_balance
        
    def withdraw(self, amount):
        if self.total_balance > amount:
            self.total_balance = self.total_balance - amount
            print(f"Withdrawal of Amount {amount} was successful")
            print(self.total_balance)
        else:
            print(f"Not enough to withdraw amount {amount}. \n Your account balance is {self.total_balance}. \n Try a lower amount")
        return self.total_balance

    def get_balance(self):
        print(f"Your account balance at {datetime.now()} is {self.total_balance}")
        return self.total_balance


Person1 = Bank_account("John Doe")
Person1.deposit(500)
Person1.deposit(1500)
Person1.deposit(46)
Person1.withdraw(250)
Person1.get_balance()