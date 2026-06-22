#  b =[10,20]
#  b.append(30)
#  print(b)
#  # adds the multiple elements extend() method)
#  a.extend([40,50,60])
#  print(a)
#  #insert()-->this method is add the elements in the specific index
#  b.insert(2,20)----> first part is index and second part is element 
#  print(b)
#  #remove()---> this function remove the element from the list
#  b.remove(20)--->delete the elememt in the list 
#  print(b)
# # pop() this method is used to delete the element base on the index 
# b.pop(0)
# print(b)
# #clear() this method is used to delete the all elements in the list
# b.clear()
# #index() return the position of the element ---> that means it shows the particular element position 
# b.index(20)
# print(b)
# #count() this method is used to count the occurence of the element 
# b.count(20)--> this the method shows that the value 20 repeated time 
# print(b)
# #reverse() this method is used to reverse the list 
# b.reverse()
# print(b)
# #copy()  this method is used to copy the elements from one variable to another variable 
# c = b.copy()
# print(c)
# #sorting in list 
# a = [10,20,30,5,4,6]
# a.sort()
# print(a)
# #sort() this method sorts the in asscending order 
# #Descending order :
# a.sort(reverse=True)
# print(a)
# #sort()--> this method is used to sort the list 
# #sorted()--> this method  it creates the new list
# ex : b =sorted(a)
#      print(b)
#SUM() THIS FUNCTION IS USED TO FIND THE SUM OF THE LIST
#EX: a[10,20,30]
#print(sum(a))
# TASK1---> create the list with 5 bestfriends 
# 1.add a new frnd just introduced 
# 2.remove  the 2 frnd just a fight 
# 3.add 3 close frnds ata single time 
# 4. sort the frnd in alphabetical order 
# 5.delete the frnd at index 5
# 6.copy the frnd list in a new list 
# 7.then perform clear the list
list = ["kavya","navya","meher",'t5','k2','l2',]
print(list.append('m2'))
print(list.remove('m2'))
list.remove('t5')
list.extend(['w2','x5','t20'])
print(list)
list.sort()
print(list)
list.pop(5)
list2 =list.copy()
print(list2)
list.clear()
#Nested list?
a = [[1,2,3],[4,5,6]]----> nested loop
    0(index)  1(index) 
      print(a[0[1]])----> this will print the index 0(index) of the 1(index) it gives 
#Iterating over the list 
a = [10,20,30,40]
for i in a :
     print(i)
# range()  by using rande function

for i in range(len(a)):
     print(a[i])
#******LIST comprehension:
[expression for yhe variable in iterable]
square = [X*X for x in range(1,6)]
print(squares)