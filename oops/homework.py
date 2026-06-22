'''
-----------------------------------------------------------------------------
TAsk1: create a class of Employee and the instance variable in the constructor:
class Employee:
    def __init__(self,emp_id,emp_name,salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.salary)
s1 = Employee(108,"kavya",10000)
s1.display()

#TAsk2: create a class Rectangle:
class Rectangle:
    def __init__(self,length,width):
         self.length = length
         self.width =  width
    def display(self):
         print(self.length)
         print(self.width)
         Area = self.length * self.width
         print(Area)
s1 = Rectangle(10,20)
s1.display()

---------------------------------------------------

# instance variable:
#Task1:create 3 student objects:
class Student:
    def __init__(self):
         self.name = "kavya"
         self.rollno = 100
         self.marks = 200
    def display(self):
         print(self.name)
         print(self.rollno)
         print(self.marks)
s1 = Student()
s2 = Student()
s3 = Student()
s1.display()
#TAsk2:create a bank deposit ,withdraw,holdername:
class BankAccount:
     def __init__(self,name,balance,deposite,withdraw):
        self.name = name
        self.balance =balance
     def deposite(self):
        self.deposite = self.deposite + self.balance
        print(self.deposite)
     def withdraw(self):
        self.withdraw = self.balance -  self.withdraw
        print(self.withdraw)
     def display(self):
        print(self.name)
        print(self.balance)
        print(self.deposite)
        print(self.withdraw)
s1 = BankAccount("kavya",1000000,1,1)
s1.display()
#TASK3:   print th book details:
class Book:
     def __init__(self):
         self.title = "bangaram"
         self.author = "kavya"
         self.price = 10000000
     def display(self):
         print(self.title)
         print(self.author)
         print(self.price)
s1 = Book()
s1.display()
------------------------------------------------------------------
'''
#Instance methods:
#TASK1: creaate a calculator:
class  Calculator:
     def __init__(self,a,b,add,sub,division):
         self.a = a
         self.b = b
     def add(self):
            self.add = self.a +self.b
     def sub(self):
         self.sub = self.a - self.b
     def division(self):
         self.division = self.a /self.b
     def display(self):
         print(self.a)
         print(self.b)
         print(self.add)
         print(self.sub)
         print(self.division)
s1 = Calculator(10,5)
s1.display()
        
         
         


