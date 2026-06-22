N = int(input())
a = list(map(int,input().split()))
key_value =int(input())
count = 0
for i in a:
     if(i<key_value):
         count = count+1
print(count)