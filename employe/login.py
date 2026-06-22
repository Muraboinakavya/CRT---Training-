username = input("enter the user name : ")
password = input("enter the password : ")
attempt = int(input("Enter the attempts : "))
correct_username = "kavya"
correct_password = "navya@1"
if(username == correct_username and password == correct_password) :
       print("Login correct")
if (len(password)<8):
        print("weak password")
if (attempt>=3): 
        print("account block")
else :
        print("login failed")
#else :
 #   print("invalid password")
#else : 
 #       print("spam")

