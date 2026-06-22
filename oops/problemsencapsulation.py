#using the @property and @setter method
'''
class Student:
    def __init__(self):
        self.__marks=90

    #getter
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        if value >=0:
            self.__marks=value
        else:
            print("Invalid marks")


s1=Student()
print(s1.marks)
s1.marks=95
print(s1.marks)

Student marks validator
Create a class named as student :
Requirements are:
1.private variables--->__marks
methods set_marks(marks)
method get_marks()

rules:
Marks must be btw 0-100
otherwise print
Invalid marks

Example:Input[85]---->85
------------------------------------------------------------------
TASK1:
class Student:
     def __inti__(self):
         self.__marks = 0
     def get_marks(self):
         return self.__marks
     def set_marks(self,marks):
         if marks >=0 and marks <=100:
             self.__marks = marks
             print(self.__marks)
         else:
             print("Invalid marks")
marks = int(input())
s1 = Student()
print(s1.set_marks(marks))
print(s1.get_marks())
---------------------------------------------------------
#TASK2:create a class named as Employee
# requirements:
#1.private var- __salary
#2.salary should be < 15000
#3.method increase_salary(percent)
class Employee:
    def __init__(self):
        self.__salary =  0       
    def set_salary(self,salary):
        if salary >= 1500:
            self.__salary = salary
        else:
            print("invalid salary")
    def increase_salary(self,percent):
        self.__salary += (self.__salary*percent/100)
    def get_salary(self):
        return self.__salary
salary = int(input())
percent = int(input())   
e1 = Employee()
e1.set_salary(salary)
if salary >= 15000:
    e1.increase_salary(percent)
    print(e1.get_salary())
--------------------------------------------------------------
#TASK3: password checking
class PasswordManager:
     def __init__(self,):
        self.__password = ""
     def set_password(self,password):
         upper = False
         lower = False
         digit = False
         if len(password) < 8:
             print("weak password")
             return
         for ch in password:
             if ch.isdigit():
                digit = True
             elif ch.isupper():
                 upper = True
             elif ch.islower():
                 lower = True
         if (upper and lower and digit):
            print("password successfully")
         else:
            print("invalid password")
     def get_password(self):
         return self.__password
password = input()
p1 = PasswordManager()
p1.set_password(password)
----------------------------------------------------------------------------
#TASK4:
'''
class ShoppingCart():
     def __init__(self):
         self.__total = 0
     def add_item(self,price):
         if price >0:
            self.__total += price
     def remove_item(self,price):
         if price <= self.total:
             self.total -= price
     def apply_discount(self,percent):
         if self.__total >1000:
             self.total -=(self.__total*percent/100)
     def get_total(self):
         return self.__total
         
n = int(input())
cart = ShoppingCart()
for _ in range(n):
     price = float(input())
     cart.add_item(price)
remove_price = float(input())
cart.remove_item(remove_price)
discount = float(input())
cart.apply_discount(discount)
print(cart.get_total())

            
            



         
         
    
