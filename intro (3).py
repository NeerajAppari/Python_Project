#including headers
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
global lnamel
global fnamel
lnamel=[]
fnamel=[]
global lnamew
global fnamew
lnamew=[]
fnamew=[]
global lnamewa
global fnamewa
lnamewa=[]
fnamewa=[]



def app():
    #creating front page
    win=Tk()
    win.geometry("2000x1000")
    win.title("NEERAJ_APPARI_F-129_FYCS")
    win["bg"]="white"
    def dest1():
        win.destroy()
        userlog()

    def dest2():
        win.destroy()
        euser()

    def dest3():
        exit()
    
        
    #front page design
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

    



#checking user page
def userlog():
    #creating window
    win1=Tk()
    win1.geometry("2000x1000")
    win1.title("Creating Account")
    win1["bg"]="white"

    #creating Labels
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

    #taking entry from user
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

    #checking for errors
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
    
      
    #Button for next page
    next1=Button(win1,text="Next",width=12,height=2,bg="navy",fg="white",command=ntab1)
    next1.configure(font="Times 18")
    next1.place(x=450,y=330)

    
        
        

    #Button for main menu page

    next1=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next1.configure(font="Times 18")
    next1.place(x=700,y=330)


def details():
    #questions for login
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
    #Button for next page
    nxtbtn=Button(win3,text="Back",width=12,height=2,bg="navy",fg="white",command=neat)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=450,y=365)

    def mainb():
        win3.destroy()
        app()
    #Button for main page
    nxtbtn=Button(win3,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=700,y=365)

    #checking questions
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

#checking personal details
def pdtls():
    #creating a window
    win4=Tk()
    win4.geometry("2000x1000")
    win4.title("Personal Details")
    win4["bg"]="white"

    gender=StringVar()

    #creating labels
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
    #creating Labels and Radiobutton
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

    #creating spin box
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
    #checking for errors
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
                #using message box to show errors
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
                    #creating database
                    con=sqlite3.connect('data.bd')
                    cur=con.cursor()
                    cur.execute('Drop table if exists data')
                    cur.execute('create table data(fname text,lname text,contact integer)')
                    cur.execute('insert into data(fname,lname,contact) values(?,?,?)',(y,x,a))
                    cur.execute('Select * from data')
                    d1=cur.fetchall()
                    #creating file
                    with open(f"{lname.get()}{fname.get()}.txt","a") as out1:
                        A=['Last Name:',x]
                        B=['\nFirst Name:',y]
                        C=['\nMiddle Name:',z]
                        D=['\nPhone Number:',a]
                        G=['\nDay:',b,'\tMonth:',c,'\tYear:',d]
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

                
                        
    #Button for next page

    nxtbtn3=Button(win4,text="Next",width=12,height=2,bg="navy",fg="white",command=logcheck)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=450,y=670)

    #Button for main page
    def main5():
        win4.destroy()
        app()

    nxtbtn3=Button(win4,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=main5)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=700,y=670)

    #Button for back page
    def back5():
        win4.destroy()
        details()

    nxtbtn3=Button(win4,text="Back",width=12,height=2,bg="navy",fg="white",command=back5)
    nxtbtn3.configure(font="Times 18")
    nxtbtn3.place(x=950,y=670)




    


    def next10():
        win4.destroy()
        opt()



    


#verifying login and password
def euser():
    #creating window
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

    #procedures for forgot password
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

    #reading file from location given  below
    #change the given string below when using a different computer i.e type the location of the path where this
    #python program is saved
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
        
        
        
        
    #Button for next page
    next1=Button(win1,text="Next",width=12,height=2,bg="navy",fg="white",command=ntab1)
    next1.configure(font="Times 18")
    next1.place(x=450,y=330)

    #Button for main page

    next2=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next2.configure(font="Times 18")
    next2.place(x=700,y=330)


#verifying questions
def questfor():
    #creating a window
    fp=Tk()
    fp.geometry("2000x1000")
    
    fp["bg"]="white"
    fp.title("Questions for checking password")

    #creating Labels

    head1=Label(fp,text="Forgot Password",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=450,y=10)

    lb1=Label(fp,text="What is favourite food? ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=450,y=140)

    lb2=Label(fp,text="Who is your best friend? ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=450,y=230)

    #creating Entry
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

    
    #Button for back page
    def backm3():
        fp.destroy()
        euser()

    nxtbtn=Button(fp,text="Back",width=12,height=2,bg="navy",fg="white",command=backm3)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=450,y=365)
    #Button for main page
    def mainb2():
        fp.destroy()
        app()

    nxtbtn=Button(fp,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb2)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=700,y=365)

    #reading file from location given  below
    #change the given string below when using a different computer i.e type the location of the path where this
    #python program is saved
    
    def next3():
        read1=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui_project")
        if f"{q1.get()}{q2.get()}.txt" in read1:
           fp.destroy()
           opt()
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")
            
    #Button for next page
    nxtbtn=Button(fp,text="Next",width=12,height=2,bg="navy",fg="white",command=next3)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=950,y=365)

    fp.mainloop()

    


#creating Further transactions
def opt():

    win3=Tk()
    win3.title("Options")
    win3.geometry("2000x1000")
    win3["bg"]="white"

    info=Label(win3,text="FURTHER TRANSACTIONS",bg="white",fg="navy")
    info.configure(font="helvetica 40")
    info.place(x=450,y=10)

    lb1=Label(win3,text="LAST NAME ",bg="white",fg="black")
    lb1.configure(font="helvetica 15")
    lb1.place(x=450,y=102)

    lb2=Label(win3,text="FIRST NAME ",bg="white",fg="black")
    lb2.configure(font="helvetica 15")
    lb2.place(x=450,y=165)

    lname=Entry(win3,bd=4,fg="navy",width=50)
    lname.configure(font="helvetica 19")
    lname.place(x=600,y=102)

    fname=Entry(win3,bd=4,fg="navy",width=50)
    fname.configure(font="helvetica 19")
    fname.place(x=600,y=167)

    side=Label(win3,width=14,height=200)
    side.configure(bg="slate blue")
    side.place(x=0,y=0)
    side1=Label(win3,width=14,height=200)
    side1.configure(bg="slate blue")
    side1.place(x=1440,y=0)
    side2=Label(win3,width=1,height=200)
    side2.configure(bg="black")
    side2.place(x=1438,y=0)
    side3=Label(win3,width=1,height=200)
    side3.configure(bg="black")
    side3.place(x=95,y=0)


    

    def dispp():
        gtx1=os.getcwd()
        print(gtx1)
        last=lname.get()
        first=fname.get()
        osd=f"{gtx1}"
        if os.path.exists(osd):
            win5=Tk()
            win5.geometry("2000x1000")
            side=Label(win5,width=14,height=200)
            side.configure(bg="slate blue")
            side.place(x=0,y=0)
            side1=Label(win5,width=14,height=200)
            side1.configure(bg="slate blue")
            side1.place(x=1440,y=0)
            side2=Label(win5,width=1,height=200)
            side2.configure(bg="black")
            side2.place(x=1438,y=0)
            side3=Label(win5,width=1,height=200)
            side3.configure(bg="black")
            side3.place(x=95,y=0)

            #reading a file
            osde=osd+f'\\{last}{first}'
            with open (f"{osde}.txt","r") as d:
                   
                displabel=Label(win5,font=('Arial Black',20,'bold'),text=d.read())
                displabel.pack()

            def win5d():
                win5.destroy()
            #Button for prev page
            bb=Button(win5,text="Back",width=12,height=2,bg="navy",fg="white",command=win5d)
            bb.configure(font="Times 18")
            bb.place(x=650,y=365)

            
                
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")

    #Button for display page

    dispb=Button(win3,text="Display",width=12,height=2,bg="navy",fg="white",command=dispp)
    dispb.configure(font="Times 18")
    dispb.place(x=450,y=365)

    def mainagain():
        win3.destroy()
        app()

    #Button for main page

    mainm10=Button(win3,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainagain)
    mainm10.configure(font="Times 18")
    mainm10.place(x=700,y=365)

    def trans1():
        lnamel.append(lname.get())
        fnamel.append(fname.get())
        lnamew.append(lname.get())
        fnamew.append(fname.get())
        lnamewa.append(lname.get())
        fnamewa.append(fname.get())
        
        win3.destroy()
        transo()

    def transo():
        
        win6=Tk()
        win6.title("Options")
        win6.geometry("2000x1000")
        
        win6["bg"]="white"

        
            
            
            

        pro=Label(win6,text="TRANSACTIONS",bg="white",fg="navy")
        pro.configure(font="helvetica 40")
        pro.place(x=450,y=10)
        side=Label(win6,width=14,height=200)
        side.configure(bg="slate blue")
        side.place(x=0,y=0)
        side1=Label(win6,width=14,height=200)
        side1.configure(bg="slate blue")
        side1.place(x=1440,y=0)
        side2=Label(win6,width=1,height=200)
        side2.configure(bg="black")
        side2.place(x=1438,y=0)
        side3=Label(win6,width=1,height=200)
        side3.configure(bg="black")
        side3.place(x=95,y=0)

        #Button for withdraw page

        def withdrawnext():
            win6.destroy()
            withdrawal()

        

        withd=Button(win6,text="Withdraw",width=12,height=2,bg="navy",fg="white",command=withdrawnext)
        withd.configure(font="Times 18")
        withd.place(x=500,y=100)

        #Button for deposit page

        def nextdeposit():
            win6.destroy()
            deposit()
            

        depo=Button(win6,text="Deposit",width=12,height=2,bg="navy",fg="white",command=nextdeposit)
        depo.configure(font="Times 18")
        depo.place(x=750,y=100)

        #Button for transaction page

        def nexttran():
            win6.destroy()
            transac()
            

        trans=Button(win6,text="Transactions",width=12,height=2,bg="navy",fg="white",command=nexttran)
        trans.configure(font="Times 18")
        trans.place(x=500,y=250)

        #Button for balance page

        def nextbal():
            win6.destroy()
            balance()
            

        balc=Button(win6,text="Balance",width=12,height=2,bg="navy",fg="white",command=nextbal)
        balc.configure(font="Times 18")
        balc.place(x=750,y=250)

        #Button for main page
        
        def mainmb10():
            win6.destroy()
            app()

            

        main11=Button(win6,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainmb10)
        main11.configure(font="Times 18")
        main11.place(x=500,y=400)

        #Button for exit page

        def lmenu():
            win6.destroy()
            exit(0)

        lback=Button(win6,text="Quit",width=12,height=2,bg="navy",fg="white",command=lmenu)
        lback.configure(font="Times 18")
        lback.place(x=750,y=400)

        #window for checking transactions
        def transac():
            gtx2=os.getcwd()
            print(gtx2)
            last1=lnamewa[-1]
            first1=fnamewa[-1]
            osd2=f"{gtx2}"
            if os.path.exists(osd2):
                win11=Tk()
                win11.geometry("2000x1000")
                
                dl=Label(win11,text="TRANSACTIONS",fg="navy")
                dl.configure(font="helvetica 40")
                dl.place(x=450,y=10)

                
                osde2=osd2+f'\\{last1}{first1}'
                with open (f"{osde2}trans.txt","r") as d:
                   
                    displabel2=Label(win11,font=('Arial Black',20,'bold'),text=d.read())
                    displabel2.place(x=500,y=100)
                side=Label(win11,width=14,height=200)
                side.configure(bg="slate blue")
                side.place(x=0,y=0)
                side1=Label(win11,width=14,height=200)
                side1.configure(bg="slate blue")
                side1.place(x=1440,y=0)
                side2=Label(win11,width=1,height=200)
                side2.configure(bg="black")
                side2.place(x=1438,y=0)
                side3=Label(win11,width=1,height=200)
                side3.configure(bg="black")
                side3.place(x=95,y=0)

                def gtt():
                    win11.destroy()
                    transo()

                tb1=Button(win11,text="Back",width=12,height=2,bg="navy",fg="white",command=gtt)
                tb1.configure(font="Times 18")
                tb1.place(x=200,y=10)


                

        #window for withdrawal
        def withdrawal():
            gtx5=os.getcwd()
            print(gtx5)
            last5=lnamel[-1]
            first5=fnamel[-1]
            osd5=f"{gtx5}"
            if os.path.exists(osd5):
                wintdr=Tk()
                wintdr.title("Withdrawal")
                wintdr.geometry("2000x1000")

                dl=Label(wintdr,text="WITHDRAW",fg="navy")
                dl.configure(font="helvetica 40")
                dl.place(x=450,y=10)

                dl1=Label(wintdr,text="AMOUNT",fg="navy")
                dl1.configure(font="helvetica 15")
                dl1.place(x=500,y=100)

##                
##
                osde5=osd5+f'\\{last5}{first5}'
                withaa=Entry(wintdr)
                withaa.place(x=650,y=102)
                def fun_fun():
                    messagebox.showinfo('Transaction Complete',"Money Withdrawn Successfully")
                    fun1()
                with_aa=Button(wintdr,text="Enter",width=12,height=2,bg="navy",fg="white",command=fun_fun)
                with_aa.configure(font="Times 18")
                with_aa.place(x=500,y=400)
                #performing operations based on balances
                def fun1():
                    l=[]
                    file_=open(f"{osde5}acc.txt",'r')
                    for g in file_:
                        l.append(g.strip())
                    d=int(l[-1])
                    if int(withaa.get())<=d:
                       final_ammount=int(d)-int(withaa.get())
                       print('Current Balance :',final_ammount)
                       with open (f"{osde5}acc.txt",'a') as bal11:
                            bal11.write(f'\n{str(final_ammount)}')
                    else:
                       print()
                       print('Insufficient WithDrawal Balance!')
                       transo()
                    with open(f"{osde5}trans.txt",'a') as tbal1:
                        tbal1.writelines(f'\nwithdraw:{str(withaa.get())}')
                     
##                    
##                    withaa=Enter(wintdr)
##                    withaa.place(x=200,500)
                side=Label(wintdr,width=14,height=200)
                side.configure(bg="slate blue")
                side.place(x=0,y=0)
                side1=Label(wintdr,width=14,height=200)
                side1.configure(bg="slate blue")
                side1.place(x=1440,y=0)
                side2=Label(wintdr,width=1,height=200)
                side2.configure(bg="black")
                side2.place(x=1438,y=0)
                side3=Label(wintdr,width=1,height=200)
                side3.configure(bg="black")
                side3.place(x=95,y=0)

           

            

           #Button for back page
            def gtt2():
                wintdr.destroy()
                transo()

            tb2=Button(wintdr,text="Back",width=12,height=2,bg="navy",fg="white",command=gtt2)
            tb2.configure(font="Times 18")
            tb2.place(x=700,y=400)

            
            #window for deposit

        def deposit():
            
            gtx6=os.getcwd()
            print(gtx6)
            last6=lnamel[-1]
            first6=fnamel[-1]
            osd6=f"{gtx6}"
            if os.path.exists(osd6):
                winbhav=Tk()
                winbhav.title("Deposit")
                winbhav.geometry("2000x1000")
                dl=Label(winbhav,text="DEPOSIT",fg="navy")
                dl.configure(font="helvetica 40")
                dl.place(x=450,y=10)

                dl1=Label(winbhav,text="AMOUNT",fg="navy")
                dl1.configure(font="helvetica 15")
                dl1.place(x=500,y=100)
##
                osde6=osd6+f'\\{last6}{first6}'
                withrts=Entry(winbhav)
                withrts.place(x=650,y=102)
                #deposit transactions
                def gotodepo():
                    messagebox.showinfo('Transaction Complete',"Money Deposited Successfully")
                    gotodepo1()
                with_dd=Button(winbhav,text="Enter",width=12,height=2,bg="navy",fg="white",command=gotodepo)
                with_dd.configure(font="Times 18")
                with_dd.place(x=350,y=400)
                def gotodepo1():
                    l1=[]
                    file_1=open(f"{osde6}acc.txt",'r')
                    for g1 in file_1:
                        l1.append(g1.strip())
                    b=int(l1[-1])
                    
                    final_ammount=int(b)+int(withrts.get())
                    print('Current Balance :',final_ammount)
                    with open (f"{osde6}acc.txt",'a') as bal112:
                        bal112.write(f'\n{str(final_ammount)}')
                
                   
                    with open(f"{osde6}trans.txt",'a') as tbal12:
                        tbal12.writelines(f'\ndeposit:{str(withrts.get())}')
                     
            side=Label(winbhav,width=14,height=200)
            side.configure(bg="slate blue")
            side.place(x=0,y=0)
            side1=Label(winbhav,width=14,height=200)
            side1.configure(bg="slate blue")
            side1.place(x=1440,y=0)
            side2=Label(winbhav,width=1,height=200)
            side2.configure(bg="black")
            side2.place(x=1438,y=0)
            side3=Label(winbhav,width=1,height=200)
            side3.configure(bg="black")
            side3.place(x=95,y=0)

            def gtt3():
                winbhav.destroy()
                transo()

            tb3=Button(winbhav,text="Back",width=12,height=2,bg="navy",fg="white",command=gtt3)
            tb3.configure(font="Times 18")
            tb3.place(x=650,y=400)
        #window for balance
        def balance():
            gtx3=os.getcwd()
            print(gtx3)
            last3=lnamew[-1]
            first3=fnamew[-1]
            osd3=f"{gtx3}"
            if os.path.exists(osd3):
                wintbal=Tk()
                wintbal.geometry("2000x1000")
                dl=Label(wintbal,text="BALANCE",bg="white",fg="navy")
                dl.configure(font="helvetica 40")
                dl.place(x=450,y=10)
                #shows current balance
                osde3=osd3+f'\\{last3}{first3}'
                gh=[]
                fgl=open(f"{osde3}acc.txt","r")
                for b in fgl:
                    gh.append(b)
                d=gh[-1]
                displabel3=Label(wintbal,font=('Arial Black',20,'bold'),text=d)
                displabel3.place(x=500,y=100)
                side=Label(wintbal,width=14,height=200)
                side.configure(bg="slate blue")
                side.place(x=0,y=0)
                side1=Label(wintbal,width=14,height=200)
                side1.configure(bg="slate blue")
                side1.place(x=1440,y=0)
                side2=Label(wintbal,width=1,height=200)
                side2.configure(bg="black")
                side2.place(x=1438,y=0)
                side3=Label(wintbal,width=1,height=200)
                side3.configure(bg="black")
                side3.place(x=95,y=0)

                #Button for prev page

                def gtt4():
                    wintbal.destroy()
                    transo()

                tb4=Button(wintbal,text="Back",width=12,height=2,bg="navy",fg="white",command=gtt4)
                tb4.configure(font="Times 18")
                tb4.place(x=650,y=400)

    
            
        

    

        
        #Button for prev page        
        
    gtt=Button(win3,text="Transactions",width=12,height=2,bg="navy",fg="white",command=trans1)
    gtt.configure(font="Times 18")
    gtt.place(x=950,y=365)

    

            
    
    
        


        


        


    
    
    
    

    
    



    
app()
    

