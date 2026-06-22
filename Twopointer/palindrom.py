#TASK PALINDROM :
arr = [15,10,7,5,3,2,1]
arr1 =[1,2,3,5,7,10,15] 
left = 0
rigth = len(arr)-1
while(left<rigth):
    arr[left],arr[rigth] = arr[rigth],arr[left] 
    left +=1
    rigth -=1
print(*arr1)
if(arr==arr1):
    print("palindrom")
else:
     print("not palindrom") 
ALTERNATE APPROACH :
#check an arr is palindrome
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = len(arr)-1
flag = True
while left < right:
    if arr[left] != arr[right]:
        flag = False
        break

    left += 1
    right -= 1

if flag:
    print("palindrome")
else:
    print("not palindrome")