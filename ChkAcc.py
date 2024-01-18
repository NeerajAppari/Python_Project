import os
def chkLogin():
    login1 = input("Enter Your login : ")
    pwd1 = input("Enter Your password : ")
    PersonalFile1 = "login"+login1+pwd1+".txt"
    if os.path.exists(PersonalFile1):
        print("login Successfull")
        #call bank menu
    else :
        print("Login Unsucessful")
