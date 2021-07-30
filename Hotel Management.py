import time
credentials=[]
dictionary={}
cart=[]
cart_dictionary={}

def Royal_Room():                                                                                  # Function for royal room
    print("This is the room having full of luxury.\n1.Breakfast\n2.Lunch\n3.Dinner\nWill be served for free.")
    print("Pick and drop facility to and from the place.")
    print("HD T.V and luxurious Bathroom.")
    print("Room Service Daily and anytime.")
    cost_of_room=2000                                                                          # We have declared the cost and features
    print("The cost of room is :-",cost_of_room)
    print()

def Deluxe_Room():                                                                                 # Function for deluxe room
    print("This is the room having full of luxury.\n1.Breakfast\n2.Lunch\n3.Dinner\nWill be served but are paid.")
    print("Pick and drop facility to and from the place.")
    print("HD T.V and luxurious Bathroom.")
    print("Room Service Daily and anytime.")
    cost_of_room=1500
    print("The cost of room is :-",cost_of_room)
    print()

def Semi_Deluxe_Room():                                                                            # Function for semi deluxe room
    print("This is the room with spacious compartment alongwith a great joy of traditions.")
    print("Customer needs to come the Dinning hall and need to purchase the items.")
    print("Pick and drop facility to and from the place.")
    print("AV/DV T.V and Bathroom.")
    print("Room Service :- Once a day...")
    cost_of_room=800
    print("The cost of room is :-",cost_of_room)
    print()

def Semi_Room():                                                                                   # Function for semi room.
    print("This is the room with great Furniture")
    print("Customer needs to come the Dinning hall and need to purchase the items.")
    print("T.V and Bathroom.")
    print("Room Service :- Once a day...")
    cost_of_room=500
    print("The cost of room is :-",cost_of_room)
    print()

def proceed_for_booking(cost_of_room):                                                             # Function for booking or not
    print("Do you want to book the room?")
    proceed_for_booking=int(input("1. Yes\n2. No\n"))                                              # Asking user if he wants to book or not
    if proceed_for_booking==1:
        Calculate_Price(cost_of_room)
    else:
        book_rooms()
    print()

def Calculate_Price(cost_of_room):                                                                 # Function for calculating price and total
    print("Note:- No room will be allotted to the 3rd person.")
    print("       So 2 persons per room")
    room_quantity=int(input("How many rooms do you wish to take\n"))                               # Number of rooms user wish to have
    days=int(input("For how many days do you wish to stay here..\n"))                              # Number of days to be lived in hotel
    price_for_rooms=(room_quantity*cost_of_room)*days
    print("Total Price for the rooms are    :- ",price_for_rooms)
    calculating_tax=(price_for_rooms*18)/100
    print("CGST and SGST as per govt. rules :- ",calculating_tax)
    total_price=price_for_rooms+calculating_tax
    print("Total Amount to be paid is       :- ",total_price)
    ask_for_booking=int(input("Do you wish to book the room finally???\n1. Yes\n2. No\n"))
    print()
    if ask_for_booking<=3:
        ask_details(total_price)
    else:
        book_rooms()
    

def ask_details(total_price):                                                                      # Function for asking first name, last name and all
        First_name=input("Enter the First Name of person\n")                                  # Asking for first name
        Last_name=input("Enter the Last Name of"" person\n")                                    # Asking for last name
        cart_dictionary.update({"First":First_name,"Last":Last_name,"Price":total_price})          # Saving to cart dictionary
        cart.append(cart_dictionary)
        print()
        payment(total_price)

def card():                                                                                        # Function for payment from card
        try:
            insertcardnumber=input("Enter the Card Number :- ")                                    # Asking user to enter the card number
            if len(insertcardnumber)!=16 :                                                         # Checking length of card
                print("Invalid Details Input Again")
            else:                                                                                  # If found okay then it will proceed
                a=int(insertcardnumber)                                                            # Conveerting from string to int
                print("Checking Card valid or not....!! ")
                time.sleep(5)
                insertexpirydatemonth=int(input("Month of expiry :- "))                            # Asking user to insert Expiry Month
                insertexpirydateyear=int(input("Year of expiry :- "))                              # Asking user to insert Expiry Month
                m=insertexpirydatemonth                                                            # Assigning Insertexpirydatemonth to small variable m
                y=insertexpirydateyear                                                             # Assigning Insertexpirydateyear to small variable y
                insertcvvcode=int(input("Last 3 digit of the card:- "))                            # Asking user to enter CVV code
                if len(str(insertcvvcode))!=3 :
                    print("invalid CVV retry it")
                    print()
                else:                                                                              # If valid length of cvv code
                    print("Cvv validation...")
                    print("please hold for few seconds checking into database.")
                    print("Thanks for co-operation")
                    time.sleep(5)
                    Insertfirstname=input("Enter the First name of card Holder:-")                 # Asking for first name
                    Insertlastname=input("Enter the Last name of card Holder:-")                   # Asking for last name
                    print("Card Number :-",a)                                                      # Just Showing user for their convience
                    print("Month Of Expiry",m)                                                     # Just Showing user for their convience
                    print("Year Of Expiry",y)                                                      # Just Showing user for their convience
                    print("First Name",Insertfirstname)                                            # Just Showing user for their convience
                    print("Last Name",Insertlastname)                                              # Just Showing user for their convience
                    print("CVV",insertcvvcode)                                                     # Just Showing user for their convience
                    Enter_pin=input("Enter Pin\n")                                                 # Checking of pin length 
                    if len(Enter_pin)==4 or len(Enter_pin)==6:
                        print("Payment Successful")
                        print()
                    else:                                                                          # incase the length is greater than or less than the following the payment goes for failure
                        print("Payment Failure")
                        print()
                        card()

        except Exception as e:
                print("Add card Error is :-",e)

def wallet(total_price):
    enter_number=input("Enter the number linked to wallet")                                # Asking user to enter the number
    if len(enter_number)<10 or len(enter_number)>10:                                       # Checking the length of the phone number entered
        print("Incorrect Number please check again...")
        print()
        payment(total_price)
    else:
        print("Validating Amount..")
        time.sleep(2)
        print("Payment Successful")
        print("Thanks for booking.")
        print()

def payment(total_price):                                                                          # Asking User to pay
    print("How would you like to pay")
    print("1. Credit Card.")
    print("2. Debit Card.")
    print("3. Net banking.")
    print("4. Wallet.")
    print("5. Bhim Upi.")
    print("6. QR Scanner Code.")
    print()
    payment_method=int(input("Please select the mode of payment\n"))
    if payment_method==1:
        print()
        card()
    elif payment_method==2:
        print()
        card()
    elif payment_method==3:
        print()
        print("redirecting to bank gateway")
        time.sleep(3)
        User_Name=input("Enter User Name:-\n")
        Password=input("Enter Password:-\n")
        print("Payment for :- ",total_price)
        print("Validating Amount..")
        time.sleep(2)
        print("Payment Successful")
        print("Thanks for booking.")
        print()

    elif payment_method==4:
        print()
        print("which wallet would you like to pay...")
        print("1. Paytm")
        print("2. Jio Money")
        print("3. free charge")
        Wallet_payment=int(input("Enter the Wallet Number for payment"))
        print()
        if Wallet_payment==1:
            print("Paying from Paytm Wallet\n")
            wallet(total_price)
            
        elif Wallet_payment==2:
            print("Paying from Jio Money Wallet\n")
            wallet(total_price)
            
        elif Wallet_payment==3:
            print("Paying from Free Charge Wallet\n")
            wallet(total_price)
            
        else:
            print("No Other wallet exits\n")
            payment(total_price)
    
    elif payment_method==5:
        enter_upi_id=input("Enter the upi id\n")
        print("Validating UPI id...")
        time.sleep(3)
        enter_upi_password=int(input("Enter Password to pay.\n"))
        print("Payment Successful")
        print()
    
    elif payment_method==6:
        print("Currently Not Available\n Please Try any other method\n")
        payment(total_price)
    
    else:
        print("No other Payment exists")

def book_rooms():                                                                                  # Function declaration for bookng rooms..
    print("Welcome to the Hotel....")                                                              # Just A welcome message for the user
    time.sleep(2)                                                                                  # Just to stop as it seems genuine    
    print("We are having variety of rooms.\nPlease Select One of them.....")                       # Describing types of rooms
    print("1. Royal Room")
    print("2. Deluxe Room")
    print("3. Semi-Deluxe Room")
    print("4. Semi Room")
    
    select_room=int(input("Which room do you like:-\n"))                                           # Asking user to select a room
    
    if select_room==1:

        Royal_Room()
        proceed_for_booking(2000)

    elif select_room==2:

        Deluxe_Room()
        proceed_for_booking(1500)
    
    elif select_room==3:

        Semi_Deluxe_Room()
        proceed_for_booking(800)

    elif select_room==4:

        Semi_Room()
        proceed_for_booking(500)

    else:
        print("No such rooms available")


def check_booking():                                                                               # Function declaration for validating that booking exists or not.
    for x,i in enumerate(cart):
        print(x+1,end=" ")
        print("First Name of Guest is :-",i["First"],end=" | ")
        print("Last Name of Guest is :-",i["Last"])
        print()

def cancel_booking():                                                                              # Function declaration for cancelling the booking..
    for x,i in enumerate(cart):
        print(x+1,end=" ")
        print("First Name of Guest is :-",i["First"],end=" | ")
        print("Last Name of Guest is :-",i["Last"])
        print()

    delete_booking=int(input("Enter the Number of booking you want to cancel\n"))
    del cart[delete_booking-1]
    
    # try:
        
    # except Exception as e:
    #     print(e)

 
def login():                                                                                       # Function to login into the account..                                                                                                 

    try:                                                                                            # Declaring a try block to handle errors
        print("Id Already Exits?")
        print("1. Yes")
        print("2. No")
        enter_wish=int(input("Enter a option to proceed.\n"))                                       # Asks user as per his wish and will perform the action
        if enter_wish==1:                                                                           # This is the option if he press 1
            enter_user_id=input("Enter User Name\n")                                                # Asks user to input User-id
            if enter_user_id in dictionary["User_id"]:                                              # Checking whether such id exists in dictionary
                enter_password=input("Enter Password\n")                                            # Asks user to enter password
                if enter_password in dictionary["Password"]:                                        # matching of the password of particular id from dictionary
                    print("Login Successful...")                                                    # if passwords matches then user will get a message ["Logged in successful"]
                else:
                    print('Wrong user id or password.')                                             # if failure occurs then.
            else:
                print("Invalid user id or you are not a member of the club.\nPlease create an Id")  # Throwing an error to the user



        elif enter_wish==2:                                                                         # if user enter that no id and password exists with in the database
            create_id=input("Enter New Id\n")                                                       # Asks user to create the user id as per their wish
            print("Validating to database whether such id password exits or not")       
            time.sleep(1)                                                                           # Just to show that works smoothly
            create_password=input("Create new password.\n")                                         # Asks user to create password
            confirm_password=input("Confirm the entered password\n")                                # Asks user to confirm password    
            if create_password==confirm_password:                                                   # Checking of password and confirm password.
                print("Storing into database for further access.")
                time.sleep(1)
                dictionary.update({"User_id":create_id,"Password":confirm_password})                # Storing to the lists with the help of dictionary
                credentials.append(dictionary)
            else:
                print("Try Again...")
                login()
            
        else:
            print("No option mentioned such like that please re-enter the number.")
    
    except Exception as e:                                                                          # catching an exception , if any error exits.                                                                                  
        print("There is an error please try again....",e)
        login()

login()
while True:
    print("1. Book Rooms")
    print("2. Check My Booking")
    print("3. Cancel Booking")
    print("4. Logout")
    enter_choice=int(input("What Would you like to do\n"))
    if enter_choice==1:
        book_rooms()
    elif enter_choice==2:
        check_booking()
    elif enter_choice==3:
        cancel_booking()
    elif enter_choice==4:
        print("logging out")
        time.sleep(3)
        del[dictionary]
        break
    else:
        print("Invalid Input..")