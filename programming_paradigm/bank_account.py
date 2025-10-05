class BankAccount:
    def __init__(self, initial_balance: float = 0) -> None:
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.") 
        self.account_balance += float(amount)

    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("Insufficient funds.")
        if amount <= self.account_balance:
        self.account_balance -= float(amount)
        return True
    return False
    def display_balance(self):
         print(f" Current Balance: ${self.account_balance}")


    


      

