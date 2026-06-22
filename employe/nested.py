user = input("enter the username")
# first condition
if user == "admin" :
    password = input("Enter the password :")
    #Nested condition
    if password == "1234" :
        print("Login successful")
    else:
        print("wrong password")
else :
    print("Invalid username")
    # nested if means if-else inside contains the if-else condition
    #Syntax 
    # if :

    #     statement
    #     if:
    #         statement
    #     else:
    #         statement   
    # else:

         

