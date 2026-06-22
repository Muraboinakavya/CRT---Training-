base_fare = int(input("Enter the base fare : "))
age = int(input("Enter the age : "))
ac = input("Enter that yes(or) no")
festival = input("Enter the yes(or) No")
if(age<12):
     amount = base_fare/2
     print(amount)
elif(age>=12 or age<=59):
     print(base_fare)
elif(age>=60):
     discount = base_fare *40/100
     amount = base_fare - discount
     print(amount)
else:
    print("invalide data")

    if(ac.lower() == "yes"):
    if(festival.lower() == "yes"):
    add = base_fare * 30/100 +  base_fare *10/100
    amount = base_fare +add
     print(amount)
 #if(festival == "yes"):
    # add = base_fare *10/100
    # amount = base_fare + add
    # print(amount)

             

