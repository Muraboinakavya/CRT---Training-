'''
What is encapsulation ?
Binding of data and methods together into a single unit
And:
restricting direct access to data 
 
 Encapsulation protects the data from 
 1.unauthorized access
 2.accidential modification
 --->similarily In oops:
data is hidden inside the classs access using the methods
key-idea
data +methods
     |
combined  into a single unit
       |
    control access
----->Features of Encapsulation:
1.security
2.data hiding
3.control access
4.Better maintenance
5.Better organization
#Ex: No encapsulation:
balance = 500000
balance = - 500000
-----------------------------------------------------------
#Encapsulation:
class Bank:
    def __init__(self):
        self.balance = 1000
    def deposite(self,amount):
         self.balance +=amount
    def show_balance(self):
        print(self.balance)
s1 = Bank()
s1.deposite(500)
s1.show_balance()#data and methods  are bound together
--------------------------------------------------------------------
--->data hidding:
restricting the access to direct variables
goal:
to prevent the  data modification missusing the data
acces modofieds in python
1.public
2.protect(denoted by single underscore)
3.private(denoted by double underscore)
------------------------------------------------------------------------------
1.public : memebers can accessible everey where and it is default acces in python
Ex:
class Bank:
     def __init__(self):
feratures for public:
Access anywhere
No restriction
Default behaviour
-------------------------------------------------------
2.protect:_single_underscore
should not directly access directly outside the class
EX:

class Student:
     def __init__(self):
        self._marks = 90
s1 = Student()
print(s1._marks)

In python the protected members  are not exactly protected 
please dont access it directly
where  to use?
1.During inheritance
2.for internal usage
---------------------------------------------------------------
3.private:__(double under score)
used for: strong data hidding
Ex:
class Student:
     def __init__(self):
         self.__marks = 90
s1 = Student()
print(s1.__marks)# this will give the attribute error: because of the name mangling
--------------------------------------------------
#Name Mangling
__marks
   |
_Student__marks
Prevent:
accidental direct access
accidental overriding
#can i access private var inside the class
class Student:
    def __init__(self):
        self.marks=90

    def show(self):
        print(self.__marks)


s1=Student()
s1.show() #accesed with the same class 
#try to access using name mangaling
class Student:
    def __init__(self):
        self.__marks=90

s1=Student()
#I am using name mangaling to access
print(s1._Student__marks)

self.__marks
    |
 python will convert
      |
    self._Student__marks
------------------------------------------------------------------------
Acess modifiers      |      syntax             | Accessible outside
1.public                  variable                    yes 
2.protect                  _variable                   yes(convention only)
3. private                 __variable                   No directly 
-----------------------------------------------------------------------------
#task: create a class named"BankAccount"
#balance--->private
#deposite
withdraw amountcheck for balanceprint balance using name mangling:
class BankAccount:
    def __init__(self,balance,amount):
        self.__balance = balance
        self.__deposite = self.__balance + amount
        self.__withdraw = self.__balance - amount
    def show_balance(self):
         print(self._balance)
s1 = BankAccount(5000,2000)
s1.show_balance()
print(s1._BankAccount__balance) 
--------------------------------------------

Getters and setters:
getters-->read the data
setters-->modify/update the data
Why use:
Student.marks = -90
Invalid
------------------------------------------
#Without getters and setters:
class Student:
     def __init__(self):
         self.marks = 90
s1 = Student()
s1.marks = -50
print(s1.marks)
'''
#With using the getter and setter:
class Student:
     def __init__(self):
         self.__marks = 90
    #getter method:
     def get_marks(self):
         return self.__marks
    #setter method:
     def set_marks(self,value):
         if value >=0:
             self._marks = value
         else:
             print("Invalid marks")
b1 = Student()
print(b1.get_marks())
b1.set_marks(95)
print(b1.get_marks())
b1.set_marks(-95)
print(b1.get_marks())




         




           