age=int(input("Enter Your age: "))
if age<3:
    print("Your Ticket is Free")
elif age>=3 and age<=12:
    print("Ticket price is $10")

elif age>12:
    print("Ticket price is $15")

else:
    print("Invalid Input")
    
