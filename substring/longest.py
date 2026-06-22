#TASK 3: FIND THE LENGTH of Longest continuous subarray tha contains no repetaded elements:
#BRUTE FORCE METHOD:
# arr = [1,2,3,1,2,3,4]
# #length = 0
# #rigth = 0
# #count =0
# max_length = 0
# for i in range(0,len(arr)):
#     unique = set()
#     for j in range(i,len(arr())):
#          if arr[j] in unique:
#              break
#         unique.add(arr[j])
#         length = j-i+1
#         max_length = max(max_length,length)
# print(max_length)
#BY USING THE SLIDING APPROACH :
arr = [1,2,3,1,2,3,4]
max_length = 0
left = 0
rigth = 0
unique =set()
for rigth in range(0,len(arr)):
     while arr[rigth] in unique:
         unique.remove(arr[left])
         left = left+1
     unique.add(arr[rigth])
     max_length = max(max_length,rigth - left+1)
print(max_length)
# sliding approach in the string :



         

     
