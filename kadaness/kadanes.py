'''
kadane's algorithm : max sub arrays problems
a = [2,-1,3,-2,4]
find the contigious sub array with max sum


subarrays           sum
[2]                   2
[2,-1]                1
[2,-1,3,]             4
[2,-1,3,-2]            2
[2,-1,3,-2,4]           6

kadane's algorithm main idea 
at every element we decide:
two choices:
1. continue the previous subarray
                (or)
2. start a new subarray
current_sum = -5
next_element = 10
-5+10 = 5 #discarding the previous (-ve)
next = 10

 # example 
 arr = [2,-1,3,-2,4]
 current_sum = 2
 max_sum = 2
 
 index:1
 -1 
 choice-1: extend the array 
   2+(-1) = 1
 choice-2: start a new array
 -1 
 index : 2
 
current_sum formula = max(a[i],current_sum+arr[i])
max_sum = max(max_sum,current_sum)
#Task: find thee maximum sum in the list by using the kadaness:
arr = [2,-1 ,3 -2,4]
current_sum = 0
max_sum = 0
for i in range(len(arr)):
      current_sum = max(arr[i],current_sum+arr[i])
      max_sum = max(max_sum,current_sum)
print(max_sum)
'''
#Task:

score =[-2,4,-1,5,-3,2]
current_sum = score[0]
max_sum = score[0]
start_index = 0
end_index = 0
temp_start = 0
for i in range(1,len(score)):
  if score[i]>current_sum+score[i]:
       current_sum = score[i]
       temp_start = i
  else:
      current_sum = current_sum+score[i]
      if(current_sum > max_sum):
           max_sum = current_sum
           start_index = temp_start
           end_index = i
print("Maximum score :",max_sum)
print(start_index)
print(end_index)
print(score[start_index:end_index+1])
