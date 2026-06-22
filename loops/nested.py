# i = 1
# while(i<=3):
#     j=1
#     while(j<=2):
#         print(i,j)
#         j = j+1
#     i = i+1
# i = 1
#  for i in range(1,5):
#      j = 1
#     for j in range(1,5):
#         print("*", end="")
#     print()
n = int(input("Enter the  value :"))
for i in range(1,n+1):
    if(i%2==0):
         print(str(i)*i)
    for j in range(1,i+1):
        print(j,end=" ")
    print()
        



    
