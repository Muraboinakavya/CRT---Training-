#TASK24: COUNT THE MULTIPLES OF THE 3
n = int(input())
a = list(map(int,input().split()))
count = 0
for i in a:
     if(i% 3 == 0):
        count = count + 1
print(count,end="")