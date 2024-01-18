from NewAcc import *
from ChkAcc import *

def BankMain():
    print("_____ Bank od YUYU _______")
    ch = int(input("1-- open new acccount\n2-- Login\0--Exit"))
    if ch == 1:
        #call new account method
        NewAccount()
    elif ch == 2:
        #call ti login method
        chkLogin()
    elif ch == 0:
        # call exit method
        pass
    else :
        print("Wrong Input try again")
        BankMain()

BankMain()
