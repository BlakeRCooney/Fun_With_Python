class Account:
    def __init__(self, name, balance, minimum_balance):
        self.name = name
        self.balance = balance
        self.minimum_balance = minimum_balance


    def Deposit(self, amount):
        self.balance += amount

    def Withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
        else:
            print("Insufficient Funds!")

    def Statement(self):
        print("Account Balance: ${}".format(self.balance))

class Checking(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, minimum_balance = 0)

    def __str__(self):
        return "{}'s Checking Account: Balance ${}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, minimum_balance = 0)
        
    def __str__(self):
        return "{}'s Savings Account: Balance ${}".format(self.name, self.balance)
