# for i in range(6,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()
# N = int(input("Enter the N value"))
# for i in range(N):
#     for j in range(N,i,-1):
#          print(i, end="")
#     print()
     # EXAMPLE -7
     
    #  A
    #  B C 
    #  D E F 
    #  G H I J
#ch = 65
#print(char(ch))
# n = int(input("enter the n value:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(ch), end="")
#         ch =ch+1

#     print()     
# EXAMPLE -8
# 1
# 1 3 
# 1 3 5
# 1  3 5 7
for i in range(1,5):
    for j in range(1,i+1):
        odd = 2*j - 1
        print(odd ,end="")
    print()
