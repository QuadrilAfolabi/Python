class Bank_app():
    def __init__(self):
        def login():
            user_details ={}
            print("Login into your account>>")
            username =(input("Enter your Username>>").lower())
            password = (input("Enter your Password>>>"))
            users = (input("Enter your Username>>").lower())
            passcode = (input("Enter your Password>>>"))
            user_details["Username"] = username
            user_details["Password"]= password
            print(user_details)
            if users == username and passcode ==password:
                print("Login Successfull")
                print(f'Welcome back {username} \n')
            else:
                    print("invalid details \nForgotten password?")
                    reset = input("Click>>>")
                    if reset == "Forgotten password":
                        email_check = input("enter your email>>>>>")
                        if email_check == "raw@gmail.com":
                            new_pass = input("New Password>>>")
                            con_pass = input("Confirm Password>>")
                            if con_pass == new_pass:
                                print("You have successfully reset your password. \nLogin into your account.")
                                username =(input("Enter your Username>>").lower())
                                password = (input("Enter your Password>>>"))
                                users = (input("Enter your Username>>").lower())
                                passcode = (input("Enter your Password>>>"))
                                if users == username and passcode ==password:
                                    print("Login Successfull")
                                    print(f'Welcome back {username} \n')
                    
                            
                    
        # login()
    
        def menu():
            account_balance = 1000000
            home_menu=('''

            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Transfer
            5. Purchase Airtime
            6. Confirm cheque/Cheque deposit
            7. Reset Password
            8. Speak with the customer service representative
            9. End

            '''
            )
            print("Account Balance:", account_balance, home_menu)
            option = input("Select an Options:  ")
            if option == "1" :
                print(f"Your account balance is: {account_balance}" )
                ask = input("Do you want to perform another transaction?").lower()
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")
                  
            elif option == "2":
                deposit = int(input("Enter the amount your want to deposit>>>"))
                account_balance += deposit
                print(f"Your deposit has been made \nYour balance is: {account_balance}")
                ask = input("Do you want to perform another transaction?").lower()
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")
            elif option == "3":
                withdrawal = int(input("Enter the amount you want to withdraw>>>"))
                account_balance -= withdrawal
                print(f"Withdrawal Successful \nYour balance is: {account_balance}")
                ask = input("Do you want to perform another transaction?").lower()
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")
            elif option == "4":
                acc = int(input("enter the account name you want to transfer to >>>"))
                amount = int(input("Enter the amount you want to transfer>>>"))
                account_balance -= amount
                print(f"Transfer Successful. \nYour balance is {account_balance}")
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")

            elif option == "5":
                airtime = int (input("enter the amount of airtime you want to purchase>>"))
                account_balance -= airtime 
                print(f"Airtime purchase was successful \nYour new balance is: {account_balance}")
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")
            elif option == "6":
                print("Enter details of the cheque to be confirmed below:")
                cheque_details ={}
                chq_no = int(input("Enter the cheque number>>"))
                issue_date =  (input("Enter the issuance date>>"))
                ben_name = input ("Enter the Beneficiary name>>")
                amt_on_chq = int (input("Enter the amount on check>>>"))
                cheque_details['Cheque number'] = chq_no
                cheque_details["Cheque issue date"] = issue_date
                cheque_details["Beneficiary Name"] =ben_name
                cheque_details ["Amount on the cheque"] = amt_on_chq
                account_balance += amt_on_chq
                print(cheque_details)
                print(f'Your cheque has een confirmed and successful deposited into your account \nYour balance is {account_balance}. \nThank you for banking with us.')
                if ask ==("Yes").lower():
                    menu()
                else:
                    print("Thanks for banking with us.")
            elif option == "7":
                current_pass = input("Current password>>")
                if current_pass == "4233":
                    new_pass = input("New Password>>>")
                    con_pass = input("Confirm Password>>")
                    if con_pass == new_pass:
                        print("You have successfully reset your password. \nLogin into your account.")
                    else:
                        print(f"paasword not tally with the New password. Try again!")
                        new_pass = input("New Password>>>")
                        con_pass = input("Confirm Password>>")
                        if con_pass == new_pass:
                            print("You have successfully reset your password. \nLogin into your account.") 
                            login()
                            menu()
            elif option == "8":
                print("Your request has been accepted and you have been transferred to our available customer care representative.")
            elif option == "9":
                print ("Thank you for banking with us.")
        # menu()
        def home():
            print ("Welcome to City Bank")
            reg ={}
            query = (input("Are you a New User or Old User>>>").lower())
            if query == (("New User").lower()):
                print("Register your Account>>")
                first_name = input("Enter your first name>>").lower()
                last_name = input ("Enter your last name>>").lower()
                email = input("enter your email address>>").lower()
                phone = int(input("Enter your phone>>>"))
                username =(input("Enter your Username>>").lower())
                password = (input("Enter your Password>>>"))
                reg[username]= password
                reg["First name"] = first_name
                reg["Last name"] = last_name
                reg ["Email"] = email
                reg["Phone"] = phone
                print(reg)
                print("Registration Complete.")
                print("Login into your Account.")
                users = (input("Enter your Username>>").lower())
                passcode = (input("Enter your Password>>>"))
                if users == username and passcode ==password:
                    print("Login Successfull")
                    menu()
            elif query == (("Old User").lower()):
                login()
                menu()
            else:
                print("invalid")
        home()

Bank_app()


