class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print( f'withdraw not possible below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print( f'withdraw not possible upto {self.max_withdraw}')
        else:
            self.balance -= amount
            print( f'here is your money {amount}')
            print(f'your balace after withdraw : {self.get_balance()}')

ific = Bank(15000)
ific.withdraw(10)
ific.deposit(1000)
ific.withdraw(2000000)
ific.withdraw(5000)