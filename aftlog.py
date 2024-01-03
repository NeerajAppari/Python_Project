from custacc import *
from entercd import *
def nexts():

    print("\t\t\tCUSTOMER MENU")
    
    

    print("\t\tTYPE 1 TO CREATE A NEW CUSTOMER ACCOUNT")
    print("\t\tTYPE 2 TO FILL IN THE DETAILS IN CUSTOMER ACCOUNT  (create an account first)")
    print("\t\tTYPE 3 TO EXIT")

    step2=input("1/2/3:")

    if step2=='1':
        print()
        print("*"*80)
        print("create customer account")
        print("*"*80)
        print()
        cacc()
        

    elif step2=='2':
        print()
        print("~"*80)
        print("Enter customer details")
        print("~"*80)
        print()
        Entdetails()
        

    elif step2=='3':
        print()
        print("`"*80)
        print("TO exit")
        print("`"*80)
        print()
        exit()

    else:
        print()
        print("!"*80)
        print("Wrong input please try again")
        print("!"*80)
        nexts()
        
    
