# ***** TASK: ROTATE THE LIST BY K POSITIONS 
# GIVEN  a List and k integer ,rotate the list to the left by k position 
#  n = int(input())
#  a = list(map(int,input().split()))
#  k = int(input())
#  for i in a :
#       k = k% N # this is used to handle the large size of the k value than list 
#       rotated = a[-k:]+a[:-k] # in this the a[-k:]--> this mean the list start from last  k values and a[:-k] this mean the first element upto last  k values 

# print(rotated)
#ANOTHER METHOD FOR THIS PROBLEM BY USING BUILD IN FUNCTIONS INSTEAD OF TRAVERSAL:
n = int(input())
a = list(map(int,input().split()))
k = int(input())
list1 =[]
for i in range(a[:-k]):
     a.pop(0)
     list1.append(i)

         

