'''Decorators:
adds the extra functionality without changing the original function 
Gift Wrapper:
 wrapper adds:
 extra layer ,beauty
 decorators = wrapper around the function 
 # Why decorators are needed?
 logging:
 authentication,
 timing
 validation
 #---> if no decorators
 1.repeated computed
 2.messy program
 example:
 
def greet():
    print("hello students")
x = greet
x()
# In python -- functions are
# treated like variables
------------------------
# nested functions:
def outer():
    def inner():
         print("Inside side")
    inner()
outer()
-------------------------
#returning the function inside the function:
#returing the function
def outer():
    def inner():
        print("inner side")
    return inner
x = outer
outer
|
returns the inner
|
stored in x
|
x()

#------------------------------------
#simple decorators
def decorators_function(original_function):
    def wrapper():
        print("------------")
        original_function()
        print("************")
    return wrapper

#original function
def greet():
    print("hello nigar")

#apply manually
decorated = decorators_function(greet)
decorated()
'''

#------------------------------------(by using the (@) special character)
#EXAMPLE2:
# def smart_divide(func):
#     def wrapper():
#         print("before checking the division ")
#         func()
#         print("Division is completed :")
#     return wrapper 
# @smart_divide
# def divide():
#      print(10/2)
# divide()
# --------------------------------(brute force method(kavya creation))
# print("before the division :")
# result = 10/2
# print(result)
# print("After the division ")
#-------------------------------
#Task: login checking problem:
def login_required(func):
    def wrapper():
        print("checking the user login ")
        func()
    return wrapper
@login_required
def dashboard():
     print("Welcome to dashboard")
dashboard()
