'''def productivity_report(activities):
    #dict to store employee task counts
    count = {}
    #traverse each activity
    for activity in activities:
        #John:Login --> name = John
        #task = Login
        name, task = activity.split()
        name = name.lower()
        if name in count:
            count[name] +=1
        else:
            #add a new employee with count
            count[name] = 1
    employees = list(count.items())
-----------------------------------------------------------------
Task2:Given an array of integers, count how many elements become a new maximum when traversing the array from left to right.
The first element is always considered a new maximum because there are no elements before it.
Whenever an element is greater than all previously seen elements, it is counted as a new maximum.
Print the total number of such elements.
 
arr = [7,4,8,2,9]
max_so = arr[0]
count = 1
for i in range(1,len(arr)):
     if  arr[i] > max_so :
        count = count +1
        max_so = arr[i]
print(count)
------------------------------------------------------------
Task3:Given an array, move all the 0's to the end while maintaining the order of the non-zero elements.
arr = list(map(int,input().split()))
count = 0 
list1 = []
for i in range(0,len(arr)):
     if arr[i] != 0:
        count = count+1
        list1.append(arr[i])
zeros = len(arr) - count
for i in range(zeros):
    list1.append(0)
print(list1)
-----------------------------------------------------------------
triplet problem:
'''
n= int(input())
arr = list(map(int,input().split()))
for i in range(n-2):
     
