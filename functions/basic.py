'''
 what is a function?
 function is a block of reusuable code.performs specific task
why functions?
1. avoid repetition
2. improves readability
3. easy debug
4. modular programming

# function definition
def function_name(parameters):
    """Doc strings"""
    statements
    return value
    
    def---> it is a keyword to define the function
    function_name--> identifiers
    parameters--> input to the function
    return---> output

# function calling: excuting the code

function_name()

functions are two types
            1. bulit in functions 
            2. user defined functions
1. bulit in function : which are already defined 
ex : print()
input() sum() mean() max()
2. user define functions : we will create our own logic as per our requirement

# parameters : passed during the function definition

types of aruguments:
1. positional aruguments:

ex : def multiply(a,b)
        return a*b
call the function
multiply(2,3) 
2. keyword aruguments :
ex: def sub(a,b):
        return a-b
sub(b=5,a=10)


3. default aruguments: used by value is not provided
ex 
def student(name = "manish"):
    print(f"student name is {name}")
student()

4. variable lenght aruguments : 
ex : 
def total(*args):
    print(args)
total(10,20,30,40)

5. keyword  variable length aruguments kwargs 
ex:
def student_details(**kwargs):
    print(kwargs)
student_details(name = "vijaya",branch = "CSE",rollno = "77")

return statement : send the value back to the caller
ex :
def add(a,b):
    return a+b
    result= add(10,20)
    print(result)
    
    print                                           return
    display the output                          sends the value 
    cannot reuse                                    can reuse
    
multiple return values:
def calculate(a,b):
    return a+b.a-b,a/b

format : tuple 
s,sub,div = calculate(20,30)

Doc strings describes:
1. what function does:
2. parameter 
3. return values

ex 
def add(a,b)
    """this function adds two numbers and return result"""
    result = a+b
print(add._d_)
help(help(add))

variable scopes:
#1. local scope:
variables declared inside the function 
ex: 
def test():
    x = 100
    print(x)
test()

2. global scope:
variable declared outside the function
ex:
x = 200 # global variable
def show():
    print(x)
show()
# accessing the local variable outside the function
ex:
x = 0
def update():
    global x
    x = x+5
update()
    
    
'''
# create a function 
def hello():
    print("hello world")
#call the function 
hello()

# parameters 
def add(a,b): # a,b are parameters
    print(a+b)
# calling the function
# arguments = values passed during the function call
add(2,3) # 2, 3 --- aruguments 
# task : create a function to calculate simple interest using positional arguments


# keyword aruguments 
# call the simple interest function using key word aruguments
#def simple_interest(a,b):
    #print()

# task: create a function to calculate squares by default parameters
def squares(num,power=2):
    print(num**power)
squares(8)

# task: create a function to find sum of any num of values
'''def sum(*args):
    print(*args)
    print(sum(args))
sum(2,4,5,6)
'''
def student_details(**kwargs):
    print(kwargs)
student_details(name = "vijaya",branch = "CSE",rollno = "77")
 # create a function to print employee details using kwargs
def employee_details(**kwargs):
    print(kwargs)
employee_details(name = "vijaya",age = "21",salary = "10000")
# task : write a function where variable length aruguments and keyword length aruguments
def together(*args,**kwargs):
    print(args,kwargs)
together(10,20,name = "vijay")

# task: create a function that returns multiple values min , max, avg of the numbers
'''
def calculate(a,b):
    return max(),min(),avg()
s,m,t = calculate(10,20,30,57)
print(10,20,30,57)
'''
# task: write a docstring for the simple interest program
x = 0
def update():
    global x
    x = x+5
update()
print(x)
'''
# create a function bank_transaction()
# which accepts the 
1. account holder(string)
2. balance
3. transaction_type(deposit/withdraw)
4. amount
'''
'''
def bank_transaction(account_holder,transaction_type ,amount):
    global balance 
    if transaction_type == "'deposit":
        balance += amount
        print(f"{account_holder} deposited{amount}")
    elif transaction_type =="withdraw":
        if amount <= balance:
            balance -= amount
            print(f"{account_holder} withdraw{amount}")
        else:
            print("Insufficient balance for {account_holder}")
    else:
        print("invalid transaction_type")
    print(f"updated balance {balance}")
    return balance

bank_transaction("vijaya","deposit",500)
'''

''''
lamda function: is a small and anonymous function
# function without name 
# defined using lambda
can pass any number of aruguments
can have only expression
returns the value automatically (no return keyword)
normal function:
def add(a,b):
    return a+b
# write using lambda 
add = lambda a,b: a+b
#calling the function 
add(10,20)

'''
# write a normal function to square of num
#convert the normal function to lambda 
#max number in 2
# c - programing 
#ternary : a if a> else b

'''
arr = list(map(int,input().split()))
#map(): applies the function to each element of iterable
map(function,iterable)
ex:
def square():
    return x*X
nums = [1,2,3,4]
result = map(square,num)
print(result)

'''

'''
what is fliter?
selects the element based upon the condition
syntax:
fliter(function,iteration)
ex 
def is_even(x):
    return x%2 ==0
list = [1,2,3,4,5]
result = fliter(is_even ,list)
print(result)
'''
# task: given with a list with frds names
#fliter the names letter starting with A
names = ["Anu","Amit","Rajesh"]
result = list(Fliter(lambda x:x.startswith("A")))
print()

''''
what is reduce()?
repeatedly applies function
reduces the iterable to single value 
syntax:

functools---> module
'''
from functools import reduce
nums = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,nums)
print(result)
#TASK:create a function to find the sum of the any numners of values:
#Task:employe detailes using the kwargs:
# def employe_details(**kwargs):
#      print(kwargs)
# employe_details(name = "kavya",branch = "ai",roll = 52)
#TASK:write args and kwargs together:
def student(*args):
    print("student data : ",args)
def employe(**kwargs):
    print("employe detailes",kwargs)
student(10,20,30)
employe(name = "kavya",branch ="ai")
#TASK: CREATE A FUNCTION THAT RETURN MIN,MAX,AVERAGE OF THE NUMBERS:
def numbers(a=10,b=20,c=30,d=40):
    n = 4
    minimum = min(a,b,c,d)
    print("mini",minimum)
    maximum = max(a,b,c,d)
    print(maximum)
    total = a+b+c+d
    avg = total/n
    print("average",avg)
numbers()