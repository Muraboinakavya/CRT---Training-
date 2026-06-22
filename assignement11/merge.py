n1 = int(input())
a = list(map(int,input().split()))
n2 = int(input())
b = list(map(int,input().split()))
i = 0
j = 0
result =[]
while(i<n1 and j<n2):
    if(a[i]<= b[j]):
        result.append(a[i])
        i+=1
    else:
         result.append(b[j])
         j+=1
while(i<n1):
     result.append(a[i])
while(j<n2):
     result.append(b[j])
print(*result)
     
