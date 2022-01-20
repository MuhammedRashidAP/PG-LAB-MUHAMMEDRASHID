class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!  Welcome to the Deposit & Withdrawal ")
        self.account_number=input("enter the Account Number ")
        self.name=name=input("enter User Name ")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n User Name:",self.name)
        print("\n Account Number:",self.account_number)
        print("\n Net Available Balance=",self.balance)
 
  
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()