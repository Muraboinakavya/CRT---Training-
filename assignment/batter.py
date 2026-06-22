battery = int(input("Enter the battery of the mobile: "))
usage = int(input("Enter the usage of the battery : "))
Hours =0
#if(battery>0):

   # while(battery<=20):

battery = battery-usage
while(battery>20):
     battery = battery-usage
     Hours = Hours+1
print("Hours : ",Hours)
print("battery : ",battery)
