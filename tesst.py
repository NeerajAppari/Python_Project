##import lm as m
import ok2 as q
def bank():
    print("Welcome to IBA Inkat Banking App")
    print("\t\t\tNote:This app is only for employees")

    print("[create account]\n press '1' in Request")

    
    print("[login account] \n press '2' in Request")



    Request=input("1/2:")
    for v in Request:
        if v=="1":
            print("~"*25)
            print("Create account")
            sign1()
            
        elif Request=="2":
            print("~"*25)
            print("Register a login ID first")            
            sign1()
##            RegisLoginID=input("please enter loginid")
##            RegisPassword=input("please enter password")
##            
##            if RegisLoginID==LoginID and RegisPassword==Password:
##                print("Sucessful")
##
##            else:
##                print("Wrong")

        else:
            print("~"*25)
            print("please choose the given option")

    


def create_account():

    print("~"*56)


    
    print("Successful")
    LoginID=input("Please enter your login id:")
    Password=input("Please enter your password:")
    print("LoginID:",LoginID)
    print("Password:",Password)
    print("~"*56)

    print("if details are proper press 1 to proceed")
##    print("if details are wrong press 2 to go to start")
##    print("to go back to previous page press 3")
    print("~"*56)


    Request2=input("1:")

    for i in Request2:
        if Request2=="1":
            print("Account created")
            print("~"*56)
            return (LoginID,Password)
            bank()
            
##        elif Request2=="2":
##            print("~"*25)
##            print("Going back to start")
##            bank()
####        elif Request2=="3":
####            print("~"*56)
####            print("Previous page")
####            bank()
        else:
            print("~"*56)
            print("please enter a valid option")
      


def sign1():

    LoginID,Password = create_account()
    RegisLoginID=input("please enter loginid")
    RegisPassword=input("please enter password")
    if RegisLoginID==LoginID and RegisPassword==Password:
        print("Sucessful")
        q.ok1()

    else:
        print("Wrong")



    
    



bank()

    
