#Task: find the elements  in between the particular range:
# arr = list(map(int,input().split()))
# L = int(input())
# R = int(input())
# n = len(arr)
# print(arr[L:R])
arr = list(map(int,input().split()))
n = len(arr)
prefix = [0]*n
prefix = arr[0]
for i in range(1,n):
     prefix[i] = prefix[i-1] +prefix[i]
print(arr[prefix])