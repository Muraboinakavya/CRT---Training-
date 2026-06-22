#problem1 = sum of the elements in the list 
# a = [ 10,20,30,40]
# total = 0
# for i in a:
#      total = total+i
# print(total)
# find the maximum num in the list 
# a = [ 10,20,30,40]
# max = a[0]
# #total = 0
# for i in a:
#     if(i>max):
#          max = i
# print(max)
#TASK---->COUNT THE EVEN NUMBERS IN THE LIST 
# a = [ 10,20,30,40] 
# total = 0 
# for i in a:
#     if(i%2==0):

#         total = total+1
# print(total)
#TASK---> REVERE THE LIST 
# a = [ 10,20,30,40] 
# #a.sort()
# #print(a)
# a.reverse() 
# print(a)
 #TASK -->  remove duplicate in list  
# a = [ 1,2,3,4,3,2]
# result = []
# for i in a :
#     if i not in result:
#         result.append()
# print(result)

# a =[20,60,70,10]
# largest =float('-inf')
# second_largest = float('-inf')
# for num in a:
#     if num>largest:
#          second_largest = largest 
#          largest = num 
#     elif num>second_largest and num !=largest:
#          second_largest = num
# print(largest)
# print(second_largest)
#TASK---> CHECK THAT THE LIST IS SORTED OR NOT
# a = [5,4,9,7,54]
# flag = True 
# for i in range(len(a)-1):
#      if a[i] > a[i+1]:
#         flag = False
#         break
# print(flag)
#TASK--> FIND THE LARGEST ODD NUMBER IN THE LIST :
#8.find the largest odd number:
# list = [1,2,3,4,5,6,7,8,9]
# large = 0
# for i in list:
#     if i % 2 != 0 and i > large:
#         large = i
# print(large)
# TASK--->CREATE A LIST OF squares
# list =[2,4,5,10]
# square =[]
# for i in list:
#      #square = i*i
#      result = square.append(i*i)
# print(square)
#TASK 10----> CHECK WHETHER THE GIVEN NUMBER EXIST IN THE LIST:
# list =[2,4,6,7,8]
# target = 4
# flage = False
# for i in list:
#       if(i==target):
#           flage = True
#           break
# if flage:
#      print("element found")
# else:
#       print("not found")
#TASK11--->FIND THE COMMON ELEMENT IN THE TWO LISTS 
# list1 =[2,5,0,65,29,15]
# list2 =[76,82,29,15]
# for i in list1:
#      if i in list2:
#           print(i)
#TASK12: SWAP THE FIRST AND LAST ELEMENTS :
# list =[2,4,7,8,9]
# swap = 0
# a =list[0]
# b = list[-1]
# print(list) 
#TAK13 -----> FIND THE MAXIMUM IN A TUPLE :
# t = (10,20,40,50,90)
# temp = t[0]
# for i in t:
#      if(i>temp):
#            temp = i

# print(temp)
# #TASK 14---> CONVERT TUPLE INTO LIST :
# t= (1,3,8,0)
# a = list(t)
# print(a)
# print(type(a))
#TASK15---> FIND THE AVERAGE OF THE NUMBERS IN A LIST INPUT FROM THE USER  :
# n = int(input())
# a = list(map(int,input().split()))
# count = 0
# for i in a :
#       count = count+i
# print(count)
# avg = count/n 
# print(avg)      
#TASK16-----> FIND THE ALL THE ODD NUMBERS IN A LIST 
#NOTE: TAKE THE LIST FROM THE USER 
# a =list(map(int,input().split()))
# for i in a:
#       if(i%2!=0):
#           print(i)
#TASK17----> FIND THE SUM OF THE DIGITS OF EACH ELEMENT IN THE LIST:
#n = int(input())
#a = list(map(int,input().split()))
#for i in a:
 #    temp = i
  #   total = 0
   #  while(temp>0):
    #      total = total + temp%10# the (value%10)  by using this the last value of the element it gives(EX: 123%10--> it gives '3')
       #   temp = temp//10# the (value//10) by using this the last value will be delete it gives the reminder digits(EX:123//10--->it give'12')
     #print(total)
     

#GENERAL PROGRAM ADDITION OF ALL ELEMENT OF IN THE INPUT LIST :
# a = list(map(int,input().split()))
# count = 0
# for i in a:
#       count = count+i 
# print(count)
#TASK15---> FIND THE SMMALLEST NUMBER IN THE LIST :
# n = int(input())
# a = list(map(int,input().split()))
# count = a[0]
# for i in a:
#       if(i%2==0 and i<=count):
#            print(i)
#TASK17---> FIND THE NUMBER OF ELEMENTS GREATER THAN AVERAGE:
# n = int(input())
# a = list(map(int,input().split()))
# count =0
# for i in a:
#      count+=i 
# print(count)
# avg = count/n 
# print(avg)
# for i in a:
#     if(i>avg):
#          print(i)
#ALTERNATE METHOD TO WRITE THE ABOVE PROBLEM :
# n = int(input())
# a = list(map(int,input().split()))
# total = sum(a)
# average = total/n
# for i in a:
#       if(i>average):
#            print(i)
#TASK19---> FIND THE DIFFERENCE BETWEEN THE LARGEST AND SMMALLEST NUMBER IN THE LIST:
# n = int(input())
# a = list(map(int,input().split()))
# max = a[-1]
# min = a[0]
# for i in a:
#      if(i>=max):
#           max = i
#      if(i<=min):
#           min = i
# print(min)
# print(max)
# result = max- min
# print(result)
#TASK20---->COUNT THE NUMBERS ENDING WITH 5:
# a = list(map(int,input().split()))
# count = 0
# for i in a:
#      temp = i
#      if(temp%10==5):
#           count = count+1
# print(count)
#TASK21:--> REPLACE THE NEGAR
# a = list(map(int,input().split()))
# for i in range(len(a)):
#      if(a[i]<0):
#         a[i] = 0
# print(a)
#TASK22--->PRODUCT OF ALL ELEMENTS IN THE LIST 
a = list(map(int,input().split()))
product = 1
for i in a:
     
     product = product*i 
      
print(product)
      
      


           


           

      



                


        
        
        
     
     


    

