


import os
def newac():
    print("\t\t\tNEW ACCOUNT")
    print("Please enter the verification code provided to you by the company")
    print("\t\t\t\t\t\t[note:verifcation code is required so only employees have access]")
    vericd=input("CODE:")
    veriex=vericd+".txt"
    if os.path.exists(veriex):
        print("Verification Succesfull")
    else:
        print("Failed")
        newac()
    

    
    name  = input("Enter Your Firstname: ")

    login = input("Enter Your Login : ")
    pwd = input("Enter Your Password : ")

    PersonalFile = "login"+login+pwd+".txt"
    with open(PersonalFile, 'w')as pf:
        pf.write(name)
        print(PersonalFile+ " CREATED")
        print()
        print("#"*80)
        print("Your Account Has Been Successfully Created")
        print("#"*80)
        print()

from bankmain import *
bankm()
        


        



    

