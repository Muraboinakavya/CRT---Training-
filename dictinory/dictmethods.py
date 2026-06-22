'''
dictinory methods---->
1.# keys()---> returns the keys in the dictinory
print(student.keys())
------------------------------------------------------
2.#values()---> returns the all the values in the dictinory 
print(student.values())
----------------------------------------
3.items()--> this method gives the all the keys and values in the dictinory 
print(student.items())
---------------------------------------------
4. access the element in dict 
print(student.get("branch"))---> by using the get() method it is good 
when we use the enter the key which is not in the dict by using the get()method it does not throw the erroe it gives none
-----------------------------------------------------------------------------------
5.update({})--> this method add multiple elements
student.update({"branch" : "ai","collage" : "city","gender": "femele"})
-----------------------------------------------------------------------
6.popitem() this method delete the last inserted pair 
student.popitem()
print(student)
-----------------------------------------------------------
#LOOPING ON DICTIONARY
for i in student:
     print(i) ---> this prints only the key values
     
    
#Nested dictinaries:dict inside dict:
student ={
    "s1":{
     "name" : "kavya",
     "branch" :"ai"
     },
     "s2":{
        "name":"meher",
        "branch":"cse"
     }
}
print(student["s1"]["name"])
#can i store list inside the dict
student ={
    "name" :"bhagii",
    "marks":[10,20,30,40]
    }
print(student)
#you can store the multiple dictinory in list:
student =[
    { "name":"kavya","branch":"ai"},# ---> index value of this dict is (0)
    # int this we write the dict inside the dict int in this we can access by using index value
    {"name":"bhagii","branch":"cse"}#---> index value of this dict is(1)

]
print(student[0]["name"])
'''
#Dict comprehension
#{key:value for  variable in iterable}
squares = {X:X*X for X in range(1,11) }
print(squares)
#dict comprehension

#{key:values for variables in iterable}
squares = {x:x*x for x in range(1,11)}
print(squares)

#keys: rules
'''
int
string
list --- no
dictionary

student = {
    1:"Manish",
    "Roll":08,
    (1,2):"tuple"
    [1,2,3]:"List" # List is not be used as a key 
    {"Name":"Manish"}:"Hello" #cant use 
    






