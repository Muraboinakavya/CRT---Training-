#TASK: REVERSE THE LIST BY USING TWO POINTERS APPROACH 
arr =[1,2,3,5,7,10,15] 
left = 0
rigth = len(arr)-1
while(left<rigth):
    arr[left],arr[rigth] = arr[rigth],arr[left] 
    left +=1
    rigth -=1
print(*arr)