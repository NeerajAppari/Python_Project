from entercd import *
def cacc():
    
    print("~"*80)
    cname  = input("Enter Customer's first name: ")
    clogin = input("Enter Customer's login ID : ")
    cacno = input("Enter Customer's Account no:")
    print("~"*80)

    CustomerFile = "caccount"+clogin+cname+".txt"
    with open(CustomerFile, 'w')as cf:
        cf.write(cname)
        print("*"*80)
        print(CustomerFile+ " CREATED")
        print("*"*80)
        
    AccountFile = "cbalance"+cname+cacno+".txt"    
    with open(AccountFile,'w')as af:
        af.write('0')
        print("*"*80)
        print(AccountFile+"CREATED")
        print("*"*80)

    TransactionFile = "ctrans"+cname+cacno+".txt"    
    with open(TransactionFile,'w')as tf:
        tf.write('0')
        print("*"*80)
        print(TransactionFile+"CREATED")
        print("*"*80)

    


    Entdetails()



