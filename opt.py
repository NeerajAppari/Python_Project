import os
def operations():
    
    

    cname2=input("Enter customer's  name")
    cacno2=input("Enter customer's account no")
    AccountFile1= "cbalance"+cname2+cacno2+".txt"
    TransactionFile1 = "ctrans"+cname2+cacno2+".txt"

    if os.path.exists(AccountFile1):
        print("Customers details are correct proceding for transactions")
        with open (AccountFile1,'w') as af2:
                Balancedep=input("Total ammount of money deposited:")

##                af2.writelines(str(Balancedep))
                af2.close
                print()
                print("~"*80)
                print("\t\t\tTYPE 1 TO PROCEED FOR TRANSACTIONS")
                print("\t\t\tTYPE 2 TO GO BACK TO MAIN MENU")
                print("~"*80)
                print()
                
                nextopt=input("1/2:")
                if nextopt=='1':
                    print("\t\t\tOPERATIONS")
                    print("\t\t\tTYPE 1 FOR WITHDRAWAL")
                    print("\t\t\tTYPE 2 FOR DEPOSIT")
                    print("\t\t\tTYPE 3 FOR CHECKBALANCE")
                    print("\t\t\tTYPE 4 FOR TRANSACTIONS")
                    print("\t\t\tTYPE 5 DELETE ENTIRE FILE")
                    print("\t\t\tTYPE 6 TO GO BACK TO MAIN MENU")
                    whcopt=input("1/2/3/4/5:")
                    
                    if whcopt=='1':
                        with open (AccountFile1,'w') as bal1:
                            print("-"*80)
                            print("\t\t\tWITHDRAWAL")
                            print("-"*80)
                            print("Current ammount",bal1)
                            withdrawa=input("ENter current ammount to deposited")
                            
                            final_ammount=int(Balancedep)-int(withdrawa)
                            print(final_ammount)

                            bal1.writelines(str(final_ammount))

                        with open(TransactionFile1,'a') as tbal1:
                            tbal1.writelines(str(final_ammount))
                            operations()
                    elif whcopt=='2':
                        print("-"*80)
                        print("\t\t\tDEPOSIT")
                        print("-"*80)
                        with open (AccountFile1,'w') as bal2:
                            print("Current ammount",bal2)
                            deposita=input("ENter current ammount to deposited")
                            
                            final_ammount=int(Balancedep)+int(deposita)
                            print(final_ammount)

                            bal2.writelines(str(final_ammount))

                        with open(TransactionFile1,'a') as tbal2:
                            tbal2.writelines(str(final_ammount))
                            operations()

                    elif whcopt=='3':
                        print("-"*80)
                        print("\t\t\tCURRENT BALANCE")
                        print("-"*80)
                        with open (AccountFile1,'r') as bal3:
                            balckh=bal3.readlines()
                            print(balckh)#show balance
                            operations()
                    elif whcopt=='4':
                        print("-"*80)
                        print("\t\t\tTRANSACTIONS")
                        print("-"*80)
                        with open (TransactionFile1,'r') as tbal3:
                            transckh=tbal3.readlines()#transaction
                            print(transckh)
                            operations()

                    elif whcopt=='5':
                        print("-"*80)
                        print("\t\t\tDELETING FILE")
                        print("-"*80)
                        if os.path.exists(AccountFile1):
                            os.remove(AccountFile1)
                            print(AccountFile1,'Deleted')
                            print()
                        else:
                            print()
                            print("Sorry file not found")
                            operations()

                    elif whcopt=='6':
                        print("Going back to main menu")
                        
                        

                    else:
                        print("Please choose a correct option")
                        operations()
                else:
                    print()
                    print("\t\t\tgoing back to main menu")
    else:
        print("Please check the given information again")
        operations()
                    
                

                
    

                
                
