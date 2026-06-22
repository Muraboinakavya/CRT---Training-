'''
variable scope: there are two types of the variable scope
1.Local scope:inside the function
EX:

def show():
   x = 100
   print(x)
show()
'''
#2.Global scope:out side the function:
# x = 29
# def show():
#     global x
#     x = x+5
# show()
# print(x)
# accessing the local variable outside the function:
# x = 0
# def update()
#     x = x+5
# update()
# print(x)
#TASK: create a function bank_transcation ()
# which accepts:
# 1.account holder
# 2.balance
# 3.transcation type(deposit/withdrawal)
# 4.amount
def bank_transcation(name = "kavya"):
    balance = int(input("enter the balanced : "))
    type = input("enter the type :")
    if(type == "deposite"):
        depo = int(input("enter the amount :"))
        de = balance + deposit
        print(de)
    elif(type == "withdrawal"):
        if withdrawal>balance:
            print("invalid sufficient balance")

    else:
        withdrawal = int(input(" enter the withdrawel: "))
        final = balance - withdrawal
        print(final)
bank_transcation()
    


     