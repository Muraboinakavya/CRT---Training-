''''
Analogy:
you are given 2 programs whre it is generating the same output
how will you decide which one to use?
1.Faster program
2.Less memory
3.Efficient
# Algorithmic complexity == efficient
  two types:
  1.Time complexity :faster result in google
  2.space complexity:
                         Mark-Zukerberg(facebook foundar)
                        /            \
                        A            B
Time complexity?
  Time complexity measures how the running time grows as the size of input
  3 - Techniques to measures time complexity
  Tecniques 1-> method(stop watch method)
  '''
import time
start = time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)
'''
problem in the above technique
1. different system different time
2.different compailer/different interpreters
3.background apps effect time
4.Internet/cpu/Gpu/affect the performance
Tecniques 2-> Counting the num of operations
 Not measures the time in seconds but counts operations
 EXAMPLE -1
 def mysum():
    total = 0
    for i in range(x+1):
        total = total+i # operations are two in this that are (assign,addition)
Tecnique 3-->Order of growth
'''
Notations:
Asymptotic Notations
1.Big oh o(): Calc th upper bound(Wrost time complexity)
2.Omega Notation : Best case complexity
3.Theta :average case complexity
EXAMPLE :
arr[1,2,3,4,5]
arr[0] == target#-->best case
arr[4] == target # --->average case
arr[last] == target #worst case comlexity
Big Oh : wrost time growth 
FOCUS:
1.Measuring the scalability 
2. Machine Independent
3. focuses on growth
4.ignore the hardware
#example-2:
def mysum(x):
    total = 0
    for i in range(x+1):
        total = total+i
    3 1+2n x=10--->21 operations
Big oh (rules)
1.additive constant(remove)
#1+2n ---> 2n

2.multiplicative constant(remove)
#2n ---> n 
   
time complexity --->O(n)
   
time complexity --->O(n)
**** in the nested loops the maximum time complexity is O(n^2)
**** but in individual loops the maximum result of  time complexity is O(n)
ex :
while n>1:
     n=n//2
# the above program gives the time complexity is (O(log(n))) because the loop dividing with 2 then   it give sthe output is (O(log(n)))
SPACE COMPLEXITY:
the space complexity  measures the memory usaged by the algorithms
1.input space
2.Auxiliary space
example :
a = 10
v = 20
constant space ---->O(1)
example-2:
arr =[0]*
namelinear---->O(n)
'''
