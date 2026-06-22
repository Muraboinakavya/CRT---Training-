experience = int(input("enter the experience :" ))
salary = int (input("enter the salary :"))

if experience>=5:
   if salary<30000 :
         bonus = salary *20/100
         finalsalary = salary + bonus
         print("Bonus = ",bonus)
         print("final salary = ",finalsalary)
   elif salary>=30000 and salary <=50000:
         bonus = salary *15/100
         finalsalary = salary +bonus
         print("Bonus = ",bonus)
         print("final salary = ",finalsalary)
   elif salary>50000:
         bonus = salary *10/100
         finalsalary = salary + bonus
         print("Bonus = ",bonus)
         print("final salary = ",finalsalary)
             
else:
   bonus = salary*5/100
   finalsalary = salary + bonus
   print("Bonus : ",bonus)
   print("finalsalary : ",finalsalary)
     