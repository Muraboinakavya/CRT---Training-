'''
what is dict?
list----> list is a clloection of elements and it is mutable
tuple---> tuple is a collection of elements and it is immutable
dict-----> it is a collection of key value pairs
            key : values
             08  : "kavya"
    syntax"
         dict :{}
# mutable : can be modified 
#'keys' are immutable and values are mutable
#Not allows duplicates of -->keys
#values can be duplicates
# there is no fixed indexing
  in the dictinory we can access by the key value  instead of the index values
searching is very efficient in dictionary and the time complexity  for dict is o(1)
dict uses hashing technique to search hence o(1)
ex:  list = ["manish","08",26]
#Creation of dictionary 
student = {
"name" :"kavya",
"roll.no" : 08,
 "age"  : 20
}
-----------------------------------------------------
2nd method to create the dictinory
student1 = dict(name = "kavya",age = 10,branch ='ai')
print(student1)
--------------------------------------------
3rd method to create the dictinory
data ={}
print(data)
update the value :
student["name"] = "meher"
print(student) --> it is automatically the update the value
------------------------------------------------------------
# delete the value 
student.pop("age")
print(student)
2nd method to delete the value:
del student["roll.no"]
print(student)

why we use dict?
1.labels
''
feature             list                dict
ordered             yes                  no
access(indexing)    yes                  keys no
arr[0]              yes                  student["keys"]


student = {
"name" :"kavya",
"roll.no" : 8,
 "age"  : 20
}

--------------------------------------------------------------------------
********* Dictinory  themselves cannot be sorted **************************
-------------------------------------------------------------------------------
#print(student)
student1 = dict(name = "kavya",age = 10,branch ='ai')#dictinory creation
print(student1["name"])#acessing the key in the dictinory
student1["lucky no"] = 2 # adding the key to the dictinory 
print(student1)
student1.update({"father" : "sirnu","mother" : "srilakshmi","gender" : "female"})
for in ae:
  






