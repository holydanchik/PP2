class Account: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 
 
    def deposit(self, amount): 
        self.balance += amount 
        print(f"{amount} has been deposited. Total balance: {self.balance}") 
 
    def withdraw(self, amount): 
        if amount > self.balance: 
            print("Withdrawal amount exceeds the current balance.") 
        else: 
            self.balance -= amount 
            print(f"{amount} has been withdrawn. Total balance: {self.balance}") 
 
# Instantiate the class 
account = Account("Danchik", 1000) 
 
# Make several deposits and withdrawals 
account.deposit(500) 
account.withdraw(300) 
account.withdraw(1800) 