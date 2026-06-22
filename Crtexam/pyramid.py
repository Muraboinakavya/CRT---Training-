n = int(input("Enter the  N value : "))
for i in range(1,n+1):
    #print(1,i+n)

    for j in range(1,i+n):
        print(" ",end="")

    for k in range(i,n+1):
            print("*",end=" ")
           # print(" ")
    print()
    