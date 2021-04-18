# create record
#update record
#read record
#delete record
# CRUD  - All above is call CRUD operations


# find user
import os
import Validation
user_db_path = "D:/Python/FredProject/data/userRecord/"

def create(accountNumberFromUser, first_name, last_name, email, password):
    
    completion_state = False

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_accountNumber_exist(accountNumberFromUser):
        return False

    if does_email_exist(email):
        print("User already exist")
        return False

    completion_state = False

    try:
       f = open(user_db_path + str(accountNumberFromUser) + ".txt", "x")
      
    except FileExistsError:
        # delete the already created file, and print out error, then return false
        does_file_contain_data = read(user_db_path + str(accountNumberFromUser) + ",txt")
        if not does_file_contain_data:
            delete(accountNumberFromUser)

        # do to - check content of file b4 deleting

       # delete(accountNumber)
        

    else:
        f.write(str(user_data))
        completion_state = True

    finally:
        f.close()

        return completion_state

    # create a file
    # name of the file would be accountNumber.txt
    # add the user details to the file
    # return True
    # if saving to file fails, then delete created file

def read(accountNumberFromUser):
    
    # find user with account number
    # fetch content of the file
    is_valid_account_number = Validation.accountNumberValidation(accountNumberFromUser)

    try: 

        if is_valid_account_number:
            f = open(user_db_path + str(accountNumberFromUser) + ".txt", "r")
        else:
            f = open(user_db_path + str(accountNumberFromUser), "r")

    except FileNotFoundError:
        print("User not found")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()

    return False


def update(accountNumberFromUser):
    print("update user record")

    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(accountNumberFromUser):
    

    # find user with account number 
    # delete the user record (file)
    # return True
    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(accountNumberFromUser) + ".txt"):

        try: 

            os.remove(user_db_path + str(accountNumberFromUser) + ".txt")
            is_delete_successful = True

        except  FileNotFoundError:

            print("User not find")

        finally:

            return is_delete_successful


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def does_accountNumber_exist(accountNumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(accountNumber) + ".txt":
            return True
    return False


def authenticated_user(accountNumber, password):
    if does_accountNumber_exist(accountNumber):
       user = str.split(read(accountNumber), ',')
       if password == user[3]:
           return user

    return False

def accountBalance():
    print("Account balance")
   #get_user = read(account_balance)
    


    # find user record in the data folder


#does_email_exist('ifred1642@yahoo.com')

#delete(6661444642)
#print(read(2379025857))

