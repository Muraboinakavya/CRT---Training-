# product of the given array using the recursive approach:
n = int (input())
arr = list(map(int,input().split()))
def product(i):
    if  i == n:
       return 1
    return arr[i] * product (i+1)
print(product(0))
