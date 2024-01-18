def NewAccount():
    name  = input("Enter Your name: ")
    login = input("Enter Your login : ")
    pwd = input("Enter Your password : ")

    PersonalFile = "login"+login+pwd+".txt"
    AccountBalFile = "account"+login+pwd+".txt"
    with open(PersonalFile, 'w')as pf:
        pf.write(name)
        print(PersonalFile+ " CREATED")
        
    with open(AccountBalFile, 'w') as af:
        af.write("10000")
        print(AccountBalFile+ " CREATED")
    
    
