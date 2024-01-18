def ok1():

    print("\t\t\twhat do u want to do")
    print("create a customer account")
    print("Update customer account")

    req3=input("1,2:")

    for o in req3:

        if o=="1":
            print("fill in the details")
            fill()
            
        elif o=="2":
            print("first create a customer account")
            fill()
        else:
            print("choose a correct option")

def fill():

    with open('cd.txt','w') as v:
        A=input("Customer name:")
        B=input("Customer acc.no:")
        C=input("Customer phone.no:")
        D=input("Customer Bank balance")
        

        A='\n'+A
        B='\n'+B
        C='\n'+C
        D='\n'+D
        (v).writelines(A)
        (v).writelines(B)
        (v).writelines(C)
        (v).writelines(D)
##        with open ('cd.txt','r') as error:
##            contents=error.readlines()
##            print(contents)
        


        next1=input("1,2:")

        if next1=="1":
            print("Create another account")
            

            with open('cd2.txt','w') as r:
                 L=input("Customer name:")
                 K=input("Customer acc.no:")
                 M=input("Customer phone.no:")
                 P=input("Customer Bank balance")
        

                 L='\n'+L
                 K='\n'+K
                 M='\n'+M
                 P='\n'+P
                 (v).writelines(L)
                 (v).writelines(K)
                 (v).writelines(M)
                 (v).writelines(P)
                

        elif next1=="2":
            print("update account")

        else:
            print("Choose correctly")


    



    

    


