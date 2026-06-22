cart_value = int(input("Enter the cart value : "))
premium = (input("enter the cat is premier yes(or)not : " ))
if(cart_value>5000 ):
    discount = cart_value * 25/100
    final_amount = cart_value - discount 
    print(final_amount)
elif (cart_value>3000):
    discount = cart_value * 15/100
    final_amount = cart_value - discount
elif(cart_value>1000):
    discount = cart_value * 10/100
    final_amount = cart_value - discount
if(premium == "yes"):
    discount =  discount + (cart_value * 5/100)
    final_amount = cart_value - discount
    gst = final_amount * 18/100 
    payable_amount = final_amount +gst 
    print("Discount Applied : ",discount)
    print("GST :",gst) 
    print("the final amount : ",payable_amount)
else:
    print("no discount")

    
    