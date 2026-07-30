n = int(input())
arr = list(map(int,input().split()))
maximum = max(arr)
minimum = arr[0]
result = (maximum - minimum)
print(result)