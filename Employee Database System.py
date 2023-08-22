#Importing all the neccesary libraries 
#One by one

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import mysql.connector


#creation of 1st window
#It holds the Authentication page

class window1:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="white")
        self.root.geometry("1386x786")
        self.root.title("   College Project B.Tech CSE 6th SEMESTER      ---------------     GULSHAN SINGH  :)  ")
        
        #Next window function
        #This function performs transfer between 1st window to 2nd window 
        
        def next_window(self):
            root=Tk()
            w2=window2(root)
            root.mainloop()

        email=StringVar()
        pwd=StringVar()
        
        #Login function
        #button function that check you are ADMIN or not
        
        def login():
            mail=str(email.get())
            password=str(pwd.get())
            
            if(mail=="" or password==""):
                messagebox.showwarning("      WARNING     ","Entry Field Can't Be EMPTY")
                
            elif(mail=="gulshan018@gmail.com" and password=="20cse018"):
                password=str(pwd.get())
                messagebox.showinfo("Your Information",""" Id And Password Are Correct 
            You Logging In Successfully
                """)
                next_window(root)
                
            else:
                self.root.destroy()
                messagebox.showerror("             Error","""LogIn Failed
Incorrect Employee-ID / Password""")
        
        
        #labels and Buttons for the 1st window
        
        l1=Label(root,text="Employee Database System",font=("impact",46),bg="white",fg="black")
        l1.place(x=350,y=80)
        l2=Label(root,text="Database-ID : ",font=("arial",24,"bold"),bg="white",fg="orangered")
        l2.place(x=300,y=220)
        l3=Label(root,text="Password  : ",font=("arial",24,"bold"),bg="white",fg="orangered")
        l3.place(x=300,y=320)

        e1=Entry(root,font=("arial",24,"bold"),bg="white",fg="black",textvariable=email,bd=5,width=25)
        e1.place(x=600,y=220)
        e2=Entry(root,font=("arial",24,"bold"),bg="white",fg="black",textvariable=pwd,bd=5,width=25)
        e2.place(x=600,y=320)

        b1=Button(root,text="LogIn",font=("arial",26,"bold"),bg="blue",fg="white",bd=12,width=15,command=login)
        b1.place(x=520,y=490)
        

        
#Creation of Window 2nd
#This window occurs when you authenticate succesfully
#It holds the functions of Database

class window2:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x500")
        self.root.config(bg="chocolate")
        self.root.title("      Information")
        
        
        #view button function
        #With this button ADMIN can see all the entries in Database
        
        def btn1():
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gullu@1228",
            database="project")
            cur=mydb.cursor()
            cur.execute("select * from info")
            rows=cur.fetchall()

            win=Tk()

            frm=Frame(win)
            frm.pack(side=tk.LEFT,padx=1)

            tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6,7) , show="headings",height="25")
            tv.pack()

            tv.heading(1,text="NAME")
            tv.heading(2,text="E-MAIL")
            tv.heading(3,text="CONTACT NUMBER")
            tv.heading(4,text="FATHER'S NAME")
            tv.heading(5,text="GENDER")
            tv.heading(6,text="ADDRESS ")
            tv.heading(7,text="POST")

            for i in rows:
                tv.insert('',"end",values=i)

            win.title("    FULL Information   ")
            win.geometry("1366x766")
            win.config(bg="black")
            self.root.destroy()
            win.mainloop()

            
        #Register button function
        #It creates a form to be fill
        #New entry is done by this button function
        
        def btn2():
            class Form:
                def __init__(self,root):
                    self.root=root
                    self.root.config(bg="chocolate")
                    self.root.geometry("510x610")
                    self.root.resizable(False,False)
                    self.f=Frame(root,width=480,height=580,bg="orange")
                    self.f.place(x=15,y=15)

                    self.l1=Label(self.f,text="Registration Form",font=("arial",20,"bold underline"),bg="orange")
                    self.l1.place(x=135,y=5)
                    
                    self.l2=Label(self.f,text="Name  : ",font=("arial",16,"bold"),bg="orange")
                    self.l2.place(x=10,y=50)
                    self.l3=Label(self.f,text="Email  : ",font=("arial",16,"bold"),bg="orange")
                    self.l3.place(x=10,y=100)
                    self.l4=Label(self.f,text="Contact : ",font=("arial",16,"bold"),bg="orange")
                    self.l4.place(x=10,y=150)
                    self.l5=Label(self.f,text="Father Name: ",font=("arial",16,"bold"),bg="orange")
                    self.l5.place(x=10,y=200)

                    self.name=StringVar()
                    self.email=StringVar()
                    self.contact=StringVar()
                    self.fathersname=StringVar()
                    self.gen=StringVar()

                    self.e1=Entry(self.f,font=("arial",16,"bold"),width=25,textvariable=self.name,bd=5)
                    self.e1.place(x=150,y=50)
                    self.e2=Entry(self.f,font=("arial",16,"bold"),width=25,textvariable=self.email,bd=5)
                    self.e2.place(x=150,y=100)
                    self.e3=Entry(self.f,font=("arial",16,"bold"),width=25,textvariable=self.contact,bd=5)
                    self.e3.place(x=150,y=150)
                    self.e4=Entry(self.f,font=("arial",16,"bold"),width=25,textvariable=self.fathersname,bd=5)
                    self.e4.place(x=150,y=200)

                    self.l6=Label(self.f,text="Gender : ",font=("arial",16,"bold"),bg="orange")
                    self.l6.place(x=10,y=250)
                    gend=("Select","Male","Female")
                    self.cc1=Combobox(self.f,textvariable=self.gen,value=gend,font=("arial",16,"bold"))
                    self.cc1.place(x=150,y=250)
                    self.cc1.current(0)
                    
                    self.l7=Label(self.f,text="Address : ",font=("arial",16,"bold"),bg="orange")
                    self.l7.place(x=10,y=300)
                    self.t1=Text(self.f,font=("arial",16,"bold"),width=25,height=2)
                    self.t1.place(x=150,y=300)


                    self.l8=Label(self.f,text="Post : ",font=("arial",16,"bold"),bg="orange")
                    self.l8.place(x=10,y=370)
                    self.post=StringVar()
                    posts=("Select","Manager","Accountant","Developer","Web Designer","Data Analyst","Data Scientist")
                    self.cc=Combobox(self.f,textvariable=self.post,value=posts,font=("arial",16,"bold"))
                    self.cc.place(x=150,y=370)
                    self.cc.current(0)

                    self.agree=IntVar()
                    self.ch1=Checkbutton(self.f,variable=self.agree,onvalue=1,bg="orange",offvalue=0,text="Are you agree with terms and condition", font=("arial",16,"bold"))
                    self.ch1.place(x=10,y=420)

                    self.b1=Button(self.f,command=self.action,text="Submit",font=("arial",16,"bold"),bg="black",fg="orange",width=10)
                    self.b1.place(x=150,y=470)
            
            
                #Submit Button function in Form
                #this button function saves information into the Database
                
                def action(self):
                    n1=self.e1.get()
                    em1=self.e2.get()
                    con1=self.e3.get()
                    father1=self.e4.get()
                    gender1=self.cc1.get()
                    address1=self.t1.get(1.0, "end-1c")
                    post1=self.cc.get()
                    agree1=self.agree.get()
                    
                    if n1=="" or em1=="" or con1=="" or father1=="" or gender1=="" or address1=="" or post1=="Select":
                        messagebox.showwarning("Warning","All the field are mendatory")
                    elif self.agree==0:
                        messagebox.showwarning("Warning","Please check terms and condition")
                    else:
                        mydb=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Gullu@1228",
                        database="project")
                        cur=mydb.cursor()
                        query="insert into info(Name,Email,Contact,Father_Name,Gender,Address,Post)values(%s,%s,%s,%s,%s,%s,%s);"
                        val=(n1,em1,con1,father1,gender1,address1,post1)
                        try:
                            cur.execute(query,val)
                        except:
                            messagebox.showwarning("Warning","This email or contact alraedy register")
                        else:
                            mydb.commit()
                            data=f"""
                            
                            Name           :    {n1}
                            Email          :    {em1}
                            Contact        :    {con1}
                           Father's Name  :    {father1}
                            Gender         :    {gender1}
                            address        :    {address1}
                            post           :    {post1}
                            
                            Data Inserted successfully
                            
                            """
                            messagebox.showinfo("Information",data)
                  
            self.root.destroy()    
            root=Tk()
            f=Form(root)
            root.mainloop()
        
        
        #Remove Button Function
        #this is used for the removing entry with the help of email
        #removes entry from the Database
        #It opens a 3rd window where remove button is present
        
        def btn3():
            import tkinter as tk
            from tkinter import messagebox
            from tkinter import ttk
            from tkinter.ttk import Combobox
            import mysql.connector
            
            root2=Toplevel()
            root2.title("   Removing A Entry")
            root2.geometry("500x400")
            root2.config(bg="chocolate")

            remove_email=StringVar()

            
            #remove submit button
            
            def remove():
                self.root.destroy()
                email2=str(remove_email.get())

                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Gullu@1228",
                database="project")
                cur=mydb.cursor()
                query="delete from info where email = %s"
                val=(email2)
                #cur.execute(query,val)
                #mydb.commit()
                #messagebox.showinfo("Information","""Record deleted successfully""")
                try:
                    cur.execute(query,val)
                except:
                    messagebox.showwarning("Warning","Email not Exist")
                else:
                    mydb.commit()
                    messagebox.showinfo("Information","Record deleted successfully")


            l1=Label(root2,text="Enter Email Id Of The Person",font=("arial",20,"bold"),bg="chocolate",fg="black")
            l1.place(x=65,y=55)
            e2=Entry(root2,font=("arial",24,"bold"),bg="white",textvariable=remove_email,fg="orangered",bd=5,width=20)
            e2.place(x=75,y=150)

            b1=Button(root2,text="Remove",font=("arial",26,"bold"),bg="blue",fg="white",bd=10,width=10,command=remove)
            b1.place(x=135,y=240)

            root2.mainloop()

        
        #labels and Buttons for the window 2nd
        
        l1=Label(self.root,text="Click Register for New Entry ",font=("arial",20,"bold"),bg="chocolate",fg="black")
        l1.place(x=100,y=30)
        l2=Label(self.root,text="Click View for View All Databases/Entries ",font=("arial",20,"bold"),bg="chocolate",fg="black")
        l2.place(x=30,y=90)
        l3=Label(self.root,text="Click remove for Removing person's Entry",font=("arial",20,"bold"),bg="chocolate",fg="black")
        l3.place(x=18,y=150)
        
        b1=Button(self.root,text="Register",command=btn2,font=("arial",20,"bold"),bg="blue",fg="black",bd=5,width=15)
        b1.place(x=170,y=230)
        b2=Button(self.root,text="View",command=btn1,font=("arial",20,"bold"),bg="blue",fg="black",bd=5,width=15)
        b2.place(x=170,y=330)
        b3=Button(self.root,text="Remove",command=btn3,font=("arial",20,"bold"),bg="blue",fg="black",bd=5,width=15)
        b3.place(x=170,y=430)
        
root=Tk()
w1=window1(root)
root.mainloop()
 