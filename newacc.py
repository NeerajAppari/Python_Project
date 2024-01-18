def newac():
    name  = input("Enter Your Firstname: ")
    lname = input("Enter Your Lastname")
    mname = input("Enter Your Middlename")
    age = input("Enter your age")
    address1=input("Enter your address")
    address2=input("Enter your landmark and pincode")
    login = input("Enter Your Login : ")
    pwd = input("Enter Your Password : ")

    PersonalFile = "login"+login+pwd+".txt"
    AccountBalFile = "account"+login+pwd+".txt"
    with open(PersonalFile, 'w')as pf:
        pf.write(name)
        print(PersonalFile+ " CREATED")
        
    with open(AccountBalFile, 'w') as af:
        af.write("10000")
        print(AccountBalFile+ " CREATED")

    

