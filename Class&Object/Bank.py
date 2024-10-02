class bank:

    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 5000
    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'fokira, you can not withdraw.minimum : {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'Bank fokir hoye jabe. max : {self.max_withdraw}')
        else:
            self.balance-=amount
            print(f'Here your money {amount}')
            print(f'your balance is {self.balance}')


# brac = bank(15000)
# brac.withdraw(25)
# brac.withdraw(100000)
# brac.withdraw(1000)

dbbl = bank(5000)
dbbl.deposite(2000)
dbbl.deposite(2000)
print(dbbl.get_balance())