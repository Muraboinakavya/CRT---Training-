#problem1: #find the largest element in  an array using recursion:
def find_max(arr,n):
     if n==1:
         return arr[0]
     return max(arr[n-1],find_max(arr,n-1))
     peint(find_max(arr,len(arr)))
#problem2: find the given arrays is sorted or not by using by recursion technique:
def is_so