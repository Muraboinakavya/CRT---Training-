'''what is polymorphism?
poly--->many
morphism--->forms 
same method/operators will behave different
Ex:
print(5 + 3)#8
print("Hello"+"world")#Helloworld 
                 
                 same opertor 
                     |
                but diff behaviours 
Types of polymorphissm?
1. complie polymorphism 
2.run time poiymorphism
#complie polymorphism: methos overloading
No method overloading in python 
----------------------------------------------------------------
Method overloading: the method overloading is not directly supported by the python but we can achevieve by using
(args)---->variable length aruguments and default arguments
same method names
     +
different parameters
python approach:
class Calculator:
      def add(self,a,b,c=0):
          print(a+b+c)
c1 = Calculator()
c1.add(10,20)
c1.add(10,20,30)
2.Run time polymorphism:
--->method overriding:
'''
class Bird:
     def fly(self):
         print("Bird Flying")
class Eagle(Bird):
      def fly(self):
         print("Eagle is flying")
c1 = Eagle()
#method is  choosen during run time:
c1.fly()
---------------------------------------
Important:
'''
DUCK TYPING in python:
python focuses on behaviour not object type

'''
class Duck:
    def sound(self):
        print("Quack")
class Dog():
    def Bark(self):
        print("Dog will Bark")
def make_sound(obj):
    obj.sound()
d1 = Duck()
d2 = Dog()
make_sound(d1)
make_sound(d2)
