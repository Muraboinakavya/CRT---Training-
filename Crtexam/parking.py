time = int(input("Enter the hours of the  parking : "))
if(time<=2):
    pay = time*30
    print("the first payment : ",pay)
if(time>=3 and time<=5):
    pay = time*50
    print("the first payment : ",pay)
if(time>5):
    pay = time*80
    print("the first payment :" ,pay)
if(pay>500):
    maintenance = pay *15/100
    pay = pay+maintenance
    print("the maintenance:", pay)
if(time<=1):
    discount = pay-20
    print("final amount",discount)
