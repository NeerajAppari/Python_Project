import os
from opt import *
def Entdetails():
    print("\t\t\tCUSTOMER DETAILS")
    cname1 = input("Enter Customer's Name : ")
    clogin1 = input("Enter Customer's loginID : ")
##    cacno1 = input("Enter Customer's Account no:")
    CustomerFile1 = "caccount"+clogin1+cname1+".txt"
##    AccountFile1= "cbalance"+cname1+cacno1+".txt"  
    if os.path.exists(CustomerFile1):
        print("Customer file identified")
        print("Proceedind to fill the details")

        print()
        print()
        print("/"*80)
        print("\t\tTYPE 1 TO FILL PERSONAL DETAILS")
        print("\t\tTYPE 2 TO FILL ACCOUNT DETAILS")
        print("\t\tTYPE 3 TO EXIT")
        print("\t\tTYPE 4 TO GO BACK TO MAIN MENU")
        print("/"*80)
        pORa=input("1/2/3/4:")
        if pORa =='1':
            print("\t\t\tPERSONAL DETAILS")
            print("proceeding to fill perosnal details")
            print("-"*80)
            with open (CustomerFile1,'w') as cf2:
                Cfname=input("Enter customer's first name")
                Clname=input("Enter customer's last name")
                Cphoneno=input("Enter customer's phone number")
                Caddress1=input("Enter customer's address")
           
            


                cf2.writelines(Cfname+'\t')
                cf2.writelines(Clname+'\t')
                cf2.writelines(Cphoneno+'\t')
                cf2.writelines(Caddress1+'\t')
                Entdetails()
                
        elif pORa=='2':
            print()
            print("\t\tACCOUNT DETAILS")
            print("Proceeding to fill account details")
            print("-"*80)
            operations()
##            with open (AccountFile1,'w') as af2:
##                Balancedep=input("Total ammount of money deposited:")
##
##                af2.writelines(Balancedep)

        elif pORa=='3':
            print("Proceeding to exit")
            exit()
        elif pORa=='4':
            print("Going back to main menu")


        else:
            print()
            print("!"*80)
            print("Wrong statements please type correct value")
            print()
            print("!"*80)

    
        
    else :
        print("There is no customer account with this following details\n please check details again")
        print()
        print("-"*80)
        Entdetails()

##
##def Entdetails2
##    with open (Customerfile1,'w') as cf2:
##        Cfname=input("Enter customer's first name")
##        Clname=input("ENter customer's last name")
##        Cphoneno=input("Enter customer's phone number")
##
##
##        cf2.writelines(Cfname)
##        cf2.append(Clname)
##        cf2.append(Cphoneno)
##        
