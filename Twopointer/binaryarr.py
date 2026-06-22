#TASK: SORT THE BINARY ARRAY :
arr = [1,0,0,1,1,0,1]
left = 0
rigth = len(arr) -1
for range in range(len(arr)-1):
    if(arr[rigth] != 0):
         left +=1
    else:
        arr[left],arr[rigth] = arr[rigth],arr[left]
print(arr)
