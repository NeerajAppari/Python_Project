from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import os
global lnamel
global fnamel
lnamel=[]
fnamel=[]

def app():
    win=Tk()
    win.geometry("2000x1000")
    win.title("Banking with DEVIL")
    win["bg"]="white"
    def dest1():
        win.destroy()
        userlog()

    def dest2():
        win.destroy()
        euser()

    def dest3():
        exit()
    
        

    fhead=Label(win,text="Welcome To INKAT banking app")
    fhead.configure(font="windings 40",bg="white",fg="navy")
    fhead.place(x=400,y=10)
    side=Label(win,width=14,height=200)
    side.configure(bg="red")
    side.place(x=0,y=0)
    side1=Label(win,width=14,height=200)
    side1.configure(bg="red")
    side1.place(x=1440,y=0)
    side2=Label(win,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)
    nb=Button(win,text="New User",bd=0,width=12,height=2,bg="navy",fg="white",command=dest1)
    nb.configure(font="Times 20")
    nb.place(x=650,y=150)
    eub=Button(win,text="Existing User",bd=0,width=12,height=2,bg="navy",fg="white",command=dest2)
    eub.configure(font="Times 20")
    eub.place(x=650,y=250)
    eub=Button(win,text="Exit",bd=0,width=12,height=2,bg="navy",fg="white",command=dest3)
    eub.configure(font="Times 20")
    eub.place(x=650,y=350)

    thead=Label(win,text="Welcome To INKAT banking app\nThis Banking app allows you to create user\nStore info about the account\nYou can obtain information about \n transaction,balance,withdrawal and deposit ")
    thead.configure(font="windings 25",bg="white",fg="navy")
    thead.place(x=500,y=500)

    




def userlog():
    win1=Tk()
    win1.geometry("2000x1000")
    win1.title("Creating Account")
    win1["bg"]="white"

    head1=Label(win1,text="New User",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=400,y=10)

    lb1=Label(win1,text="Login ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=450,y=140)

    lb2=Label(win1,text="Password ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=450,y=185)

    lb3=Label(win1,text="Confirm",bg="white",fg="black")
    lb3.configure(font="helvetica 19")
    lb3.place(x=450,y=232)

    login=Entry(win1,bd=4,fg="navy",width=55)
    login.configure(font="Times 19")
    login.place(x=600,y=140)
    neel=StringVar()
    pwd=Entry(win1,bd=4,textvariable=neel,fg="navy",width=55)
    pwd.configure(font="Times 19")
    pwd.place(x=600,y=187)
    
    neel1=StringVar()
    cpwd=Entry(win1,bd=4,textvariable=neel1,fg="navy",width=55)
    cpwd.configure(font="Times 19")
    cpwd.place(x=600,y=234)

    side=Label(win1,width=14,height=200)
    side.configure(bg="blue4")
    side.place(x=0,y=0)
    side1=Label(win1,width=14,height=200)
    side1.configure(bg="blue4")
    side1.place(x=1440,y=0)
    side2=Label(win1,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win1,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)

    def ntab1():
        neelis=neel.get()
        neelis1=neel1.get()
        x=login.get()
        y=pwd.get()
        z=cpwd.get()
        if len(x)==0:
            messagebox.showerror('Wrong Input!',"Please Enter Login!")
        elif len(y)==0:
            messagebox.showerror('Wrong Input!',"Please Enter Password!")
        elif len(z)==0:
            messagebox.showerror('Wrong Input!',"Please Enter Confirm Password!")
        elif neelis==neelis1:
            with open(f"{login.get()}{pwd.get()}.txt","a") as out:
                out.write("")
            out.close()
            win1.destroy()
            details()
        
        else:
            messagebox.showerror('Wrong Input!',"Password and Confirm Password do not match")
        
        

    def btab1():
        win1.destroy()
        app()
    
      

    next1=Button(win1,text="Next",width=12,height=2,bg="navy",fg="white",command=ntab1)
    next1.configure(font="Times 18")
    next1.place(x=450,y=330)

    
        
        

    

    next1=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next1.configure(font="Times 18")
    next1.place(x=700,y=330)


def details():

    win3=Tk()
    win3.geometry("2000x1000")
    win3["bg"]="white"
    win3.title("Questions")

    head1=Label(win3,text="Questions",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=400,y=10)

    lb1=Label(win3,text="What is favourite food? ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=450,y=140)

    lb2=Label(win3,text="Who is your best friend? ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=450,y=230)

    q1=Entry(win3,bd=4,fg="navy",width=25)
    q1.configure(font="Times 19")
    q1.place(x=450,y=185)

    q2=Entry(win3,bd=4,fg="navy",width=25)
    q2.configure(font="Times 19")
    q2.place(x=450,y=275)

    side=Label(win3,width=14,height=200)
    side.configure(bg="blue4")
    side.place(x=0,y=0)
    side1=Label(win3,width=14,height=200)
    side1.configure(bg="blue4")
    side1.place(x=1440,y=0)
    side2=Label(win3,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win3,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)

    def neat():
        win3.destroy()
        userlog()

    nxtbtn=Button(win3,text="Back",width=12,height=2,bg="navy",fg="white",command=neat)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=450,y=365)

    def mainb():
        win3.destroy()
        app()

    nxtbtn=Button(win3,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=700,y=365)

    def npdtls():
        x=q1.get()
        y=q2.get()
        if len(x)==0:
           messagebox.showerror('Wrong Input!',"Please Enter Your Favourite Food!")
        elif len(y)==0:
           messagebox.showerror('Wrong Input!',"Please Enter Your Your Best Friend's Name!")
        else:
                   
            with open(f"{q1.get()}{q2.get()}.txt","a") as out1:
                 out1.write("")
            out1.close()
            win3.destroy()
            pdtls()

    nxtbtn=Button(win3,text="Next",width=12,height=2,bg="navy",fg="white",command=npdtls)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=950,y=365)

    win3.mainloop()


def pdtls():
    win4=Tk()
    win4.geometry("2000x1000")
    win4.title("Personal Details")
    win4["bg"]="white"

    gender=StringVar()


    head2=Label(win4,text="DETAILS",bg="white",fg="navy")
    head2.configure(font="helvetica 40")
    head2.place(x=400,y=10)

    lb1=Label(win4,text="LAST NAME ",bg="white",fg="black")
    lb1.configure(font="helvetica 15")
    lb1.place(x=450,y=125)

    lb2=Label(win4,text="FIRST NAME ",bg="white",fg="black")
    lb2.configure(font="helvetica 15")
    lb2.place(x=450,y=80)

    lb3=Label(win4,text="MIDDLE NAME ",bg="white",fg="black")
    lb3.configure(font="helvetica 15")
    lb3.place(x=450,y=170)

    lb4=Label(win4,text="CONTACT NO. ",bg="white",fg="black")
    lb4.configure(font="helvetica 15")
    lb4.place(x=450,y=220)

    lb5=Label(win4,text="GENDER ",bg="white",fg="black")
    lb5.configure(font="helvetica 15")
    lb5.place(x=450,y=270)

    lb6=Label(win4,text="DATE OF BIRTH ",bg="white",fg="black")
    lb6.configure(font="helvetica 15")
    lb6.place(x=450,y=370)

    lb7=Label(win4,text="ADHAAR NO. ",bg="white",fg="black")
    lb7.configure(font="helvetica 15")
    lb7.place(x=450,y=460)

    lb8=Label(win4,text="ADDRESS ",bg="white",fg="black")
    lb8.configure(font="helvetica 15")
    lb8.place(x=450,y=520)

    lb9=Label(win4,text="MALE ",bg="white",fg="black")
    lb9.configure(font="helvetica 15")
    lb9.place(x=500,y=310)

    lb10=Label(win4,text="FEMALE ",bg="white",fg="black")
    lb10.configure(font="helvetica 15")
    lb10.place(x=615,y=310)

    lname=Entry(win4,bd=4,fg="navy",width=60)
    lname.configure(font="helvetica 15")
    lname.place(x=600,y=127)

    fname=Entry(win4,bd=4,fg="navy",width=60)
    fname.configure(font="helvetica 15")
    fname.place(x=600,y=82)

    mname=Entry(win4,bd=4,fg="navy",width=60)
    mname.configure(font="helvetica 15")
    mname.place(x=600,y=172)

    phone=Entry(win4,bd=4,fg="navy",width=60)
    phone.configure(font="helvetica 15")
    phone.place(x=600,y=222)

    

    male=Radiobutton(win4,bg="white",variable=gender,value="Female",width=3,height=2)
    male.place(x=450,y=310)

    female=Radiobutton(win4,bg="white",variable=gender,value="Male",width=3,height=2)
    female.place(x=560,y=310)

    day=Spinbox(win4,from_=1,to=31,width=3)
    day.configure(font="12")
    day.place(x=460,y=420)

    month=Spinbox(win4,from_=1,to=12,width=3)
    month.configure(font="12")
    month.place(x=510,y=420)

    year=Spinbox(win4,from_=1960,to=2010,width=6)
    year.configure(font="12")
    year.place(x=580,y=420)

    adh=Entry(win4,bd=4,fg="navy",width=60)
    adh.configure(font="helvetica 15")
    adh.place(x=600,y=460)

    adres=Text(win4,width=80,height=2,bg="white",fg="blue")
    adres.configure(font="helvetica 15")
    adres.place(x=450,y=560)

    side=Label(win4,width=14,height=200)
    side.configure(bg="blue4")
    side.place(x=0,y=0)
    side1=Label(win4,width=14,height=200)
    side1.configure(bg="blue4")
    side1.place(x=1440,y=0)
    side2=Label(win4,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win4,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)

    def logcheck():
                x=lname.get()
                y=fname.get()
                z=mname.get()
                a=phone.get()
                b=day.get()
                
                c=month.get()
                d=year.get()
                e=adh.get()
                f=adres.get("1.0",'end-1c')
                gen=gender.get()
                if len(x)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your Last Name!")
                elif len(y)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your First Name!")
                elif len(z)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your Middle Name!")
                elif x.isalpha()==False:
                   messagebox.showerror('Wrong Input!',"Last Name should be in Alphabets!")
                elif y.isalpha()==False:
                   messagebox.showerror('Wrong Input!',"First Name should be in Alphabets!")
                elif z.isalpha()==False:
                   messagebox.showerror('Wrong Input!',"Middle Name should be in Alphabets!")
                elif len(a)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your Contact No!")
                elif (len(a)<10 or len(a)>10) and a.isdigit()==True:
                   messagebox.showerror('Wrong Input!',"Contact No should be of 10 Digits!")
                elif a.isdigit()==False:
                   messagebox.showerror('Wrong Input!',"Contact No should be in Digits!")
                elif len(e)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your Adhaar No!")
                elif (len(e)<12 or len(e)>12) and e.isdigit()==True:
                   messagebox.showerror('Wrong Input!',"Adhaar No should be of 12 Digits!")
                elif e.isdigit()==False:
                   messagebox.showerror('Wrong Input!',"Adhaar No should be in Digits!")
                elif len(f)==0:
                   messagebox.showerror('Wrong Input!',"Please Enter Your Address!")
                elif len(f)<25:
                   messagebox.showerror('Wrong Input!',"Address should be of at least 25 Characters!")
                else:
                    with open(f"{lname.get()}{fname.get()}.txt","a") as out1:
                        A=['Last Name:',x]
                        B=['\nFirst Name:',y]
                        C=['\nMiddle Name:',z]
                        D=['\nPhone Number:',a]
                        G=['\nDay:\t',b,'Month:\t',c,'Year:',d]
                        E=['\nAadhar Number:',e]
                        F=['\nAddress:',f]
                        H=['\nGender:',gen]
                        out1.writelines(A)
                        out1.writelines(B)
                        out1.writelines(C)
                        out1.writelines(G)
                        out1.writelines(D)
                        out1.writelines(E)
                        out1.writelines(F)
                        out1.writelines(H)

                    with open(f"{lname.get()}{fname.get()}acc.txt","a") as out2:
                        K=['10000']
                        out2.writelines(K)
                    with open(f"{lname.get()}{fname.get()}trans.txt","a") as out3:
                        M=['']
                        out3.writelines(M)
                        next10()

##
##                def ntab1():
##                    read=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui project")
##                    if f"{login.get()}{pwd.get()}.txt" in read:
##                       win1.destroy()
##                       opt(y,x)
##                    else:
##                        messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")
##                        next10()
##
##                next1=Button(win1,text="Next",width=12,height=2,bg="navy",fg="white",command=ntab1)
##                next1.configure(font="Times 18")
##                next1.place(x=450,y=330)
##
##
####                        bankdata2=sqlite3.connect("banksys.db")
####                        bankd=bankdata2.cursor()
####
####                        bankd.execute('CREATE TABLE IF NOT EXISTS bankinfo (Fname TEXT,Mname TEXT,Lname TEXT,DAY TEXT,MONTH TEXT,YEAR TEXT,Gender TEXT,Address TEXT,Phone_no TEXT,Aadhar no')
####                        bankd.execute(f'insert into bankinfo("{y}","{z}","{x}","{b}","{c}","{d}","{gen}","{f},"{a}","{e}")')
####                        bankd.commit()
####                        yu=bankd.execute('select * from bankinfo')
####                        for i in yu:
####                            print(i)
                
                        


    nxtbtn3=Button(win4,text="Next",width=12,height=2,bg="navy",fg="white",command=logcheck)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=450,y=670)

    def main5():
        win4.destroy()
        app()

    nxtbtn3=Button(win4,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=main5)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=700,y=670)

    def back5():
        win4.destroy()
        details()

    nxtbtn3=Button(win4,text="Back",width=12,height=2,bg="navy",fg="white",command=back5)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=950,y=670)




    


    def next10():
        win4.destroy()
        opt()
##        def opt():
##
##            win3=Tk()
##            win3.title("Options")
##            win3.geometry("2000x1000")
##            win3["bg"]="white"
##
##            def dispp():
##                win3.destroy
##                disp()
##                
##
##            nxtbtn=Button(win3,text="Display information",width=12,height=2,bg="navy",fg="white",command=dispp)
##            nxtbtn.configure(font="Times 18")
##            nxtbtn.place(x=950,y=365)
##
##
##            def disp():
##
##                with open (f"{y.get()}{x.get()}.txt,r") as d:
##                    g=d.readlines()
##                    for i in g:
##                        print(strip(i))
##                    win3.mainloop()



    



def euser():
    win1=Tk()
    win1.geometry("2000x1000")
    
    win1["bg"]="white"
    win1.title("Checking Login and Password")

    head1=Label(win1,text="Existing User",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=450,y=10)

    lb1=Label(win1,text="Login ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=450,y=140)

    lb2=Label(win1,text="Password ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=450,y=185)


    login=Entry(win1,bd=4,fg="navy",width=55)
    login.configure(font="Times 19")
    login.place(x=600,y=140)

    pwd=Entry(win1,bd=4,fg="navy",width=55)
    pwd.configure(font="Times 19")
    pwd.place(x=600,y=187)

    def forgotpass():
        win1.destroy()
        questfor()

    forget=Button(win1,text='Forgot Password',width=15,fg='blue4',bg="white",bd=0,activebackground="white",command=forgotpass)
    forget.configure(font='helvetica 12')
    forget.place(x=448,y=250)

    side=Label(win1,width=14,height=200)
    side.configure(bg="magenta4")
    side.place(x=0,y=0)
    side1=Label(win1,width=14,height=200)
    side1.configure(bg="magenta4")
    side1.place(x=1440,y=0)
    side2=Label(win1,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win1,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)

    def ntab1():
        read=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui_project")
        if f"{login.get()}{pwd.get()}.txt" in read:
           win1.destroy()
           opt()
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")

    def btab1():
        win1.destroy()
        app()
        
        
        
        

    next1=Button(win1,text="Next",width=12,height=2,bg="navy",fg="white",command=ntab1)
    next1.configure(font="Times 18")
    next1.place(x=450,y=330)

    next2=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next2.configure(font="Times 18")
    next2.place(x=700,y=330)



def questfor():
    fp=Tk()
    fp.geometry("2000x1000")
    
    fp["bg"]="white"
    fp.title("Questions for checking password")


    head1=Label(fp,text="Forgot Password",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=450,y=10)

    lb1=Label(fp,text="What is favourite food? ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=450,y=140)

    lb2=Label(fp,text="Who is your best friend? ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=450,y=230)

    q1=Entry(fp,bd=4,fg="navy",width=25)
    q1.configure(font="Times 19")
    q1.place(x=450,y=185)

    q2=Entry(fp,bd=4,fg="navy",width=25)
    q2.configure(font="Times 19")
    q2.place(x=450,y=275)

    side=Label(fp,width=14,height=200)
    side.configure(bg="magenta4")
    side.place(x=0,y=0)
    side1=Label(fp,width=14,height=200)
    side1.configure(bg="magenta4")
    side1.place(x=1440,y=0)
    side2=Label(fp,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(fp,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)

    

    def backm3():
        fp.destroy()
        userlog()

    nxtbtn=Button(fp,text="Back",width=12,height=2,bg="navy",fg="white",command=backm3)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=450,y=365)

    def mainb2():
        fp.destroy()
        app()

    nxtbtn=Button(fp,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb2)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=700,y=365)

    def next3():
        read1=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui_project")
        if f"{q1.get()}{q2.get()}.txt" in read1:
           fp.destroy()
           opt()
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")
        
        

    nxtbtn=Button(fp,text="Next",width=12,height=2,bg="navy",fg="white",command=next3)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=950,y=365)

    fp.mainloop()

    



def opt():

    win3=Tk()
    win3.title("Options")
    win3.geometry("2000x1000")
    win3["bg"]="white"

    info=Label(win3,text="ENTER NAME FOR FURTHER TRANSACTIONS",bg="white",fg="navy")
    info.configure(font="helvetica 40")
    info.place(x=450,y=10)

    lb1=Label(win3,text="LAST NAME ",bg="white",fg="black")
    lb1.configure(font="helvetica 15")
    lb1.place(x=450,y=80)

    lb2=Label(win3,text="FIRST NAME ",bg="white",fg="black")
    lb2.configure(font="helvetica 15")
    lb2.place(x=450,y=125)

    lname=Entry(win3,bd=4,fg="navy",width=60)
    lname.configure(font="helvetica 15")
    lname.place(x=600,y=82)

    fname=Entry(win3,bd=4,fg="navy",width=60)
    fname.configure(font="helvetica 15")
    fname.place(x=600,y=127)


    

    def dispp():
        gtx1=os.getcwd()
        print(gtx1)
        last=lname.get()
        first=fname.get()
        osd=f"{gtx1}"
        if os.path.exists(osd):
            win5=Tk()
            win5.geometry("2000x1000")
            
            osde=osd+f'\\{last}{first}'
            with open (f"{osde}.txt","r") as d:
                   
                displabel=Label(win5,font=('Arial Black',20,'bold'),text=d.read())
                displabel.pack()
            
                   
            
            
            
            
            
##        reading=os.listdir(f"{gtx1}")
##        if f"{lname.get()}{fname.get()}.txt" in reading:
##           win3.destroy()
##            
##           with open (f"{lname.get()}{fname.get()}.txt","r") as d:
##               g=d.readlines()
##               for i in g:
##                   print(strip(i))

                   ##win5=Tk()
                   
                
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")

        

    dispb=Button(win3,text="Display",width=12,height=2,bg="navy",fg="white",command=dispp)
    dispb.configure(font="Times 18")
    dispb.place(x=450,y=365)

    def mainagain():
        win3.destroy()
        app()

    

    mainm10=Button(win3,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainagain)
    mainm10.configure(font="Times 18")
    mainm10.place(x=700,y=365)

    def trans1():
        lnamel.append(lname.get())
        fnamel.append(fname.get())
        win3.destroy()
        trans()

    def trans():
        try:
            win6=Tk()
            win6.title("Options")
            win6.geometry("2000x1000")
            
            win6["bg"]="white"

            
                
                
                

            pro=Label(win6,text="TRANSACTIONS",bg="white",fg="navy")
            pro.configure(font="helvetica 40")
            pro.place(x=450,y=10)
        except TclError:
            """"""

        def withdrawnext():
            win6.destroy()
            withdrawal()

        

        withd=Button(win6,text="Withdraw",width=12,height=2,bg="navy",fg="white",command=withdrawnext)
        withd.configure(font="Times 18")
        withd.place(x=500,y=100)

        def nextdeposit():
            win6.destroy()
            deposit()
            

        depo=Button(win6,text="Deposit",width=12,height=2,bg="navy",fg="white",command=nextdeposit)
        depo.configure(font="Times 18")
        depo.place(x=750,y=100)

        def nexttran():
            win6.destroy()
            transac()
            

        trans=Button(win6,text="Transactions",width=12,height=2,bg="navy",fg="white",command=nexttran)
        trans.configure(font="Times 18")
        trans.place(x=500,y=250)

        def nextbal():
            win6.destroy()
            balance()
            

        balc=Button(win6,text="Balance",width=12,height=2,bg="navy",fg="white",command=nextbal)
        balc.configure(font="Times 18")
        balc.place(x=750,y=250)
        def mainmb10():
            win6.destroy()
            app()
            

        main11=Button(win6,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainmb10)
        main11.configure(font="Times 18")
        main11.place(x=500,y=400)

        def lmenu():
            win6.destroy()
            exit(0)

        lback=Button(win6,text="Quit",width=12,height=2,bg="navy",fg="white",command=lmenu)
        lback.configure(font="Times 18")
        lback.place(x=750,y=400)


        def transac():
            gtx2=os.getcwd()
            print(gtx2)
            last1=lnamel[-1]
            first1=fnamel[-1]
            osd2=f"{gtx2}"
            if os.path.exists(osd2):
                win11=Tk()
                win11.geometry("2000x1000")
                
                osde2=osd2+f'\\{last1}{first1}'
                with open (f"{osde2}trans.txt","r") as d:
                   
                    displabel2=Label(win11,font=('Arial Black',20,'bold'),text=d.read())
                    displabel2.pack()


        def withdrawal():
            wintan=Tk()
            wintan.title("Withdrawal")
            wintan.geometry("2000x1000")

            withenter=Entry(wintan)
            
            

        def deposit():
            wintan=Tk()
            wintan.title("deposit")
            wintan.geometry("2000x1000")

        def balance():
            wintan=Tk()
            wintan.title("Current Balance")
            wintan.geometry("2000x1000")

        
            
        

    

        
        
        
    gtt=Button(win3,text="Transactions",width=12,height=2,bg="navy",fg="white",command=trans1)
    gtt.configure(font="Times 18")
    gtt.place(x=950,y=365)

##def disp():
    

            
    
    
        


        


        


    
    
    
    

    
    



    
app()
    

