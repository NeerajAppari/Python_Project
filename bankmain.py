from newacc import *
from entlog import *
def bankm():
    

    print("_"*57)
    print("~"*57)
    print("~\t\t WELCOME TO INKAT BANKING APP\t\t~")
    print("~"*57)
    print("_"*57)

    print("press 1 to create an account")
    print("press 2 to login")
    print("press 3 to exit")

    opt=input("[1/2/3:]")

    if opt=='1':
        print("To create account")
        newac()
    elif opt=='2':
        print("To log into exixting account")
        chklog()
        
    elif opt=='3':
        print("to exit")
    else:
        print("wrong input please choose options again")
        bankm()

        


    

bankm()
    
    
