import abc 
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Encapsulated Attribute

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount
        

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Invalid input"
        
    def apply_interest(self):
        self.__balance += self.__balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.__balance += amount
        

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Invalid input"
        
    def deduct_fee(self):
        self.__balance -= self.fee

def print_account_details(account):
    print(f"Account Details: \nOwner: {account.owner} \nBalance: {account.get_balance()}")

def process_amount(account, transaction_type, amount):
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)
    else:
        return "Incorrect transaction type"
    
# Create instance of SavingsAccount and CheckingAccount
savings = SavingsAccount("John", 1000)
checking = CheckingAccount("Jane", 500)

# Using Polymorphism on different types of accounts 
print_account_details(savings)
print_account_details(checking)

# Applying interest to savings account
savings.apply_interest()
print_account_details(savings)