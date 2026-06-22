# name = "kavya navya divya bhagii adithya"
# print(name.split())
# variable = name.split()
# joinvariable = ("_".join(variable))
# print(joinvariable)
# for i in range(len(name)):
#     print(name[i])
#     if(name.startswith('a')):
        #print(name[i])

       
#person = (name.startswith('a'))
#print(person)
#print(len(person))
#print(person.count('a'))
#print(person.center(30))
#Task-1
str = input("Enter the string : ")
special = "!@#$%^&*"
for ch in str:
     if(ch==ch.upper() and ch==ch.lower() and ch.isdigit()  and ch in special and len(str)=8 ):
        print("valid password")
    else:
        print("invalid password")