'''
str = "collaage"
#print(len(str))
print(str[-1:-4])
#slicing:
str[start,end,step]
print(str[0:3])

OMITTING START
str[:3]----> start from 0 to and end with 3-1 that means (col)
# C O L L E G E
  0  1 2 3 4 5 6
  C       L     E 
  C     L   E    E 
  #STEP SLICING : in this zero will be count
  str[0:6:2]----->CLE 
  str[0:6:1]------>colleg 
  '''
  # REVERSE THE STRING IN  WITH STEP SLICING METHOD
  #[::-1]------>this start from -1 and goes upto end
#name = "kavya"
#print(name[::-1])
'''
STRING TRAVERSAL:

str = "chalapathi"
for i in str:-----> this for loop statement of sequence (for i in sequence)
    print(i)
    the string traversal by using the for loop of range(for i in range())
    '''
'''
str = "chalapathi"
for i in range(len(str)):
    print(str[i])----->when we use only print(i) we print onlly index if we print(variable name(i))then we give the characters
'''
#UPPER, LOWER CASES
# name = "kavya"
# for ch in range(len(name)):
#     print(ch,name[ch])
#     print(name.upper())
#     print(name.lower())
#TITLE ------>
#strip ---> Remove the extra spaces

# collage_name = " chalapathi "
# print(collage_name.strip())
# REPLACE() METHOD:
#text = " I Love programming"
#print(text.replace("I Love","Hate"))
#---> here also we can use by using also variable 
#COUNT THE PARTICULAR WORD IN A STRING (OR) FREQUENCY OF THE A WORD
# COUNT()METHOD
friut = "banana"
print(friut.count("a"))
# STARTsWITH()
#it checks that the string start the  word (or) not
print(friut.startswith('k'))
# ENDSWITH()
#it checks that the string END WITH the  word (or) not
# split()
text = "python c java"
print(text.split())
separate = text.split()
print(type(separate))
# Using "join()" method convert list---->string
#python - c - java
new = ("-".join(separate))
print(new)
# SEARCHING INSIDE THH STRINGS
 # FIND()--->
#print(new.find(python))
print("python" in new)
# index()
text = "python"
#print(text.index("z"))
# which is safe find() or index()
  # *** find() id safe to use
  # STRING FORMATTING
name = "vijay"
age = 20
#print(f"My name is {name} and age is{age}")----> fstrings
#print(My name is,name,"and age is",age)------>old college
# FORMAT()METHOD
print("Welcom{}".format(name))#----->format()method
#ESCAPING characters or sequence
print("hello \n World")
print("Hello \t World")
'''
# R- strings(Regex - regular expressions)
path = r"c:// download/photos/pic.jpeg"

r---> tells to the interpreter that thre are no escaping characters in path
'''
# swapcase()
str1 = "kavYA"
#str2 = "bhagii"
print(str1.swapcase())
#casefold--->strong lower converstion
print(text.casefold())

# center()method
print(text.center(40))
# TASK : create the string with your frnd names
# name = mainsh vijay ajay
#split the names to in alist

#join the string "_"
# traverse over the string and find the index
# of the person name starting  with "A"
# print the person name
# count the len of the name & check " a" apperence
#print
name = "kavya","navya","divya","bhagii","Adithya"
print(name.split())
variable = name.split()
joinvariable = ("_".join(variable))
  for i in range(len(name)):
       print(name[i])
       
person = (name.startswith('A'))
print(person)
print("the length of the string :",len(person))
print(name.count("a"))
rint(name.center(30))
nested loops in the uv in this loope are in design in this the loops are in horizontel line 
 they are many types in this len() this method used to find the length of the string
 strip() this method is used to  it gives the space to the strings in this the valie od the string is incress
  








