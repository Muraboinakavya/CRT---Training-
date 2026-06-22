'''count the frequency of the characters

explain : 
input : aaabc
output:
a:3
b:1
c:1
'''
str = input("enter the str:")
dict = {}

for ch in str:
    if ch in dict:
        dict[ch] += 1
#print(dict[ch])
       
    else:
        dict[ch] = 1
#print(dict[ch])
max = 0
  

for ch in dict:
    #max = 0
    if(dict[ch] >max):
        

    #if(dict[ch] >=0):
    max = max+1
    print(ch," ",dict[ch])
print(max)
