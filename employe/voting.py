age = int(input("Enter the age : "))
citizen = input("Enter that yes (or) No : ")
voteID =input("Enter that in yrs(or) No")
if(age>=18):
    print("Eligible to vote ")

    if(age>60):
        print("priority voting is Allowed")
else:
     print("Not Eligible")

  