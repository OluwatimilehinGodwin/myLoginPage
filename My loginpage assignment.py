anewList=[{"NAME":"GODWIN",
           "PASSWORD":7232,
           "AGE":15,
           "SEX":'M'},
          {"NAME":"TENI",
           "PASSWORD":2463,
           "AGE":194,
           "SEX":'F'},
          {"NAME":"NIKE",
           "PASSWORD":8205,
           "AGE":13,
           "SEX":'M'}
          ] #here's my little database :)

def repeat(): #this function calls the login function again
    login()
def login(): #function that asks and allows user's access to page
    firstName = input("Enter your name: ")
    firstName=firstName.upper()
    passwrd = int(input("Enter password: "))
    foundname = False #helps to check if name has been found
    for item in anewList:
                if (item["NAME"]==firstName):
                    foundname = True #confirms that name has been found 
                                     #before even checking password correctness
                    if (item["PASSWORD"]==passwrd):
                        print(f"welcome to our page {firstName}")
                        break
                    else: #allows user to try logingin again if they want to
                        print("invalid password\n")
                        tryagain=input("Would you like to try again, Yes/No?: ")
                        if (tryagain.lower() =="yes"):
                            repeat()
                        else:
                            break
                        
                else:
                    continue
    if (not foundname):
        print(f"Unable to find profile with the name {firstName}")
        tryagain=input("Would you like to try again, Yes/No?: ")
        if (tryagain.lower() =="yes"):
            repeat()
        
login()
    