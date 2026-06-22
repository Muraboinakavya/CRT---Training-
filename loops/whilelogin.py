password = int(input("Enter the password : "))
correct_password = 12345
while(password != correct_password):
    password  =int (input())     
    if(password != correct_password):
         print("password invalid :")
         print("login successfully")
