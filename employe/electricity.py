units = int(input("Enter the electricity bill  units: "))
if units<=100:
    surcharge = units*2
    finalbill = units+surcharge
    print("Electricity = ",finalbill)
    print("surcharge Applied = ",surcharge)
elif units <=200 :
    surcharge = units*5
    finalbill = units+surcharge
    print("Electricity = ",finalbill)
    print("surcharge Applied = ",surcharge)
elif  units>300:
    surcharge = units *10/100
    totalbill = units + surcharge
    print("Electricity Bill = ", totalbill)
    print("surcharge Applied = ",surcharge)
else :
     print("invalid")

    