s1 = int(input("Enter the side1 : "))
s2 = int(input("Enter the side2 : "))
s3 = int(input("Enter the side3 : "))
# If all sides should be equal for eqquilateral
if(s1==s2 and s2==s3 and s1 ==s3):
     print("Equilateral")
     # two sides are equal for isosceles
elif(s1==s2 or s2==s3 or s1==s3 ):
    print("Isosceles")
    # all are sides are different for scalene
else:
    print("scalene")