from newacc import *
from entlog import *
def bankm():
    

    print("_"*97)
    print("~"*97)
    print("~\t\t\t\t WELCOME TO INKAT BANKING APP \t\t\t\t\t~")
    print("~"*97)
    print("_"*97)
    print("\t\t\t\t\t\t\t\t\t\t(note:This app is only for employees)")

    print("\t\t\tTYPE 1 TO CREATE AN ACCOUNT")
    print("\t\t\tTYPE 2 TO LOGIN\t\t(To proceed making an account for customer)")
    print("\t\t\tTYPE 3 TO EXIT")
    print("\t\t\tTYPE 4 TO KNOW MORE ABOUT")

    opt=input("[1/2/3/4:]")

    if opt=='1':
        print()
        print("\t\t\tProceding To Create An Account")
        newac()
    elif opt=='2':
        print()
        print("\t\t\tProceding to logging into exixting account")
        chklog()
        
    elif opt=='3':
        print()
        print("Exiting")
        exit()

    elif opt=='4':
        print()
        print("*"*80)
        print("\t\tFirst you have to create an account,if you dont already have one")
        print("\t\tAfter creating account you can proceed to making account for customer")
        print("\t\tYou can update,delete as well check for transactions")
        print("*"*80)
        bankm()
    else:
        print()
        print("Wrong Input Please Choose Options Again")
        bankm()

        


    

bankm()
    
    
