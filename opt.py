import os
def operations():
    
    print("\t\t\tACCOUNT DETAILS")
    cname2=input("Enter customer's  name:")
    print()
    cacno2=input("Enter customer's account no:")
    print()
    AccountFile1= "cbalance"+cname2+cacno2+".txt"
    TransactionFile1 = "ctrans"+cname2+cacno2+".txt"

    if os.path.exists(AccountFile1):
        print("Customers details are correct proceding for transactions")
        Balancedep=input("Total ammount of money deposited:")
        with open (AccountFile1,'w') as af2:
             af2.write(Balancedep)
        af2.close()
        om(AccountFile1,TransactionFile1,Balancedep)
    else:
        print("Please check the given information again")
        operations()

def om(ab,ab1,Balancedep):
        print()
        print("~"*80)
        print("\t\t\tTYPE 1 TO PROCEED FOR TRANSACTIONS")
        print("\t\t\tTYPE 2 TO GO BACK TO MAIN MENU")
        print("~"*80)
        print()
        
        nextopt=input("1/2:")
        if nextopt=='1':
            print("/"*100)
            print("\t\t\tOPERATIONS")
            print("\t\t\tTYPE 1 FOR WITHDRAWAL")
            print("\t\t\tTYPE 2 FOR DEPOSIT")
            print("\t\t\tTYPE 3 FOR CHECKBALANCE")
            print("\t\t\tTYPE 4 FOR TRANSACTIONS")
            print("\t\t\tTYPE 5 DELETE ENTIRE FILE")
            print("\t\t\tTYPE 6 TO GO BACK TO MAIN MENU")
            print("/"*100)
            whcopt=input("1/2/3/4/5:")
            
            if whcopt=='1':
                with open (ab,'w') as bal1:
                    print("-"*80)
                    print("\t\t\tWITHDRAWAL")
                    print("-"*80)
                    print("Current ammount",bal1)
                    withdrawa=input("Enter ammount to withdraw :")
                    if withdrawa<=Balancedep:
                       final_ammount=int(Balancedep)-int(withdrawa)
                       print('Current Balance :',final_ammount)

                       bal1.write(str(final_ammount))
                    else:
                       print()
                       print('Insufficient WithDrawal Balance!')
                       om(ab,ab1,Balancedep)

                with open(ab1,'a') as tbal1:
                    tbal1.writelines(f'\n {str(final_ammount)}')
                    om(ab,ab1,Balancedep)
            elif whcopt=='2':
                print("-"*80)
                print("\t\t\tDEPOSIT")
                print("-"*80)
                with open (ab,'w') as bal2:
                    print("Current ammount",bal2)
                    deposita=input("Enter current ammount to deposited:")
                    
                    final_ammount=int(Balancedep)+int(deposita)
                    print(final_ammount)

                    bal2.writelines(str(final_ammount))
                bal2.close()

                with open(ab1,'a') as tbal2:
                    tbal2.writelines(f'\n{str(final_ammount)}')
                    om(ab,ab1,Balancedep)

            elif whcopt=='3':
                print("-"*80)
                print("\t\t\tCURRENT BALANCE")
                print("-"*80)
                balc=open(ab,'r')
                print(balc.read())#show balance
                om(ab,ab1,Balancedep)
            elif whcopt=='4':
                print("-"*80)
                print("\t\t\tTRANSACTIONS")
                print("-"*80)
                tbal3=open(ab1,'r')
                print(tbal3.read())
                om(ab,ab1,balancedep)
##                with open (ab1,'r') as tbal3:
##                    transckh=tbal3.readlines()#transaction
##                    print(transckh)
##                    om(ab,ab1,Balancedep)
##
            elif whcopt=='5':
                print("-"*80)
                print("\t\t\tDELETING FILE")
                print("-"*80)
                if os.path.exists(ab):
                    os.remove(ab)
                    print(ab,'Deleted')
                    print()
                else:
                    print()
                    print("Sorry file not found")
                    om(ab,ab1,Balancedep)

            elif whcopt=='6':
                print("Going back to main menu")
                
                

            else:
                print("Please choose a correct option")
                om(ab,ab1,Balancedep)
        else:
            print("~"*80)
            print("\t\t\tgoing back to main menu")
            print()
    
                    
                

                
    

                
                
