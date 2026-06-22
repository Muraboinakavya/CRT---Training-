# constructor:__init__()
# it is special method which is automatically called when object is created
# used: intializing the object data
# # Ex:
# class Student:
#      def __init__(self):
#          print("Constructor is called")
# s1 = Student()
# #--------------------------------------------
# # Flow of the :
# Student()
# |
# object()creation
# |
# __init__automatically called
# #---------------------------------------------
# if no constructor:
#     if yes
#     automatically
# Ex:
# class Student:
#     pass
# s1 = Student()
# s1.name = "kavya"
# s1.branch = "AI"
# -----------------------------------------
#With constuctor: 
# class Student1:
#     def __init__(self):# self refers to current object
#         self.name = "kavya"
#         self.branch = "AI"
# s1 = Student1()
# print(s1.name) # the variable in the constructor  is access by using the object name and (.) dout operation
# print(s1.branch)# self is used to intialize the data:
#--------------------------------------------
#constuctor with parameters:
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# obj2 = Student("mehar",19)
# print(obj2.name)
# print(obj2.age)
#----------------------------------
# # flow  for the above code:
# self --> obj2
# name:"vijaya"
# age : 20

# obj2_______
# name = "vijaya"
# age = 20
#----------------------------------

# #step by step:
# 1. object memory allocated
# 2. init is automatiaclly 
# 3. self pointes to object
# 4.variables intilialized
# 5. object  returned 
#-----------------------------------
# #default constructor:
#  class Test:
#      def __init__(self):# self is not a reserved keyword the (self is a convention)
#          print("Default constructor")
# s1 = Test()
# ------------------------------------------
# # parametrized constructor:
# class Test:
#      def __init__(self,x):# self is not a reserved keyword
#         self.X = 100
#         print("Default constructor")
# s1 = Test()
# #----------------------------------------------------
# # Difference between  constuctor and normal method:
# ----------------------------------------------------------------
# constructor                    |            Normal method
# ------------------------------------------------------------------
# automatically called           |          manually call it 
# name fixed: __init___          |          any name
# used for intialization         |       used for operations
# executes during object         |        executess when called
# -----------------------------------------------------------------
# class Student:
#     def __init__(self):
#         print("constructor")
#     #normal method
#     def display(self):
#         print("normal method")
# c1 = Student()
# c1.display()# this acces the normal method
#----------------------------------------------------------
'''
Instance variable:
 variables that belong to an object separate copy created dor every object
 They store:
 object - specific data

Student | Name     | Marks
s1       vijaya      98
s2       rajesh      99
 
 each object store it's own data
 '''
#-----------------------------------
#Instance method:
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
#instance method 
    def display(self):
         print(self.name)
         print(self.marks)
s1 = Student("Rajesh",93)
s1.display()
'''
------------------------------------
flow of the instance methods:
s1.display()
|
Student.display(self)
|
self---->s1
---------------------------------------
#Dynamic object properties adding the variables dynamically
After creting object
Ex: 

class Student:
     pass
s1 = Student()
s1.name = "kavya"
s1.marks = 90
print(s1.name)
-----------------------------
# Class variable:
#class variable shared among the all  objects
class  Student:
    #class variable
     collage_name = "CITY"
     def __init__(self,branch):
        #instance variable
        self.branch = branch
    # Normal Method
     def display(self):
         print(self.college_name)
s1 = Student("cse")
s2 = Student("ai")
print(s1.collage_name)
print(s2.branch)
EX:
                        student class(---->class name)
                        ---------------
                          collage = "kavya"(class variable share among all objects  in the class)(--->class variable)
                        -------------------------
                          |      |      |
                          s1     s2     s3
------------------------------------------------
self : self refer to current object
              (or)
reference variable pointing to current object
-------------------------------------------------------

class Student:
     def show(self):
         print(self)
s1 = Student()
s2 = Student()
print(s1)
print(s2)
s2.show()
------------------------------------------------------
#using object
class employee:
    company = "google"
    def display(self):
        self.company = company
        print(self.company)
e = employee()
two ways access:
print(e.company)

-----------------------------
#no object use
print(employee.company)
-----------------------------------
#class methods:
work with class variaables operate on class  level data
@classmethod--------->decorator
--------------------------------
Ex: this is for the example for the class variable,class methods
class Student:
    collage = "CITY"
    @classmethod
    def show_college(cls):
         print(cls.collage)
Student.show_college()
------------------------------
@classmethod:
decorator which tells python:
this method belongs to class not object
self--->current object
cls--->current class
---------------------------------
#EX : create a class and class variable and class methods
class Employee:
     employe_name = "kavya"
     @classmethod
     def company_name(cls):
        print(cls.employe_name)
s1 = Employee()
s2 = Employee()
s1.company_name()
s2.company_name
------------------------------------------------------------
Ex: update the data  (or) modify the varibles in class
class Employee():
    var_name = "mehar"
    @classmethod
    def company_name(cls,new_name):
        cls.var_name = new_name

Employee.company_name("google")
print(Employee.var_name)
----------------------------------------------------------
diff btw instance methods and class methods:
       instance methods:                            class method:
---> works on  the object data                    works on the class data
--->uses (self)                                      uses (cls)
---->need object                                     directly use class
---->acess the instance variable                       access the class variables
-----------------------------------------------------------------------------
Ex: write a code by using the both instance methods and class methods:
class Student:
     #instance methods:refers to the object
    def instance_methods(self):
         print("Instance method")
    # class methods: refers to the class
    @classmethod
    def class_method(cls):
         print("class method")
-------------------------------------------------------------
#Static Method:
--->static method does not uses objects and class
# it is independent method
#logically belongs to class but no data requires from class
They Are:
--->utility/helper method
-->NOt uses:self,cls:
EX1:
add()
multiply()
@staticmethod--->decorator
#static method Example:
class Calculator:
     @staticmethod  # helper method
     def add(a,b):
         return a+b
print(Calculator.add(10,20))
EX2:
class Message:
    @staticmethod:
    def greet():
         print("hello sir")
print(Message.great())
------------------------------------------------

FINAL TASK:

class Student:
    class_name = "kavya"
    age = 10
    def __init__(self):
        self.friend = friend
        self.branch = "ai"
    def instance_methods(self):
         print(self.friend)
         print(self.branch)
    @classmethod
    def class_method(cls):
        print(cls.class_name)
        print(cls.age)
    def greet():
         print("hello sir")
Student.greet()
Student.class_method()
s1 = Student("kavya")
s1.instance_methods()
'''



         


   






