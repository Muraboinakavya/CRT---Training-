balance = 6000
correct_pin =2915
pin = int(input("enter the pin : "))
if(pin == correct_pin) :
     amount = int(input("Enter  the amount to withdrawal :"))


     if(balance>=amount):
          remaining_balance = balance - amount
          print("Transaction successful")
          #remaining_balance = balance - amount
          print("Remaining balance : ",remaining_balance)
          
     else:
          print("insufficient ")
     
else:
     print("invalid pin")