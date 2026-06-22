#  what is filter?
#  selects the elements based upon the condition
#  Syntax:
#  filter(function,iterable)
#  Ex:
# def is even():
#     return x%2==0
# list = [1,2,3,4,6]
# result = filter(is_even,list)
# print(result)
nums = [2,3 ,4 ,5]
square = filter(lambda x : x % 2 == 0,nums)
print(list(square))

     