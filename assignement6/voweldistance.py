name = input("Enter the string : ")
vowel = "aeiouAEIOU"
prevoius_position = -1
count = -1
balance = True

count =0
for i in  range(len((name))):
  if name[i] in  vowel:
    if(prevoius_position != -1):
      gap = i - prevoius_position-1
    if( count ==-1):
         count= gap
    elif gap != count:

        balance = false
        break
        prevoius = i 
    if balance:
        print("balanced")
    else:
         print("Not balanced")


      
        
          

     