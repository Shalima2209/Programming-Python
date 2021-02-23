class bank():
        def __init__(self):
            self.balance = 0
            print("YOUR ACCOUNT IS CREATED")
        def deposit(self):
            amount=float(input("\n enter the amount to be deposited: "))   
            self.balance = self.balance + amount
            print("Amount Deposited :", amount)
        def withdraw(self):
            amount=float(input("\n enter the amount to be withdraw: "))     
            if self.balance >= amount:
               self.balance = self.balance - amount
               print("amount you withdrew:", amount)
            else:
                 print("'Insufficient balance")
            
a=bank()
a.deposit()
a.withdraw()
