# import any necessary libraries/scripts here
from additional_exceptions import InvalidAccount, InvalidPinNumber, InvalidATMCard, InsufficientFunds, AccountNotFound

def atm_app(atm) -> None:
    """ATM idle mode, this is the state when there is no card inserted.
After card is inserted, ATM will prompt for pin number and verify it
If card and pin are valid, ATM will transition to atm_menu_sys,
otherwise display error message"""
    while True:
        print("Welcome to XX bank\n")
        print("Choose an option:")
        print("1. Insert ATM card")
        print("2. Exit")
        idle_option = input("Enter option: ").strip()
        if idle_option == "1":
            #Insert card by entering card number
            print()
            card_num = input("Please enter card number: ").strip()
            try:
                atm.check_card(card_num)
                #print(atm.get_current_card)
                print()
                pin = input("Please enter your pin number: ").strip()
                try:
                    #verify the entered pin
                    atm.check_pin(pin)
                    print("\nTransaction in progress...\n")
                    #go to the atm menu sys if pin is correct
                    atm_menu_sys(atm)
                except InvalidPinNumber as e:
                    #invalid pin number is entered
                    print()
                    print(e)
                    print()
            except InvalidATMCard as e:
                #invalid card number is entered
                print()
                print(e)
                print()

        elif idle_option == "2":
            #Exit the ATM application
            print("\nClosing application...\nApplication closed")
            break
        else:
            #For all other input that is not recognized
            print("\nInvalid option, please try again.\n")
            continue


def atm_menu_sys(atm) -> None:    
    while True:
        #atm main menu
        print("Select a transaction")
        print("1. Balance enquiry")
        print("2. Cash withdrawal")
        print("3. Fund transfer")
        print("4. Exit")
        txn_option = input("Enter option: ").strip()
        
        if txn_option == "1":
            #Select balance enquiry
            #If only 1 account show default account
            if not atm.check_accts():
                print()
                print(atm.show_balance("savings"))

            else:
                print("\nBalance enquiry")
                print("Select account type:")
                print("1. Current Account")
                print("2. Savings Account")
                
                #Ask for account type, any option other than 1 or 2 is consider press cancel            
                acct_type_option = input("Select account: ").strip()
                if acct_type_option == "1":
                    acct_type = "current"
                elif acct_type_option == "2":
                    acct_type = "savings"
                else:
                    print("Transaction cancelled\n")
                    continue

                print()
                print(atm.show_balance(acct_type))
                #go back to list of transaction selection

        elif txn_option == "2":
            #Select cash withdrawal
            #If only 1 account ask for withdrawal amount
            if not atm.check_accts():
                txn_amount = input("\nSelect amount: ").strip()
                #withdraw from account if enough balance
                try:
                   atm.transactions("withdrawal", txn_amount, "savings")
                except ValueError as e:
                    #check that the input is a valid amount
                    #at most 2 decimal place and more than 0
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                except InsufficientFunds as e:
                    #withdrawal amount > account balance
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                else:
                    #successful withdrawal, show updated balance and exit from menu
                    print("Card returned")
                    print(atm.show_balance("savings"))
                    break

            else:    
                print("\nCash withdrawal")
                print("Choose account:")
                print("1. Current Account")
                print("2. Savings Account\n")

                #Ask for account type, any option other than 1 or 2 is consider press cancel 
                acct_type_option = input("Select account: ").strip()
                if acct_type_option == "1":
                    acct_type = "current"
                elif acct_type_option == "2":
                    acct_type = "savings"
                else:
                    print("Transaction cancelled")
                    continue

                txn_amount = input("\nSelect amount: ").strip()

                #withdraw from account if enough balance
                try:
                   atm.transactions("withdrawal", txn_amount, acct_type)
                except ValueError as e:
                    #check that the input is a valid amount
                    #at most 2 decimal place and more than 0
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                except InsufficientFunds as e:
                    #withdrawal amount > account balance
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                else:
                    #successful withdrawal, show updated balance and exit from menu
                    print("Card Returned")
                    print(atm.show_balance(acct_type))
                    break

        elif txn_option == "3":
            #Select Fund transfer
            #If only 1 account ask for withdrawal amount
            if not atm.check_accts():
                #transfer to other account, input account number
                trans_acct_num = input("\nEnter account number to transfer funds to: ")

                #check if this account number exists by checking with bank
                try:
                    trans_acct = atm.bank.get_acct(trans_acct_num)
                except AccountNotFound as e:
                    #no such account exists in the bank
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                    continue
                else:
                    try:
                        txn_amount = 0
                        #Uncomment below 3 lines to check the input being passed
                        #print(acct_type)
                        #print(atm.get_current_card().access(acct_type))
                        #print(trans_acct)
                        atm.transactions("transfer", txn_amount, "savings",
                                        trans_acct)
                    except InvalidAccount as e:
                        #If transfer from and transfer to account is the same,
                        #print error message invalid account and cancel transaction
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                        continue

                    #transfer to account ok, enter the transfer amount
                    txn_amount = input("\nSelect amount: ").strip()
                    try:
                        atm.transactions("transfer", txn_amount, "savings",
                                        trans_acct)
                    except ValueError as e:
                        #check that the input is a valid amount
                        #at most 2 decimal place and more than 0
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                    except InsufficientFunds as e:
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                    else:    
                        #successful transfer, show updated balance
                        #return card and exit from menu
                        print("Card Returned")
                        print(atm.show_balance("savings"))
                        break
            else:
                #Select account options to transfer from,
                #any option other than 1,2,3 is considered press cancel
                print("\nChoose account to transfer from:")
                print("1. Current Account")
                print("2. Savings Account")

                #Ask for account type, any option other than 1 or 2 is consider press cancel 
                acct_type_option = input("Select account: ").strip()
                if acct_type_option == "1":
                    #Transfer from current account
                    acct_type = "current"
                elif acct_type_option == "2":
                #Transfer from savings account
                    acct_type = "savings"
                else:
                    print("Transaction cancelled\n")
                    continue

                print("\nChoose account to transfer to:")
                print("1. Current Account")
                print("2. Savings Account")
                print("3. Other Account")

                #Select account options to transfer to,
                #any option other than 1,2,3 is considered press cancel
                acct_type_option = input("Select account: ").strip()

                if acct_type_option == "1":
                    #transfer to own current account
                    trans_acct_type = "current"
                    trans_acct = atm.get_current_card().access(trans_acct_type)
                    #For transfer to own current and savings account,
                    #check if transfer from and transfer to account is the same
                    try:
                        txn_amount = 0
                        atm.transactions("transfer", txn_amount, acct_type, trans_acct)
                    except InvalidAccount as e:
                        #If transfer from and transfer to account is the same,
                        #print error message invalid account and cancel transaction
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                        continue

                elif acct_type_option == "2":
                    #transfer to own savings account
                    trans_acct_type = "savings"
                    trans_acct = atm.get_current_card().access(trans_acct_type)
                    #For transfer to own current and savings account,
                    #check if transfer from and transfer to account is the same
                    try:
                        txn_amount = 0
                        atm.transactions("transfer", txn_amount, acct_type, trans_acct)
                    except InvalidAccount as e:
                        #If transfer from and transfer to account is the same,
                        #print error message invalid account and cancel transaction
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                        continue
    
                elif acct_type_option == "3":
                    #transfer to other account, input account number
                    #possible to key in own account number
                    trans_acct_num = input("\nEnter account number to transfer funds to: ")

                    #check if this account number exists by checking with bank
                    try:
                        trans_acct = atm.bank.get_acct(trans_acct_num)
                    except AccountNotFound as e:
                        #no such account exists in the bank, return to main menu
                        print(f"\n{e}")
                        print("Returning to main menu\n")
                        continue
                    else:
                        try:
                            txn_amount = 0
                            #Uncomment below 3 lines to check the input being passed
                            #print(acct_type)
                            #print(atm.get_current_card().access(acct_type))
                            #print(trans_acct)
                            atm.transactions("transfer", txn_amount, acct_type,
                                            trans_acct)
                        except InvalidAccount as e:
                            #If transfer from and transfer to account is the same,
                            #print error message invalid account and cancel transaction
                            print(f"\n{e}")
                            print("Returning to main menu\n")
                            continue
                
                else:
                    print("Transaction cancelled\n")
                    continue

                #transfer to account ok, enter the transfer amount
                txn_amount = input("\nSelect amount: ").strip()
                try:
                    atm.transactions("transfer", txn_amount, acct_type, trans_acct)
                except ValueError as e:
                    #check that the input is a valid amount
                    #at most 2 decimal place and more than 0
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                except InsufficientFunds as e:
                    print(f"\n{e}")
                    print("Returning to main menu\n")
                else:    
                #successful transfer, show updated balance
                #return card and exit from menu
                    print("Card Returned")
                    print(atm.show_balance(acct_type))
                    break

        elif txn_option == "4":
            #Exit main menu and return card to customer
            print("\nTransaction cancelled, please take your card.")
            print("Thank you for using XX bank ATM.\n")
            atm.set_current_card(None)
            break
        
        else:
            print("Invalid option, please try again.\n")