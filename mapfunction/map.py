# MAP function:
# arr = list(map(int,input().split()))
# #map
# applies the functions each element of iterable
# map(function,iterable)
# EX:
# def square(x):
#      return x*x
# nums = [1,2,3,4]
# result = list(map(square,nums))
# print(result)
#squares of the given numbers by using lambda:
nums = [55,25,16]
square = list(map(lambda x : x*x*x,nums))
print(square)
