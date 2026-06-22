#Task: FINND THE GREATEST NUMBER  WHEN COMPARe WITH PREVIOUS ELEMENT:
n = int(input())
a = list(map(int,input().split()))
#pre = a[0]
for i in range(1,n):
    if(a[i] > a[i-1]):
         print(a[i],end=" ")