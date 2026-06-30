class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError('Initial balance cannot be negative')
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        self.widhdraw(amount)
        target_account.deposit(amount)
        return self.balance





# Тестирование класса
account = BankAccount(100)
print(account.get_balance())
account.deposit(50)
print(account.get_balance())
account.withdraw(30)
print(account.get_balance())