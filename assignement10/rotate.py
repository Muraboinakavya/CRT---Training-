N = int(input())
a = list(map(int,input().split()))
k = int(input())
for i in a :
      k = k% N 
      rotated = a[-k:]+a[:-k]# in this the a[-k:]--> this means the array start from (-2,-1) and also the a[:-k]this means takes the all element before the(-2,-1)
print(rotated)
         
