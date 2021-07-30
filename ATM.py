import time
balance=25000
print("Welcome To ATM machine")
print("Please Swipe Your card")
time.sleep(5)
print("Your Card number is :-\n6521 0736 5780 2113 ")
verifycard=int(input("Is the card number ok ?\n1. Yes\n2. No\n"))    # Will ask user whether the card number is okay or not.
if verifycard==1:
    enterpin=int(input("Enter the ATM pin \n"))
    atmpin=1234
    if enterpin==atmpin:
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Transfer to account")
        print("4. Change ATM pin")
        print("5. Abort Transaction")    
        askuseraction=int(input("What would you like to do ?\n"))
        if askuseraction==1:                                                                # For Withdrawal
            withdrawalamount=int(input("Enter the amount you want to withdraw???\n"))       # Asking user to input the amount  that he wish to take
            if withdrawalamount>10000:                                                      # Applying condition that user can't take more than 10K
                print("withdrawal amount is 10000 per day ....")                            # Printing Error For user that he can't withdraw more than 10K
            else:
                print("Checking balance")                                                   # Just to manipulate the user
                time.sleep(5)                                                       
                balance=balance-withdrawalamount                                            # Updating the balance as user ask after withdrawal
                print(balance)                                                              # Printing Balance for the user so that he can see after withdrawal what amount is left
                print("Thanks for using ATM machine, Visit Again!!!!!!")                    # A good Bye Message from Machine
        
        elif askuseraction==2:                                                                # For displaying Balance to the user
            print(balance)
            print("Thanks for using ATM machine, Visit Again!!!!!!")
            exit
        
        elif askuseraction==3:                                                               # Asking for transfer
            enteraccountnumber=int(input("Enter the Account Number to whom you want to transfer\n"))
            entermobilenumberreceiver=int(input("Enter the Mobile Number to whom it is going to receive\n"))
            entermobilenumbersender=int(input("Enter Your Mobile number..\n"))
            confirmaccountnumber=int(input("Confirm the receiver account number.\n"))
            if confirmaccountnumber==enteraccountnumber:
                print("Account Number Matched..")
                withdrawalamount=int(input("Enter the amount you want to withdraw???\n"))
                print("Checking balance")
                time.sleep(5)
                balance=balance-withdrawalamount
                print(balance)
                print("Thanks for using ATM machine, Visit Again!!!!!!")
        
        elif askuseraction==4:                                                          # For changing Pin
            newatmpin=int(input("Enter new pin\n"))
            confirmnewpin=int(input("Confirm the new ATM pin\n"))
            if newatmpin==confirmnewpin:
                atmpin=confirmnewpin
                print("pin changed successfully..")
                print("Thanks for using ATM machine, Visit Again!!!!!!")
        
        elif askuseraction==5:                                                          # if user abort transcation
            print("Thanks for using ATM machine, Visit Again!!!!!!")
        
        else:
            print("Invalid input")
elif verifycard==2:
    print("Re-Insert the card..")
else:
    print("Invalid Input.")