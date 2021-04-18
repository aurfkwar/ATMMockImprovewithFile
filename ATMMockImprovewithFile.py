#use Functions,  Include register, and login, Generate Account Number
import os
import sys
import random
import Validation
import database
from getpass import getpass
import datetime
x = datetime.datetime.now()
user_authSession_path = "D:/Python/FredProject/data/authSession/"

def init():

     print("Welcome to BankATM MOCK Improve")

     haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
     if(haveAccount == 1):
        
        login()
     elif(haveAccount == 2):
        
        register()

     else:
         print("You have selected invalid option")
         init()
def login():

    print("********* Login ********** ")
    accountNumberFromUser = (input("Enter your account number: \n"))

    is_valid_account_number = Validation.accountNumberValidation(accountNumberFromUser)
        
    if is_valid_account_number:
        password = getpass("Enter your password \n")
             #password = (input("Enter your password \n"))
           
        user = database.authenticated_user(accountNumberFromUser, password)

        if user:
                # create a file to keep track of user login in authSession folder
                f1 = open(user_authSession_path + str(accountNumberFromUser) + ".txt", "x")
                f1.write(str(user))
                

                bankOperations(user)
    
def register():
    print("****** Register ******")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password \n")

    accountNumber = generationAccountNumber()
    is_user_created = database.create(accountNumber, first_name, last_name, email, password)

    if is_user_created:
    

        print("Your Account has been created")
        print("== === ==== ==== ===")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe") 
        print("== === ==== ==== ===")

        login()
        
    else:
        print("Something went wrong, please try again")
        register()
       
def bankOperations(user):
    #user = database.read(accountNumber)
    #user = str.split(read(accountNumber), ',')
    print("Welcome %s %s" % (user[0], user[1]))
    print('Login time: %s' % x)
    print('These are the available options: ')
    print('1 Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
          
    isValidOptionSelected = False
    while isValidOptionSelected  == False:
        selectedOption = int(input('Please select an option: 1 (Withdrawal) 2 (Cash Deposit) 3 (Complaint) 4 (Logout) \n'))
        #    for selectedOption in range(0, 4):
        if(selectedOption == 1):
                isValidOptionSelected  == True
                withdrawalOperations(user)   
              
        elif(selectedOption == 2):
                isValidOptionSelected  == True
                cashDepositOption(user)
                                 
        elif(selectedOption == 3):
                isValidOptionSelected  == True
                complaintOption(user)
                
            
        elif(selectedOption == 4):
                isValidOptionSelected == True
                Logout()
                
            
        else:
            print('Invalid Option selected, please try again')
            #bankOperation(user)  
 
    else:
             print('Name or password incorrect, please try again') 
             login()            
          
def withdrawalOperations(user):
    # Save account balance in a file during withdrawal
    print('you selected option 1: Withdrawal \n')
    amount = float(input("\nHow much would you like to withdraw: "))
    Confirm = input("Is this the correct amount, Yes or No ? " + str(amount) + " \n")
    if Confirm == "Y":            
             print('take your cash')
             nextAction(user)

def cashDepositOption(user):
    #Save account balance in a file during Deposit
     print('you selected option 2: Deposit \n')
     #get_user = database.read(accountNumberFromUser)

     depositAmount = float(input("How much would you like to deposit? "))
     get_user = database.read(depositAmount)          
     get_user_balance = str.split(get_user, ',')[4]
     current_user_balance = get_user_balance + depositAmount
     get_user[4] = current_user_balance
     print("Your current balance is: %s cash" % get_user) 
     nextAction(user)
               
def complaintOption(user):
    print('you selected 3: Complaint \n')
    print(input("\nWhat issue will you like to report? "))
    print("Thanks for contacting us")
    nextAction(user)

def generationAccountNumber():
    #print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)

def Logout():
     # delete the user file from authSession folder when user logout
        accountNumberFromUser = open(user_authSession_path + ".txt", "r")   
        is_user_logout_successful = False
    
        if os.path.exists(user_authSession_path + str(accountNumberFromUser) + ".txt"):

            try: 

                os.remove(user_authSession_path + str(accountNumberFromUser) + ".txt")
                
                is_user_logout_successful = True

            except  FileNotFoundError:

                print("User file not found")

            finally:

                return is_user_logout_successful
            init()

        

def nextAction(user):
    EndTransaction = int(input("What will you like to do next? 1 (End) 2 (selectAnotherOption) \n" ))
    if(EndTransaction == 1):
        
        Logout()
    elif(EndTransaction == 2):
        
        bankOperations(user)
   

def Exit():
    print("Thanks for Banking with us")
    exit()
init()            
                
            


    
       
    
       
   
        
        

 