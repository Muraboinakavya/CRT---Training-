'''#TASK1:REVERSE TRIANLE:
n = int(input("Enter the n value : "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
#--------------------------------------------
#TASK2:Diamond star pattern:
n = int(input())

mid = n // 2

# Upper Half
for i in range(mid + 1):

    for j in range(mid - i):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()

# Lower Half
for i in range(mid - 1, -1, -1):

    for j in range(mid - i):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()
------------------------------------------------
#TASK3:Octaal to decimal conversion:
num = input()
decimal = 0
power = 0
for i in num[::-1]:
     decimal += int(i) *(8**power)
     power +=1
print(decimal)
------------------------------------------------------------
#TASK4:
