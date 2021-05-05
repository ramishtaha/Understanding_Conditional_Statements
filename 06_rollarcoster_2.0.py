print("Welcome to the rollercoster!\n")
height = int(input("Please Enter Your Height in cm: "))
ticket_price = 0

# Check the Height of the person and ask them about their details.
# Inform them about the price of the ticket
if height > 120:
    print("You can Ride the RollerCoster ")
    age = int(input("Please Enter Your age in Yrs: "))
    if age < 12:
        print("Child Tickets are $5.\n")
        ticket_price += 5
    elif age <= 18:
        print("Youth Tickets are $7.\n")
        ticket_price += 7
    else:
        print("Adult Tickets are $12.\n")
        ticket_price += 12

    wants_photo = input("Do you want Photos to be Taken? Y or N. ")
    if wants_photo == "Y":
        ticket_price += 3
    
    if age < 45 or age > 55:
        print(f"Your Total Ticket Price is ${ticket_price}")
    else:
        print("Sir, you are going through Midlife crisis your ticket will be on the house!!")
        ticket_price = 0

else:
    print("Sorry you have to grow Taller before you can ride.")