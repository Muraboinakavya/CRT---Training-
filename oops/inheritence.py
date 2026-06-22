'''
what is inheritance?
it is a mechanism where one class acquires the properties and methods of another class with  the specific relation
                                    (or)
one class reuses the  features of the 

a child class can 
use variables 
use methods of parent class without rewitting the code
--------------------------------------------------- 
Advantages or why ?
1. code reusability
2.reducing the code duplication 
3.better organization of code
4.easy maintenance
Terms : 
parent:super class
child : sub class/derived class
-------------------------------------------
flow be like:
      parent
         |
       child 
--------------------------------------------
Syntax:
class Parent:
     pass
class Child(Parent):
     pass
-----------------------------------------
Ex:
class Animal:# parent class
     def eat(self):
         print("Animal is eating")
class Dog(Animal):
      pass
d1 = Dog()
d1.eat()
flow of the  above program:
Dog class does not contains eat()
              |
    python searches in animal class
              |
    method is found and executed 
---------------------------------------------------
without inheritance:class Animal:# parent class
     def eat(self):
         print("Animal is eating")
class cat:
    def eat(self):
        print("Animaal is eating")
with inheritance:
class Animal:# parent class
     def eat(self):
         print("Animal is eating")
class Dog(Animal):
      pass
class cat(Animal):
       pass
c1 = Cat()# we will create the object for the grand child class not create the object for the parent class:
c1.eat()
-----------------------------------------------------------------------------------------------
Accessing the parent variable  to the class:

class Person:
     def __init__(self,name):
         self.name = name
class Student(Person):
     pass
c1 = Student("kavya")
print(c1.name)
--------------------------------------------------------
Types of inheritance:
1.single inheritance :one parent class and one child class
                parent
                  |
                child
Ex:
class Animal:# parent class
     def eat(self):
         print("Animal is eating")
class Dog(Animal):
       def bark(self):
           print("Barking")
d1 = Dog()
d1.eat()
d1.bark()
2.Multiple inheritence:
one child class inherits the multiple parent class
                parent1         parent2
                    \              / 
                        child
EX:
class Father:
     def money(self):
          print("father money")
class Mother:
      def gold(self):
          print("mother's gold")
class Child(Father,Mother):
     pass
c1 = Child()
c1.gold()
c1.money()
3.Multilevel inheritence:
Inheritence chain of multiple levels:
            
            Grand parent 
                |
             parent
               |
            child
Ex:
class Grandparent:
     def house(self):
         print("Grand parent home")
class Parent:
     def car(self):
        print("parent car")
class Child(Grandparent,Parent):
       def Bike(self):
          print("child's bike")
s1 = Child()
s1.house()
s1.car()
s1.Bike()
4.Hierarichal inheritance:
mutiple child class inherit from the single parent class:
                        
                        parent
                      /      \ 
                    child1    child2
Ex:
class Animal:
     def eat(self):
         print(:Eating)
class dog(Animal):
     def bark(self):
         print("barking")
class cat(Animal):
     def meom(self):
         print("meom")
5.hybrid   inheritance
two or more inheritance types
hierarichal  and multiple

                    A
                   /  \
                  B    C
                  \   /
                     D
#example:
class A:
    def show_a(self):
        print("class A")
class B(A):
    def show_b(self):
        print("class B")
class C(A):
    def show_c(self):
        print("class C")
class D(B,C):
    def show_d(self):
        print("class D")
d1 = D()
d1.show_a()
d1.show_b()
d1.show_c()
d1.show_d()
-------------------------------------------------------------

#check the inheritence:
class Animal:
     pass
class Dog(Animal):
      pass
c1 =Dog()
print(issubclass(Dog,Animal))
print(isinstance(c1,Dog))
#----> the constructor properties is  inherit by the child class
-----------------------------------------------------
problem1:
class Animal:
      def sound(self):
          print("Animal Makes sound")
class Dog(Animal):
     pass
c1 = Dog()
c1.sound()
---------------------------------------------------
#problem2:
class College:
     collage_name ="CITY"
class Student(College):
      def __init__(self):
           self.student_name = "kavya"
c1 = Student()
print(c1.collage_name)
print(c1.student_name)
--------------------------------------------------
#problem3:
class Vehicle:
      def start(self):
          print("car") 
class Car(Vehicle):
       pass

class Sportscar(Car):
      def speed(self):
           pass
c1 = Sportscar()
c1.start()
c1.speed()
problem4:crate a class programmer with method coding() and class designer with method designing()
class Programmer:
      def coding(self):
           print("Start coding")
class Desiginer:
       def desiging(self):
           print("hoo")
class Employee(Desiginer,Programmer):
      pass
e1 = Employee()
e1.coding()
e1.desiging()

    if role == "Developer":
        emp = Developer(name,salary)
    elif role == "Manager":
        emp = Manager(name,salary)
employees.append((role,emp))

for role,emp in employees:
    print(f"Name:{emp.name}")
    print(f"Role:{role}")
    print(f"Bonus:{emp.calculate_bonus}")
    print()
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def calculate_bonus(self):
        return 0
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary *0.35
n = int(input())
employees = []
for _ in range(n):
    role,name,salary = input().split()
    salary = int(salary)
#practice one
class Employee:
      def __init__(self,name,salary):
           self.name = name
           self.salary = salary
      def boun(self):
           pass
class Developer(Employee):
       def devboun(self,bouns,type):
           if type =="Developer":
               bonus = (salary *20)/100
               print(f"the salary for developer by adding bonus is : ",{bonus})
class Manager(Employee):
         def manboun(self,type,boun):
              if type =="Manager":
                  bonus = (salary*35)/100
                  print(f"the salary for manager by adding bonus is : ",{bonus})
s1 = Employee()
n = int(input())
name = input()
type = input("Enter the type in between developer (or) manager ")
salary = int(input())
online course Access System an online learning platform 
'''
class Course:
      def __init__(self,student_name):
           self.student_name = student_name
      def access_level(self):
           return "No Access"
class Free_course(Course):
      def access_level(self):
           return "Limited Access"
class Premium(Course):
       def access_level(self):
           return "Full Access"
n = int(input())
student = []
for _ in range(n):
      course_type,name = input().split()
      if course_type == "Free":
          student = Free_course(name)#object creation
      elif course_type == "Premium":
            student = Premium(name)
students.append((course_type,name))
for course_type,student in students:
      print(f"student:{student.student_name}")
      print(f"course_type:{student.course_type}")
      print(f"student:{student.access_level}")


          
 




      

