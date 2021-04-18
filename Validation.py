def accountNumberValidation(accountNumber):
    #check if account number is not empty
    #if account number is 10 digits
    # if the account number is an integer

    if accountNumber:
        

            try:
                int(accountNumber)

                if len(str(accountNumber)) == 10:
                  return True

                else:
                   # print("Account Number cannot be less or more than 10 digits")
                    return False
            except ValueError:
                    #print("Invalid Account Number, account number should be an integer")
                    return False
            except TypeError:
                #print("Invalid account type")
                return False
        
    
    else:
        print("Account Number is a required field")
        return False
