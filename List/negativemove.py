#TASK27: MOVE ALL THE NEGATIVE NUMBERS TO THE LEFT
#GIVEN A LIST OF INTEGERS, MOVE ALL THE NEGATIVE TO THE BEGINNING OF THE LIST 
#NOTE:IN ORDER FORM
# n = int(input())
# a = list(map(int,input().split()))
# list1 = []
# list2 = []
# for i in a:
#      if(i<0):
#         list1.append(i)
#      else:
#         list2.append(i)
# print(*list1+list2)
#'*' this is used to form in unpacking of list
# FIND THE FREQUENCY OF THE ELEMENT :
str = int(input())
frequency = {}
for i in str:
    if i in frequency:
        frequency[i] = frequency[i]+1
    else:
         frequency[i] =1
for  key in frquency:
      print(frequency[key])
      

         