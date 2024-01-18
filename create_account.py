
def create_account():
    
    print("To create an account you need a verfication code from manager")

    print("Please enter the verfication code")

    ##list verficatipn etc

    ##if  and else if right
    print("~"*56)


    print("Successful")
    LoginID=input("Please enter your login id:")
    Password=input("Please enter your password:")
    print("LoginID:",LoginID)
    print("Password:",Password)
    print("~"*56)

    print("if details are proper press 1 to proceed")
    print("if details are wrong press 2 to go to start")
    print("to go back to previous page press 3")
    print("~"*56)


    Request2=input("1/2/3:")

    if Request2=="1":
        print("Account created")
        print("~"*56)
        import bankintro
            
    elif Request2=="2":
        print("~"*25)
        print("Going back to start")
        create_account()
    elif Request2=="3":
        print("~"*56)
        print("Previous page")
        import bankintro
    else:
        print("~"*56)
        print("please enter a valid option")

    
create_account()
