n = int(input())
arr = list(map(int,input().split()))
k = int(input())
arr.sort()
left = 0
rigth = n-1
pairs = set()
while left < rigth:
    current = arr[left] +arr[rigth]
    if(current == k):
         pairs.add((arr[left],arr[rigth]))
         left +=1
         rigth -=1
    elif current < k:
         left +=1
         
    else:
         rigth -=1
print(len(pairs))