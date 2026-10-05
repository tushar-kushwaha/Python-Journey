class Account:
    def __init__(self,balance):
        self.balance = balance
        print("your account have :",balance," balance")

    def deposit(self,money):
        self.money = money
        sum = self.balance + self.money
        self.balance = sum
        print("total money left in the account : ",sum )

    def credit(self,amount):
        self.amount = amount
        diff = self.balance - self.amount
        self.balance = diff
        print("this is the left over money: ",diff)    
    
        
s1 = Account(10000)

s1.deposit(15000)
s1.credit(7000)