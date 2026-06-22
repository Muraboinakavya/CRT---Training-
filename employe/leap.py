# write the program of leap year
# the conditions are 
# 1. divisible by 400 or 4
# 2.should not  divisibly by 100
year = int(input("Enter the year : "))
if(year % 400 ==0) :
    if(year % 100 != 0) :
         print("year is a leap year : ",year)
    else:
        print(" not divisible by 100")
        print("not a leap year")
else:
    print("not a leap year")       