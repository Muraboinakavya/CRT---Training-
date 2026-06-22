--->THe below is a palindrom problem by using the slicing
#
 name = "kavya"
# reverse =(name[::-1])
# if(name==(reverse)):
#      print("the given string is a palindrom")
# else:
#      print("the given string is a not a palindrom")
----->The below is a palindrom problem  without using the slicing
name ="kavya"
reverse = ""
for var in range(len(name)-1,-1,-1):
    reverse = reverse + var
    print(reverse)
if(name==reverse):
     print("the given string is a palindrom")
else:
     print("the given string is a not a palindrom")
