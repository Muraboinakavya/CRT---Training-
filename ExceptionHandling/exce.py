'''
Error : An error is the problem in a program  causing abnormal termination
1.Syntax error(compile time error is mistake in the code)
2.Run time error ---Exceptions
--->Occurs while executing the program
Ex:
a = 10
b = 0
c = a/b --->ZeroDivision
3. Logical Errors:
program runs but gives wrong output
Ex: print(2*(3+5)) --->output(16)
------------------------------------------------------
what is exception handling?
Exception handling is a mechanism to handle run time errors gracefully without stopping the program
1.program crashes
2.poor user experince
3.Data loss possible
------------------------------------------------
With exception:
1.progra will execute normally
2.proper error message
3.safer application
Basic Exception:
Syntax:
keywords:try,catch,finally,raise

try:
    risky code
except:
     haandling code
---------------------------------------------------
program:
lets write out first program 
try:
    num = int(input("Enter the a number"))
    print(10/num)
except:
    print("Some error occured")
                                   #(Risky code will be inside the try
                                     #if exception occurs -->except execution
-------------------------------------------------------------------
#the above code is not a good practice
# hides the actual problem 
#difficul to deburge
correct code is below:
try:
    num = int(input("Enter the number:"))
    print(10/num)
except ZeroDivisionError:
     print("cannot divide with 0")
except ValueError:
     print("input is not a string")
-----------------------------------------------------------
Common python exception:
1.ZeroDivisionError:divide zero
2.ValueError: wrong data type
3.TypeError:Wrong datatype
4.IndexError: invalid index
5.KeyError  : invalid dictionary key
6.FileNotFoundError : invalid atrributes
7.AttributError    : invalid atrribute
8.NameError:variable is not define
----------------------------------------------
Ex:
try:
    lst = [10,30,50]
    index = int(input("Enter the index:"))
    print(lst[index])
except ImportError:
     print("index error")
except ValueError:
     print("please enter the interger")
else:
     print("No exception")
-----------------------------------------------------
Ex2:another example
try:
    num  = int(input("Enter the input"))
    result = 100/num
except ZeroDivisionError:
     print("Zero")
else:
     print(result)
---------------------------------------
finally block executes always:
used for:
1.closing files
2.closing database
3.cleanup code
try:
      file = open("data.txt")
except FileNotFoundError:
      print("file not found")
finally:
      print("execution completed")
--------------------------------------------------
Ex:

try:
      a = 10/0
      print("")
-------------------------------------------------
#raise:used to manually
#generate exceptions
age = int(input("Enter the age:"))
if age <18:
      raise ValueError("Age should be 18 or greather")
print("Eligible")
--------------------------------------------------
# why custom exception:
class MyException(Exception):
      pass
--------------------------------------
Ex: examle problem for create a own exception and using the own exception:
class INsufficientBalance(Exception):
      pass 
balance = 1000000
withdrawal = int(input("Enter the amount:"))
if withdrawal > balance :
     raise INsufficientBalance("Not enough balance")
print("Withdraw successful")
--------------------------------------------------
'''
#Login System:
class LoginSystem:
      def login(self,username,password):
          try:
                if username !="admin":
                    raise ValueError("Invalid user name :")
                if password != "admin123":
                    raise ValueError("Invalid password :")
                print("Login successful :")
          except ValueError as e:
                print("Error:",e)    
obj = LoginSystem()
username = input("Enter the username :")
password = input("enter the password : ")
obj.login(username,password)
-----------------------------------------------------------------------------
class
class Bank:
      def withdrawal(self,withdrawamount,balance):
          try:
                if(withdrawamount <0):
                     raise InvalidError("invalid input :")
                if(withdrawamount > blance):
                     raise OverError("withdraw amount is greaterthan balance : ")
               

     



    

