# a = [2,1,5,1,3,2]
# n = int(input())
# max = a[0]
# for i in range(len(a)-n+1):
#     current_sum = 0
#     for j in range(i,i+n):# 
#         current_sum = current_sum + a[j]
# print(current_sum)
#     if(current_sum>max):
#         max = current_sum
# print(max)
#SLIDING WINDOW APPROACH :formula----> (Previous_sum+(-outgoing)+incoming)
arr = [2,1,5,1,3,2]
k=3
window_sum = sum(arr[ :k])
max_sum = window_sum
for i in range(k,len(arr)):
    outgoing = arr[i -k]
    incoming = arr[i]
    window_sum = window_sum - outgoing + incoming 
    max_sum = max(max_sum,window_sum) 
print(max_sum)

num = int(input())
arr = map(int,input().split())
k = 3
for i in rang(arr[:3])

  

         
     
