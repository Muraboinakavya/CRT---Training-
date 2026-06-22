'''
what is set?
set is a collection of unordered unique the elements
-->unique(never allows the duplicates)
-->fast searching--->o(1)
why?
-->fast searching--->o(1)
-->duplicates removal
#set is a mutable but we can modify by using the buliding functions
#set is unordered --->there is no fixed indexing
How to create a set?

numbers = {1,2,3,4,5,6}
print(type(numbers))
#when you want to delete the duplicates in the list you just write in the set
#EX:
num = [1,2,2,3,3,4]
unique = set(num)
print(unique) 
HOW to create a set:
1st method
set ={1,2,3,4}
#2nd method :
s = set(1,2,3,4)
How to create a empty set:
s = set()-->this is the syntax to create the empty set 
set methods:
1.add()--> this method is used to add the  value to the set
s ={2,3,4,5,6}
s.add(1)
print(s)
2.update()--->this method for multiple elements at a time
s.update([2,3,4,5])
print(s)
3.remove()-->this used to remove element
s.remove(2)
print(s)
4.discard()-->this ia called safe for delete when we write un none element but it does not throw any error
print(s.discard(10))
5.pop()--> delete random element
s.pop()
print(s)
6.clear()-->it clear the all data that meand delete the elements
if we use(in) it gives the ouput in boolean value
SET OPERATIONS:
1.union
2.intersection
3.difference
Ex:
'''
# a ={10,20,30,40}
# b ={60,70,90,50}
# print(a|b)-->symbole for union
# print(a.union(b))-->build in function for union
# print(a.intersection(b))-->bulid in functions
# print(a-b)-->difference symbole
# print(a.difference(b))
#symmentric difference it is exact opposite to the intersection it does not gives the common value it gives un common values
'''
a ={10,20,30,40}
b ={60,70,90,50}
print(a^b)
##symmentric difference
a = {1,2,3}
b = {2,4,3}
print(a^b)
#built in method
print(a.symmetric_difference(b))

#subset and superset
#subset:common elements in a set
a={1,2}
b={1,2,3,4}
print(a.issubset(b))
print(b.issuperset(a))

#Frozenset:immutable version of set
fs = frozenset([1,2,3,4,5])
print(fs)


feature           list      tuple        dictionary    set 
ordered            yes       yes           no            no
mutability         yes        no           both         yes
allow  duplicates   yes       yes       key:no,val:all  no 
indexing           yes       yes          no            no 

can i store list inside the set?
1.list
2.dict
3.set
print(a.issubset(b))#--->when we use (is) it gives the bollen output
'''
# Task:
# create a list with squares of a number
# convert the list with
# squares of a number to set
# try to repeat the square two times
# add the multiple of 2 to the same  
# set at a single Time 
# --> separate the set with 2 diff sets
# multiple of 2
# squares
# now perform all the set operations on both
list1 = list(map(int,input().split()))
for i in list1:
    square = i**2
    print(square,end=" ")



