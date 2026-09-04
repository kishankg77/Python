# Task 5: Encapsulation & Abstraction
# Practical Example: Bank Account Management System

from abc import ABC, abstractmethod


# Abstract Parent Class
class BankAccount(ABC):

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self._account_number = account_number
        self.__balance = balance

    # Encapsulation: controlled access to private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    # Abstraction: abstract method
    @abstractmethod
    def account_type(self):
        pass


# Child Class
class SavingsAccount(BankAccount):

    # Implementing abstract method
    def account_type(self):
        return "Savings Account"

    def display_info(self):
        print("\n----- Account Information -----")
        print("Account Holder :", self.account_holder)
        print("Account Number :", self._account_number)
        print("Account Type   :", self.account_type())
        print("Balance        :", self.get_balance())


# Creating objects
account1 = SavingsAccount("Kishan Gupta", "SB101", 10000)
account2 = SavingsAccount("Rahul Sharma", "SB102", 15000)

# Displaying account information
account1.display_info()
account2.display_info()

# Performing transactions
print("\n----- Transactions for Account 1 -----")
account1.deposit(2000)
account1.withdraw(3000)

print("Current Balance:", account1.get_balance())

print("\n----- Transactions for Account 2 -----")
account2.deposit(5000)
account2.withdraw(4000)

print("Current Balance:", account2.get_balance())