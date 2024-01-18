def password():
    LoginID="RTY"
    
    attempt=3

    while True:
        login=input("Enter LoginID:")
        password=input("Enter Password:")


        if login==LoginID:
            print("Login successfull")
            
            Password="yry"
            password=input("Enter Password:")
            
            if password==Password:
                print("Login successfull")
                break
            else:
                print("Wrong pass")
            
        
            
                 
               

        elif attempt>1:
            attempt=attempt-1
            print("Try Again ",attempt,": more attempt only")
            continue

        else:
            print("blocked")
            break


    print("Thank You")

password()




        

        

    

    
