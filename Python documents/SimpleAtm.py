#################################
import time as s 

default_pin = 1111
default_balance = 50000.00
default_username = "CyberR"


print("Welcome to your bank account", default_username, end = "\n\n")

choice = 7


while True:
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Money")
    print("\t\t3. Logout And Quit")
    print("\t\t4. Deposit Money")
    choice = int(input("Enter any number:>"))
    print("\n")


    if choice == 3:
        print("Logging out and quiting....")
        s.sleep(2)
        print("You have been logged out. Thank You! \n")
        break

    elif choice in (1,2,4):
        tried_num = 3
        while(tried_num!=0):
            pin= int(input("Enter your 4 digit pin:>"))

            if pin == default_pin:
                print("Account Authorized. You can proceed with the transaction \n\n")
                
                if choice == 1:
                    print("Loading account balance.....\n")
                    s.sleep(3)
                    print("Your current balance is $",default_balance, end= "\n")
                    break
                elif choice == 2:
                    print("Opening money withdrawal")
                    s.sleep(2)

                    while(True):
                        withdraw = float(input("Enter the amount you wish to withdraw:>")) 
                        if withdraw > default_balance:
                            print("Can't withdraw $",withdraw, end= "\n")
                            print("Input a lower amount")
                            continue
                        else:
                            print("Withdrawing $",withdraw)
                            confirm = input("Confirm? Y/N >")
                            if confirm in ('Y', 'y'):
                                default_balance -= withdraw
                                s.sleep(1.5)
                                print("Amount Withdraw $",withdraw)
                                s.sleep(2)
                                print("Remainining balance $",default_balance, end= "\n\n")
                                break
                            else:
                                print("Cancelling transaction.....")
                                s.sleep(2)
                                print("Transaction Cancelled\n")
                                break
                    
                elif choice == 4:
                    print("Opening Deposit Page")
                    s.sleep(2)
                    deposit= float(input("Input how much you want to deposit to your account:>"))
                    confirm = input("Confirm? Y/N >")
                    if confirm in ('Y', 'y'):
                        default_balance += deposit
                        print("Depositing money......")
                        s.sleep(2.5)
                        print("Amount Deposit $",deposit)
                        s.sleep(2.5)
                        print("Updated Balance $",default_balance, end="\n\n")
                        break
                    else:
                        print("Cancelling Transaction.....")
                        s.sleep(1)
                        print("Deposit Cancelled. Thank You!")
                        break
                break

            else:
                print("incorrect pin..\nEnter the correct pin")
