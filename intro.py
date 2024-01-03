from tkinter import *
from tkinter import messagebox
import os

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
    head1.place(x=500,y=10)

    lb1=Label(win1,text="Login ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=500,y=140)

    lb2=Label(win1,text="Password ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=500,y=185)

    lb3=Label(win1,text="Confirm",bg="white",fg="black")
    lb3.configure(font="helvetica 19")
    lb3.place(x=500,y=232)

    login=Entry(win1,bd=4,fg="navy",width=55)
    login.configure(font="Times 19")
    login.place(x=650,y=140)
    neel=StringVar()
    pwd=Entry(win1,bd=4,textvariable=neel,fg="navy",width=55)
    pwd.configure(font="Times 19")
    pwd.place(x=650,y=187)
    
    neel1=StringVar()
    cpwd=Entry(win1,bd=4,textvariable=neel1,fg="navy",width=55)
    cpwd.configure(font="Times 19")
    cpwd.place(x=650,y=234)

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
        if neelis==neelis1:
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
    next1.place(x=500,y=330)

    
        
        

    

    next1=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next1.configure(font="Times 18")
    next1.place(x=750,y=330)


def details():

    win3=Tk()
    win3.geometry("2000x1000")
    win3["bg"]="white"
    win3.title("Questions")

    head1=Label(win3,text="Questions",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=500,y=10)

    lb1=Label(win3,text="What is favourite food? ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=500,y=140)

    lb2=Label(win3,text="Who is your best friend? ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=500,y=230)

    q1=Entry(win3,bd=4,fg="navy",width=25)
    q1.configure(font="Times 19")
    q1.place(x=500,y=185)

    q2=Entry(win3,bd=4,fg="navy",width=25)
    q2.configure(font="Times 19")
    q2.place(x=500,y=275)

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
    nxtbtn.place(x=500,y=365)

    def mainb():
        win3.destroy()
        app()

    nxtbtn=Button(win3,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=750,y=365)

    def npdtls():
        with open(f"{q1.get()}{q2.get()}.txt","a") as out1:
             out1.write("")
        out1.close()
        win3.destroy()
        pdtls()

    nxtbtn=Button(win3,text="Next",width=12,height=2,bg="navy",fg="white",command=npdtls)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=1000,y=365)

    win3.mainloop()


def pdtls():
    win4=Tk()
    win4.geometry("2000x1000")
    win4.title("Personal Details")
    win4["bg"]="white"


    



def euser():
    win1=Tk()
    win1.geometry("2000x1000")
    
    win1["bg"]="white"
    win1.title("Checking Login and Password")

    head1=Label(win1,text="Existing User",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=500,y=10)

    lb1=Label(win1,text="Login ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=500,y=140)

    lb2=Label(win1,text="Password ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=500,y=185)


    login=Entry(win1,bd=4,fg="navy",width=55)
    login.configure(font="Times 19")
    login.place(x=650,y=140)

    pwd=Entry(win1,bd=4,fg="navy",width=55)
    pwd.configure(font="Times 19")
    pwd.place(x=650,y=187)

    def forgotpass():
        win1.destroy()
        questfor()

    forget=Button(win1,text='Forgot Password',width=15,fg='blue4',bg="white",bd=0,activebackground="white",command=forgotpass)
    forget.configure(font='helvetica 12')
    forget.place(x=498,y=250)

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
        read=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui project")
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
    next1.place(x=500,y=330)

    next1=Button(win1,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=btab1)
    next1.configure(font="Times 18")
    next1.place(x=750,y=330)



def questfor():
    fp=Tk()
    fp.geometry("2000x1000")
    
    fp["bg"]="white"
    fp.title("Questions for checking password")


    head1=Label(fp,text="Forgot Password",bg="white",fg="navy",bd=0)
    head1.configure(font="helvetica 40")
    head1.place(x=500,y=10)

    lb1=Label(fp,text="What is favourite food? ",bg="white",fg="black")
    lb1.configure(font="helvetica 19")
    lb1.place(x=500,y=140)

    lb2=Label(fp,text="Who is your best friend? ",bg="white",fg="black")
    lb2.configure(font="helvetica 19")
    lb2.place(x=500,y=230)

    q1=Entry(fp,bd=4,fg="navy",width=25)
    q1.configure(font="Times 19")
    q1.place(x=500,y=185)

    q2=Entry(fp,bd=4,fg="navy",width=25)
    q2.configure(font="Times 19")
    q2.place(x=500,y=275)

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
    nxtbtn.place(x=500,y=365)

    def mainb2():
        fp.destroy()
        app()

    nxtbtn=Button(fp,text="Main Menu",width=12,height=2,bg="navy",fg="white",command=mainb2)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=750,y=365)

    def next3():
        read1=os.listdir(r"C:\Users\LAXMINARAYANRO\Desktop\fffiiles\college pracs and projects\py\gui project")
        if f"{q1.get()}{q2.get()}.txt" in read1:
           fp.destroy()
           opt()
        else:
            messagebox.showerror('Wrong Input!',"Please Enter Valid inputs!")
        
        

    nxtbtn=Button(fp,text="Next",width=12,height=2,bg="navy",fg="white",command=next3)
    nxtbtn.configure(font="Times 18")
    nxtbtn.place(x=1000,y=365)

    fp.mainloop()

    



def opt():

    win3=Tk()
    win3.title("Options")
    win3.geometry("2000x1000")
    win3["bg"]="white"


    
    
    
    

    
    



    
app()
    

