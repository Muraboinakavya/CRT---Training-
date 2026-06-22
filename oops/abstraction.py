'''what is abstraction?
hidding the internal implementation details
showing the essential feature to the user 
                     (or)
            what operation is done?
            but Not:
             how application is working internally 
---->complexity is hidden from the user 
Why use abstraction?
1.Reduce the complexity
2.Improve the security
3.Better maintenance
4.Cleaner code
5.Standarization
----------------------------------------
Abstraction in python?
python supportsabs using:
abstract classes
abstract methods
-------------------------------
#ABC.-- Module
ABC--Abstract Base Class
Abstract class: it is a blue print of a class we can't create objects directly
define basic common structure:
    abstract can have:
    1.abstract methods
    2.normal method 
#abstraction method:
methods declared but:implementation not provided
child class must implemeent it:
Ex:
vehicle
->start()
#ABC"Abstract base class:
 from abc import ABC,abstractmethod
 #abstract class
class Vehicle(ABC):#Abstract method(to make your method into the abstract method by using the decorated key
#like @abstractmethod)
     def start():
         pass
class Car(Vehicle):
     def start(self):
c1 = Car()
s1.start()
----------------------------------------------
EX2:
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog is sounding")
d1 = Dog()
d1.sound()
-------------------------------------------
#Ex:multiple abstract methods:
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area formula")
    def perimeter(self):
        print("perimeter formula")
r1 = Rectangle()
r1.area()
r1.perimeter()
------------------------------------
#we can create normal method inside the abstract class:
from abc import ABC,abstractmethod
#payment System:
#pay()
class PaymentGateWay(ABC):
    @abstractmethod
    def pay(self):
        pass
class Payment(PaymentGateWay):
     def pay(self):
        print("give me a job")
class PhonePay(PaymentGateWay):
     def pay(self):
         print("phone pay is created")
s1 = Payment()
s1.pay()
s2 = PhonePay()
s2 = PhonePay()
s2.pay()
--------------------------------------------------
#TAsK1:
from abc import ABC,abstractmethod
class PaymentGateWay(ABC):
    @abstractmethod
    def pay(self):
         pass
    def refund(self):
         pass
class CreditCard(PaymentGateWay):
     def pay(self,amount):
        print(f"pay amount :{amount} ")
     def refund(self,amount):
        print(f"refund amount :{amount}")
class UpiPay(PaymentGateWay):
     def pay(self,amount):
         print(f" pay amount :{amount}")
     def refund(self,amount):
        print(f"refund amount :{amount}")
s1 = CreditCard()
s1 = UpiPay()
s1.pay(100000)
s1.refund(50000)
----------------------------------------------------------
TASK2:
from abc import ABC,abstractmethod
class Employe(ABC):
     @abstractmethod
     def calculate_salary(self):
        pass
class FulltimeEmployee(Employe):
     def 
---------------------------------------------------------------
#TASK3:Food deleviry system:
create an abstract class resturant
with methods:
1.prepare_method
2.delivery_time
crete a child class 
1.pizzashop
2.burgar Shop
display:
food preparation time 
delivey time
code:
from abc import ABC,abstractmethod
class Resturant(ABC):
     @abstractmethod
     def prepare(self):
         print("preparing the food")
     def delivery(self):
         print("delivery time")
class pizzashop(Resturant):
     def __init__(self,time):
         self.time = time
     def prepare(self):
         print(f"preparing time :{time}")
class burgarshop(Resturant):
     def
------------------------------------------
Task4:
Ride booking application:
class>Ride
method:
calculate_fare(distance)
child:
1.bikerride
2.CarRide
3.AutoRide
Rules:
bike-->distance*10
auto-->distance*15
car--->distance*20
code:
from abc import ABC,abstractmethod
class Ride(ABC):
     def __init__(self,distance):
         self.time = distance
     @abstractmethod
     def calculate_fare(self):
         pass
class Bikeride(Ride):
     def calculate_fare(self):
         return self.time*10

class CarRide(Ride):
     def calculate_fare(self):
        return self.time*20
class AutoRide(Ride):
     def calculate_fare(self):
         return self.time*15
c1 = Bikeride(50)
c2 = CarRide(50)
c3 = AutoRide(50)
print(c1.calculate_fare())
print(c2.calculate_fare())
print(c3.calculate_fare())
'''
class Number:
     def __init__(self,value):
         self.value = value
     def __add__(self,other):
         return self.value + other.value

n1 = Number(10)
n2 = Number(50)
print(n1+n2)
#--->make your objects work like built in types
#-----> the(__str__) used for strings
class Student:
     def __str__(self):
         return "Student is passed"
s1 = Student()
print(s1)
#-----> the (__len__) used for length calculation
class Team:
     def __len__(self):
         return 5
t1 = Team()
print(len(t1))
#----> the ==(__eq__) this is used for equal operator:
class Student:
     def __init__(self,marks):
         self.marks = marks
     def__eq__(self,value):
         return self.marks == value.marks 
t1 = Student(50)
t2 = Student(90)
print(t1 == t2)
#repr-->offical object representation #debugging #development
class Student:
     def __repr__(self):
         return "hello"
s1 = Student()
print(s1)



          
        


