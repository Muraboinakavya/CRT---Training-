#TAsk: Find the equilibrium index using index using prefix:
#bruteforce approach:
# arr = [2,4,1,7,3,5]
# #left 0 
# #rigth = 0
# sum1 = arr[2:]
# sum2 = arr[:2]
# for i in range(0,len(arr)):
#      sum1 = arr[0] + arr[1]
#      sum2 = arr[-2] + arr[-1]
#      if(sum1 == sum2):
#  print("equilibrium index " ,arr[2,-2])
 #BY using the prefix approach:
arr = [1,3,5,2,2]
n = len(arr)
prefix =[0]*n
prefix[0] = arr[0]
for i in range(1,n):
    prefix[i]= prefix[i-1]+arr[i]
total = prefix[n-1]

for i in range(n):
    if i==0:
        left=0
    else:
        left=prefix[i-1]

    right=total-prefix[i]

    if left==right:
        print("Equilibrium Index =",i)
        break


