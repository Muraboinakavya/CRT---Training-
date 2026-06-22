'''Method Overriding:
Redefining a parent class method inside the child class
--->same method name
---> same parameters
child class method changes the behaviour of parent class method 
Ex:
class Animal:
     def sound(self):
         print("Animal Makes sound")

class Dog(Animal):
     def sound(self):
         print("Dog Barks")
d1 = Dog()
d1.sound()
------------------------------------------------
Important rule:Method name is same
super():super function
-----------------------------------------------
Is it overriding on the constructor?
 yes
 EX:
 by using the 
class Parent:
     def __init__(self):
          print("parent construuctor")
class Child(Parent):
      def __init__(self):
        super.__init__()
         print("child constructor")
s1 = 
INTERVIEW : MRO: method resolution order 
order in which python searches methods
'''
class A:
     def show(self):
         pass 
class B(A):
      pass 
class C (A):
     pass
class D(B,c):
     pass 
d1 = D()
d1.show()
print(D.mro)