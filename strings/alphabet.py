# TASK-->  check that the given character is alphabet or not
# name = input("Enter the  character :")
# str =ord(name)

# if((str >=65 and  str <=90 or str>=97 and str<=122)):
#      print("the given character is a alphabet")
# else:
#     print("not a alphabet")
# # TASK--> find the length of the string without using len()function
# str = input(" enter the string :")
# count = 0
# name = str.strip()
# print(name)
# for i in str:

#     count = count+1
# print(count)
#Task -->Toggle each character 
#str = input(" enter the string :")
result =""

# for ch in range(len(str)):
#     if str.isupper():
#         result += ch.lower()
#         print(result)
#     else:
#         result = result+.lower()
#         print(str.upper())
        
#  TASK3----> Remove the vowels from the string
# str = input("Enter the string :")
# vowel = "aeiouAEIOU"
# result =""
# for ch in str:
#     if ch.lower() not in vowel:
#         result +=ch
# print(result)
#TASK4---->print the only alphabet in the string expect digits and special characters
# str = input("Enter the string :")
# result = ""
# for ch in str:
#     if(ch.isalpha()):
#      result = result +ch
# print(result)
# #TASK5----->Remove the space from  the string and print without space 
# str = input("Enter the string :")
# result =""
# for ch in str:
#      if(ch !=" "):
#         result = result+ch
# print(result)
# #TASK6 -------> Remove the brackets from the algebric expression
# str = input("Enter the function : ")
# result =""
# #list =["()", "{}" ,"[]"]
# for ch in str:
#     if(ch not in "()[]{}"):
#         result = result+ch
# print(result)
#TASK7------> addition of integer in the string
# str = input("enter the string :")
# result = 0
# for ch in str:
#      if(ch.isdigit()):

#         result = result+int(ch)
       
# print(result)

#task8:capital the first and last letter of the string
m = input("enter the m:")
result = []
words = m.split()
for word in words:
   if len(word) == 1:
      result.append(word.upper())
   else:
      new_word = ( word[0].upper()+word[1:-1]+word[-1].upper())
      result.append(new_word)

print("".join(result))


    
     

              
        

    
