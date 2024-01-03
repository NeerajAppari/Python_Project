import os
from aftlog import *
def chklog():
    print()
    print("ENTER LOGIN ID")
    print("~"*80)
    login1 = input("Enter Your login : ")
    pwd1 = input("Enter Your password : ")
    print()
    print("~"*80)
    PersonalFile1 = "login"+login1+pwd1+".txt"
    if os.path.exists(PersonalFile1):
        print()
        print("~"*80)
        print("login Successfull")
        print()
        print("~"*80)
        nexts()
    else :
        print("!"*80)
        print("Login Unsucessful")
        print("!"*80)
        print()
        chklog()

    































##    
##    print("For security reasons you are only allowed 'Three' wrong attempts\n if you fail to type correct information on 'Three' attempts your account will be blocked")
##    while True:
##        login1 = input("Enter Your login : ")
##        pwd1 = input("Enter Your password : ")
##        PersonalFile1 = "login"+login1+pwd1+".txt"
##        attempt=3
##
##
##        if os.path.exists(PersonalFile1):
##            print("login Successfull")
##            nexts()
##            
##            
##        elif attempt>1:
##            attempt=attempt-1
##            print("Try Again ",attempt,": more attempts only")
##            continue
##
##        else:
##            print("blocked")
##            break

