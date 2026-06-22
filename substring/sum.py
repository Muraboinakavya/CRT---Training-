# FIND THE FIRST CONTINUES SUB ARRAY WHOS SUM ID EQULAS TO  TARGET VALUE:
# arr = [1,4,20,3,10,5]
# target = 33
# for i in range(0,len(arr)):
#     sum = 0
#     for j in range(i,len(arr)):
#         sum = sum + arr[j] 
# #print(sum)
#         if(sum == target):
#             print(arr[i:j+1])
# #SLIding WINDOW FOR THE ABOVE PROBLEM :
# arr = [1,4,20,3,10,5]
# target = 33
# for i in range(0,len(arr)):
#      sum = 0
#      for j in range(i,len(arr)):
#          sum = sum+arr[i]
# TASK: OPTIMAl SOLUTION IN BY USING TWO POINTERS AND SLIDING:
#n = int(input(6))
arr = [1,4,20,3,10,5]
target = 33
left = 0
rigth = 0
sum =0
for rigth in range(0,len(arr)):
    sum = sum+arr[rigth]
    while(sum>target):
        sum = sum - arr[left]
        left = left+1
    if(sum==target):
         print(arr[left:rigth+1])
         break
        

         
     

     
     
