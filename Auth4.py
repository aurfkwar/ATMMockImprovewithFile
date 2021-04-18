#register
# -First_name, last_name, username, password, email
# - generate user id
# generate user account

#login
# - accountNumber and password
# user input validation
#Error Handling

#bank operations

#Initializing the system
import random
import Validation
import database
from getpass import getpass


# database ={
#     6661444642: ['Fred', 'Kwa', 'ifred1642@yahoo.com', 'password', 200]
# }


def init():

    print("Welcome to BankPHP")

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
        
        #password = (input("Enter your password \n"))
        password = getpass("Enter your password \n")

        user = database.authenticated_user(accountNumberFromUser, password)

        if user:
             bankOperation(user)

        # for accountNumber,userDetails in database.read(accountNumberFromUser):
        #    if(accountNumber == int(accountNumberFromUser)):
        #       if(userDetails[3] == password):
                  

    
        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: Check that you have up to 10 digits and only integer")
        init()

    
def register():
    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password \n")

    
    
    accountNumber = generationAccountNumber()
    #prepared_user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
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

        
def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selectedOption = int(input("What will you like to do: (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
      depositOperations()
    elif(selectedOption == 2):
      withdrawalOperations()
    elif(selectedOption == 3):
      Logout()
    elif(selectedOption == 4):
      exit()
    else:
      print("Invalid option selected")
      bankOperation(user)

def withdrawalOperations():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdrawal balance
    # deduct withdrawn amount from current balance
    # display current balance

def depositOperations():
    print("Deposit")
    # get current balance
    # get amount to deposit
    # add deposit amount to current balance
    # display current balance



def generationAccountNumber():
    #print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)

def getAccountBalance(userDetails):
    return userDetails[4]

def Logout():
    login()

### ACTUAL BANKING SYSTEM

init()
