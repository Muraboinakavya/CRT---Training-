'''conditinol statement:
what conditional statements?
A conditional statement allows a program to make decisions based on the whether a condition is true (or) false
 flow of conditional Statement:
         condition 
            |
            True----->execute the blocks
            |
    flase--->skip the blocks
Types of the conditional statements:
1.if Statement
2.if-else
3.if -elif-else
4.nested if
1.if stements:
if statement is used when we want execute the a block of code only when the condition is true
#Ex:
Syntax:
if(condition):---->if condition
    Statement--->if block 
Ex:

age = 6
if(age >= 18):
    print("Eligible")

2.if-else:
if- else is used when there are two possibilities
Syntax:
if(condition):
     statement
else:
    Statement

age = int(input("Enter the age of a person"))
if(age>=18):
     print("Eligible")
else:
     print("Not Eligible")
#3.if - elif - else
pupose:it is used when there are multiple conditions
#elif ---> else if
Syntax:
if (condition):
     statements
elif(condition):
else:
    statements
#Ex:
marks = int(input("Enter the marks : "))
if(marks >= 90):
      print("Grade A")
elif(marks>=70):
      print("Grade B")
elif(marks >=50):
      print("Grade C")
else:
     print("Grade D")
4.Nested if:
it is used when one condition  depend on the other condition
** An if inside another if 
syntax:
if(condition):--->outer if
    if(condition):-->inner if--->if block
        statements
'''
#programs:
age = 10 
print("")
license = True
if(age>= 18):
    print("below 18")
    print()
    if license == True :
         print("can drive")
    else:
else:





   




  











      
