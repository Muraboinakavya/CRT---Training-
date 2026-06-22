'''
Iterators:
give the one element at a time on demand
python refers this iterators:
* memory efficency
*controlled acces
iterable: is an object can be looped
1.list 
2.tuple
3.set
4.dict
5.string
Examples:
 nums = [10,20,30,40]
  for i in range(0,len(num)):
        print(i)
-----> working process
    list
     |
    iter()
      |
    iterator 
How loop in python works internally
iterators-->will be used internally
iter(),next()
nums = [1,2,3,4]
it = iter(nums)nums = [1,2,3,4]
   it = iter(true)
   while true:
       try:
          x = next(it)
          print(x)
        except stop iteration:
            break   

# syntax:
iterable_object = [1,2,3,4]
it = iter(iterable_object)# in this iter() is  afunction used to convert the iterable to the iterator 
print(it)
print(next(it))
print(next(it))# the next() function is used to acces the element from the iterable 
examples:
iterable_object = [1,2,3,4]
it = iter(iterable_object)
print(it)
print(next(it))#element print

# using the string
name = "python"
it = iter(name)
print(next(it))
# using tuple
t = (1,2,3)
it = iter(t)
print(it)
#we can create objects with diff  data  types like list,tuple ,set...
d ={"a":10,"b":20}
it = iter(d)
print(next(it))#in this it goes only to the keys in the dictionary
#iterator No:
nums = [i for i in range(1000000)]
#huge memory
# iterator approach
nums = iter(range(1000000))
#only the current element will be processed


# creating a custom iterator
#class is a key word
class Count:
    #constructor
    def __init__(self,limit):
         self.num = 1
         self.limit = limit
# this method that means iter() this method makes the object iterable and return the iterator object itself
    def __iter__(self):
        return self 
    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        x = self.num
        self.num +=1
        return x
#creating  object
c  = count()
print(next(c))
print(next(c))
'''
# Task: print the even numbers:
class Count:
    #constructor
    def __init__(self,limit):
         self.num = 2
         self.limit = limit
# this method that means iter() this method makes the object iterable and return the iterator object itself
    def __iter__(self):
        return self 
    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        x = self.num
        self.num +=2
        return x
#creating  object
c  = Count(10)
for i in c:
     print(i,end="  ")
     ## what is meant by lazy evalution means : 
     in which an expression or value is computed only when it is neede, rather than when it if defined 



