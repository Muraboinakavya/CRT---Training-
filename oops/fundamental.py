'''
OOPS : object oriented programming system(paradiagm)
programs are organized using objects
objects contains:
1.data(variable)
2.behaviour(functions/methods)
--->OOP not only focuses on functions but also real world entities
car-->object
student--->
--------------------
each object here:
will have properties and actions
             |              |
                             
                            (methods)

         (variable)
-----------------------------
Earlier the programming  was written withour OOPs
1.difficult to message the large level
2.code duplicates
3.less security
4.difficult maintenance
OOPS: slove the above problem:
1.classes
2.objects
3.encapsulation
4.abstraction
5.polymorphism
6.inheritance
------------------------------------
#procedural programming
name = "kavya"
marks = 90
def display()
    print(name,marks)
display()
---------------------------------
OOPS APPROACH:
class Student:
     def__init__(self,name,marks)
         self.name = name
         self.marks = marks
    def display(self):
         print(self.name,self.marks)
#object
s1 = Student("kavya" ,69)
s1.display()
-------------------------------
# data +functions--->
advantages:
1.code reusability
2.better organization - modular  and structure
3.security->encapsulation
4.Easy maintenance :  to,update,debug
5.real world modelling
6.scalability: large application 
-----------------------------------
#class: a class is a blueprint of an object(or)collection  of variable and methods
blue print : can be used to build many houses
Syntax: for class
class Class:
     pass
class: is a keyword creates class 
class name:identifiers
pass: empty block
------------------------------------
#Object: Instance of a class(or) actual memory representation of class
syntax:
class Student:
     pass
#object creation:
 obj = Student()
 print(obj)
   
obj---> instance name (object)
Student--->class name
example:
class Car:
     brand = "Audi"
     #Method
     def start(self):# (self) refers to the current object
         print("Car started")
#create the objects: there is different memory allocation for each objects in the same class
c1 = Car()
c2 = Car()
print(c1,c2)
c1.start()# metod call
# we can use(.) to call the object like(c1.start())
--------------------------------------------------------------------
#TASK:create a class named as employe
'''
class Employe:
    company = "kavya"
    employe = "vasu"
    def CEo(self):
        print("hello")
    def work(self):
            print("hi")
a = Employe()
b =Employe()
print(a.company)
print(b.employe)
a.CEo()
b.work()


       


