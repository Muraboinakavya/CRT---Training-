#Task: move the zeroes to the end of the list :
arr = [1,0,4,-2,0]
left =0
for rigth in range(len(arr)):
     if(arr[rigth] != 0):
         arr[left],arr[rigth] = arr[rigth],arr[left]
         left +=1
print(arr)