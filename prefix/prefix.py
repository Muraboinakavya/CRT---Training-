'''
prefix sum: one of the most importent techniqye used
to solve sub array problems
1.fast range sum queries
2.Optimization
3.sliding window ulternative
4.sub array problems
5.competitive programming

-->reduces the repeated 
and improves the time complexity

what is prefix sum?
stores the cumulative sum of the elements
from the beginning of the array to every index

arr = [a0,a1,a2,a3....]

then:
the prefix of i will become
prefix[i] = arr[0]+arr[1]+arr[2]+.....arr[i]
'''

#problem:

# find the sum from index 1 to 3  general  code
# arr = [10, 20, 30, 40, 50]
# # index: 0 1 2 3 4

# sum = 0
# for i in range(1, 4): 
#     sum += arr[i]

# print(sum)

# # prefix sum --->
# arr = [2,4,1,7,3]
#      0 1 2 3 4
#calculate the prefix:
#index   arr[i]  prefix[i]
# 0       2        2
# 1       4       2+4
# 2       1       6+1
# 3       7       14
# 4       3       17

#prefix[1] = [2,6,7,14,17]

'''
prefix[0] = 2 sum from 0 to 0
prefix[1] = 6 sun orom 0 to 1
prefix[2] = 7 sum from 0 to 2
prefix[3] = 14 sum from 0 to 3
prefix[4] = 17 sum from 0 to 4
to calculate the prefix the formila is (prefix[i] = prefix[i-1]+list1[i])

#TASK:SUMOF THE ELEMENTS FROM 1 TO 3:
list1 = list(map(int,input().split()))
n = len(list1)
#create a prefix array
prefix =[0]*n #[0,0,0,...]
prefix[0] = list1[0]
#Build the prefix sum:

for i in range(1,n):
     prefix[i] = prefix[i-1]+list1[i]
print(prefix)
l = 2
r = 3
#range sum:
if l==0:
     ans = prefix[r]
else:
     ans = prefix[r] - prefix[l-1]
print(ans)
'''
#Task: find the multiple range queries:
list1 = list(map(int,input().split()))
n = len(list1)
#create a prefix array
prefix =[0]*n #[0,0,0,...]
prefix[0] = list1[0]
#Build the prefix sum:

for i in range(1,n):
     prefix[i] = prefix[i-1]+list1[i]
print(prefix)
queries = [[1,4],[2,5],[0,3]]
for l,r in queries:
#range sum:
    if l==0:
       ans = prefix[r]
    else:
        ans = prefix[r] - prefix[l-1]
    print(f"sum of {l} to {r} = {ans}")

   