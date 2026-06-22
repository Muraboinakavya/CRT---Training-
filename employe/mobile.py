password = input("Enter the password : ")

if(len(password)<6):
     print("weak password")
elif(len(password)>=6 and len(password)<=10) :
    print("Medium")
elif(len(password)>10 and char.isalpha() and char.isdigit() ) :
    
     print("strong")
 