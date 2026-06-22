'''
what is reduce()?
repeatedly applies functions
reduces the iterable to single value
syntax:
reduce(function,iterable)

functools --->module
'''
from functools import reduce
def add(b,c):
    return b+c
nums = [2,3,5,6]
result = reduce(sum,nums)
print(result)

