class BankAccount:
     def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance =balance
     def deposite(self,amount):
        self.balance = self.balance + amount 
     def withdraw(self,withdraw,amount):
        if(self.balance>= amount):
             self.balance -= amount
             print(self.withdraw) 
        else:
            print("Insufficient Balance")
     def display(self):
        print(self.account_holder)
        print(f"Amount Deposite" ,{self.balance})
        print(f"Amount withdraw", {self.balance})
        print(f"Amount current Balance " ,{self.balance})
s1 = BankAccount("kavaya",10000)
deposite = int(input())
withdraw = int(input())
s1.display()