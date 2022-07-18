#imports
import tkinter as tk 
from tkinter import ttk 
from tkinter import *
import os
from PIL import ImageTk, Image

#report
def rip():
    aman50 = Toplevel(aman)
    aman50.title("Report problem")
    aman50.geometry("350x350")
    Label(aman50,text="Report your problem",font=("newromantimes",20,"bold"),bg="dimgray").pack(fill=X)
    Label(aman50,text="").pack(fill=X)
    Label(aman50,text=" Enter the problems : ").pack(anchor="nw")
    Label(aman50,text="").pack(fill=X)
    Entry(aman50,justify='left',width=45).pack()
    Label(aman50,text="").pack()
    Label(aman50,text=" OR OTHER CHOICE : ").pack(anchor="nw")
    Radiobutton(aman50,text="Write issue",value=1).pack(anchor="nw")
    Radiobutton(aman50,text="Text eror",value=2).pack(anchor="nw")
    Radiobutton(aman50,text="Working issue",value=3).pack(anchor="nw")
    Radiobutton(aman50,text="Qualitity",value=4).pack(anchor="nw")
    Radiobutton(aman50,text="Other",value=5).pack(anchor="nw")
    Button(aman50,text="Feed",command=exit1,width=16,relief=SUNKEN).pack()
    my = Menu(aman50)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    aman50.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    
    my.add_command(label="Exit",command=exit1)
    
#feedback
def fb():
    aman50 = Toplevel(aman)
    aman50.title("Feedback")
    aman50.geometry("450x350")
    Label(aman50,text="Describe what's happening",font=("newromantimes",11)).pack(anchor="nw")
    Entry(aman50,text="Remember not to include personal info like phone numbers.",width=45,relief=SUNKEN).pack()
    Label(aman50,text=" URL : ").pack(anchor="nw")
    Entry(aman50,text="https://bhartbank.org",width=45,relief=SUNKEN).pack(fill=X)
    Label(aman50,text="").pack()
    Radiobutton(aman50,text="Include email address",value=0).pack(anchor="nw")
    
    Entry(aman50,width=45,relief=SUNKEN).pack(fill=X)
    Label(aman50,text="").pack()
    Radiobutton(aman50,text="Send diagnostic data",value=1).pack(anchor="nw")
    Radiobutton(aman50,text="Include you experience",value=2).pack(anchor="nw")
    Label(aman50,text="Your feedback be used to improve Bharat ATM service.",font=("newromantimes",7)).pack(anchor="nw")
    Button(aman50,text="Send",command=exit,fg="blue", width=16,relief=SUNKEN).pack()
    my = Menu(aman50)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    aman50.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    my.add_command(label="Exit",command=exit1)
#about  
def ab():
    print("123456")
    aman50 = Toplevel(aman)
    aman50.title("about")
    aman50.geometry("850x750")
    Label(aman50, text = "ATM 2.1.8",font = ("Bradley Hand ITC", 60,"bold")).pack()
    Label(aman50,text="").pack()
    
    Label(aman50, text = "https://www.bharatbank.org ",fg="blue",font = ("Times New Roman", 15,"bold")).pack()
    Label(aman50, text = "").pack()
    Label(aman50,text="Windows 10 (64 bits)",fg="blue",font = ("Chiller", 17,"bold")).pack()
    Label(aman50,text="").pack()
    Label(aman50,text="Made in .......",fg="blue",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="with the help of open-source community,microsoft and students",fg="blue",font=("Gabriola",12,"bold")).pack()                                                                                                 
    Label(aman50,text="").pack()
    Label(aman50,text="Copyright(c) 2021 SBindia",fg="black",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="This program comes with ABSOULTELY WARRANTY!",fg="black",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="It is free software, and you are welcome to redistribute it under certain conditions,see",fg="black",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="https://programmerX.org/ licenses/MIT ",fg="blue",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="For details",fg="black",font=("Gabriola",12,"bold")).pack()
    Label(aman50,text="Editiors :-",fg="Black",font=("Gabriola",12,"bold")).pack(anchor="nw")
    Label(aman50,text="Aman (Coder & Student)",fg="Dark red",font=("Gabriola",12,"bold")).pack(anchor="nw")
    Label(aman50,text="Deepak (Coder & Student)",fg="Dark red",font=("Gabriola",12,"bold")).pack(anchor="nw")
    Label(aman50,text="Lakeshay (Coder & Student)",fg="Dark red",font=("Gabriola",12,"bold")).pack(anchor="nw")
    Label(aman50,text="Vaibhav (Coder & Student)",fg="Dark red",font=("Gabriola",12,"bold")).pack(anchor="nw")
    
    Button(aman50, text="Okey",font=("Gabriola",12,"bold"), command = exit1, width=16,relief=SUNKEN).pack()
                    

    my = Menu(aman50)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    aman50.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    my.add_command(label="Exit",command=exit1)
# setting
def set():
    aman50 = Toplevel(aman)
    aman50.title("settings")
    aman50.geometry("300x170")
    Label(aman50,text="SETTINGS").pack()
    Label(aman50, text = "Backgroung colour", bg = "dimgray",font = ("calibri", 15,"bold")).pack(anchor="nw",fill=X)
    Label(aman50,text="").pack(fill=X)
    Radiobutton(aman50,text="Black",command=black,value=0).pack()
    Radiobutton(aman50,text="Gary",command=gray,value=1).pack()
    my = Menu(aman50)
    my.add_command(label="Exit",command=exit1)
    aman50.config(menu=my)
    my = Menu(aman50)
    
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    aman50.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    my.add_command(label="Exit",command=exit1)


#Rereg
def finalreg():
    n = names.get()
    Dob = DOB.get()
    Dob1=DOB1.get()
    Dob3=DOB3.get()
    gender = genders.get()
    password = passwords.get()
    accounts = os.listdir()
    if n == "" or Dob == "" or gender == "" or password == ""or Dob1==""or Dob3=="":
        notif.config(fg="red",text="//All data is requried//")
        return

    for namec in accounts:
        if  n == namec :
            notif.config(fg="red",text="//already exists//")
            return
        else:
            new_file = open(n,"w")
            new_file.write(n+'\n')
            new_file.write(password+'\n')
            new_file.write(Dob+'\n')
            new_file.write(Dob1+'\n')
            new_file.write(Dob3+'\n')
            
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="//Account has been created//")
#registeration
def register():
    global names
    global DOB
    global genders
    global passwords
    global notif
    global DOB1
    global DOB3
    names = StringVar()
    genders = StringVar()
    passwords = StringVar()
    
    #Register aman
    registeration = Toplevel(aman)
    registeration.title('ACCOUNT CREATER')
    registeration.geometry("300x300")
#Labels
    Label(registeration, text=" Please enter your correct details ",font=('Calibri',16,"bold"),bg="gray").grid(row=0,sticky=N,pady=10)
    Label(registeration, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(registeration, text="Date Of Birth", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(registeration, text="Gender", font=('Calibri',12)).grid(row=4,sticky=W)
    Label(registeration, text="Password", font=('Calibri',12)).grid(row=5,sticky=W)
    notif = Label(registeration, font=('Calibri',12))
    notif.grid(row=7,sticky=N,pady=10)

    #Entries
    Entry(registeration,textvariable=names).grid(row=1,column=0)
    # Combobox creation 
    DOB = tk.StringVar()
    DOB1 = tk.StringVar()
    DOB3 = tk.StringVar()
    monthchoosen = ttk.Combobox(registeration, width = 7, textvariable = DOB) 
# Adding combobox drop down list 
    monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 

    monthchoosen.grid(column = 0, row = 2,pady=10) 
    monthchoosen.current()
#date 
    monthchoosen1 = ttk.Combobox(registeration, width = 7, textvariable = DOB1) 
    monthchoosen1['values'] = (' 1',  
                          ' 2', 
                          ' 3', 
                          ' 4', 
                          ' 5', 
                          ' 6', 
                          ' 7', 
                          ' 8', 
                          ' 9','10', 
                          ' 11', 
                          ' 12', 
                          ' 13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31') 
    monthchoosen1.grid(column = 0, row = 2,sticky=E) 
    monthchoosen1.current()
#year
    monthchoosen2 = ttk.Combobox(registeration, width = 7, textvariable = DOB3) 
    monthchoosen2['values'] = ('1961',
                            '1962',
                            '1963',
                            '1964',
                            '1965',
                            '1966',
                            '1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982',
                            '1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998',
                            '1999','2000','2001','2002',  '2003','2004',   '2005','2006',   '2007',) 
    monthchoosen2.grid(column = 0, row = 3,sticky=S) 
    monthchoosen2.current() 
    Entry(registeration,textvariable=genders).grid(row=4,column=0)
    Entry(registeration,textvariable=passwords,show="*").grid(row=5,column=0)
#Buttons
    Button(registeration, text="Register", command = finalreg, font=('Calibri',12)).grid(row=6,sticky=N,pady=10)
    #bar
    my = Menu(registeration)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    registeration.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)

#Login
def login1():
    global loginname
    accounts = os.listdir()
    loginname = name5.get()
    loginpassword = password5.get()
    for name in accounts:
        if name == loginname:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            #Account Dashboard
            if loginpassword == password:
                loginaman.destroy()
                accountboard = Toplevel(aman)
                accountboard.title('Dashboard')
                #Labels
                Label(accountboard, text="Account Dashboard", font=('Calibri',16,"bold"),bg="gray").grid(row=0,sticky=N,pady=10)
                Label(accountboard, text="Welcome "+name, font=('Calibri',12,"bold")).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(accountboard, text="Personal Details",font= ('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(accountboard, text="Deposit",font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(accountboard,text="Withdraw",font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(accountboard).grid(row=5,sticky=N,pady=10)
#bar
                my = Menu(accountboard)
                m=Menu(my)
                m.add_command(label="Registeration",command=register)
                m.add_command(label="Login",command=login)
                accountboard.config(menu=my)
                my.add_cascade(label="Menu",menu=m)
                help=Menu(my)
                help.add_command(label="Report Problem",command=rip)
                help.add_command(label="Feedback",command=fb)
                help.add_command(label="About",command=ab)
                my.add_cascade(label="Help",menu=help)
                my.add_command(label="Exit",command=exit1)
                return
            else:
                loginnote.config(fg="red", text="Password incorrect!!")
                return
    loginnote.config(fg="red", text="No account found !!")
def deposit():
    #Vars
    global amount
    global depositnote
    global current_balance_label
    amount = StringVar()
    file   = open(loginname, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[6]
    #Deposit aman
    depositaman = Toplevel(aman)
    depositaman.title('Deposit')
    #Label
    Label(depositaman, text="Deposit", font=('Calibri',16,"bold")).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(depositaman, text="Current Balance : Rs "+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(depositaman, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    depositnote = Label(depositaman,font=('Calibri',12))
    depositnote.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(depositaman, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(depositaman,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=N,pady=10)
#bar
    my = Menu(depositaman)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    depositaman.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)

def finish_deposit():
    if amount.get() == "":
        depositnote.config(text='Write any Amount in it!',fg="red")
        return
    if float(amount.get()) <=0:
        depositnote.config(text='Negative Amount is not accepted', fg='red')
        return

    file = open(loginname, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs "+str(updated_balance),fg="green")
    depositnote.config(text='Balance Updated', fg='green')
def withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file   = open(loginname, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[6]
    #Deposit aman
    withdraw_aman = Toplevel(aman)
    withdraw_aman.title('Withdraw')
    #Label
    Label(withdraw_aman, text="Withdrawn", font=('Calibri',16,"bold"),bg="gray").grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_aman, text="Current Balance : Rs "+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_aman, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_aman,font=('Calibri',12))
    withdraw_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(withdraw_aman, textvariable=withdraw_amount).grid(row=2,column=1)
    #Button
    Button(withdraw_aman,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)
#bar
    my = Menu(withdraw_aman)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    withdraw_aman.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)
#bar
    my = Menu(withdraw_aman)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    withdraw_aman.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)
def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!',fg="red")
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return
    file = open(loginname, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]
    print(current_balance)
    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    print(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs "+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')
#PERSIONAL_DETAILS
def personal_details():
    file = open(loginname, 'r')
    file_data = file.read()
    print(file_data)
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_Dob = user_details[2]
    details_Dob1 = user_details[3]
    details_Dob3 = user_details[4]
    details_gender = user_details[5]
    details_balance = user_details[6]
    #Personal details aman
    personal_details_aman = Toplevel(aman)
    personal_details_aman.title('Personal Details')
    #Labels
    Label(personal_details_aman, text="Personal Details", font=('Calibri',22,"bold"),bg="gray").grid(row=0,sticky=N,pady=10)
    Label(personal_details_aman, text="Name : "+details_name, font=('Calibri',16,"bold")).grid(row=1,sticky=W)
    Label(personal_details_aman, text="Month : "+details_Dob, font=('Calibri',16,"bold")).grid(row=2,sticky=W)
    Label(personal_details_aman, text="Date : "+details_Dob1, font=('Calibri',16,"bold")).grid(row=3,sticky=W)
    Label(personal_details_aman, text="Year : "+details_Dob3, font=('Calibri',16,"bold")).grid(row=4,sticky=W)
    Label(personal_details_aman, text="Gender : "+details_gender, font=('Calibri',16,"bold")).grid(row=5,sticky=W)
    Label(personal_details_aman, text="Balance : Rs "+details_balance, font=('Calibri',16,"bold")).grid(row=6,sticky=W)
    Label(personal_details_aman, text=" ///THANKS/// ", font=('Calibri',10,"bold"),fg="green").grid(row=7,sticky=N)
#bar
    my = Menu(personal_details_aman)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    m.add_command(label="setting",command=set)
    personal_details_aman.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)
def login():
    global name5
    global password5
    global loginnote
    global loginaman
    name5 = StringVar()
    password5 = StringVar()
    #Login aman
    loginaman = Toplevel(aman)
    loginaman.title('Login')
    #Labels
    Label(loginaman, text="Login to your account", font=('Calibri',12,"bold"),bg="gray").grid(row=0,sticky=N,pady=10)
    Label(loginaman, text="Username", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(loginaman, text="Password", font=('Calibri',12)).grid(row=2,sticky=W)
    loginnote = Label(loginaman, font=('Calibri',12))
    loginnote.grid(row=4,sticky=N)
    #Entry
    Entry(loginaman, textvariable=name5).grid(row=1,column=1)
    Entry(loginaman, textvariable=password5,show="*").grid(row=2,column=1,padx=5)
    #Button
    Button(loginaman, text="Log in", command=login1, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)
    #bar
    my = Menu(loginaman)
    m=Menu(my)
    m.add_command(label="Registeration",command=register)
    m.add_command(label="Login",command=login)
    loginaman.config(menu=my)
    my.add_cascade(label="Menu",menu=m)
    help=Menu(my)
    help.add_command(label="Report Problem",command=rip)
    help.add_command(label="Feedback",command=fb)
    help.add_command(label="About",command=ab)
    my.add_cascade(label="Help",menu=help)
    my.add_command(label="Exit",command=exit1)


#Main aman
aman = Tk()
aman.title('Banking App (ATM)')


#exit
def exit1():
    aman.destroy()
#dcoloour
def black():
      aman.configure(bg="black")
def gray():
    aman.configure(bg="dimgray")
    
#Image import
img = Image.open('th.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(aman, text = "BHARAT BANK (ATM) ", font=('Calibri',18)).grid(row=0,sticky=N,pady=10)
Label(aman, text = " India's most secure bank ", font=('Calibri',16,"bold"),bg="gray").grid(row=1,sticky=N)
Label(aman, image=img).grid(row=2,sticky=N,pady=15)
#Buttons
Button(aman, text="Register", font=('Calibri',12),width=30,command=register).grid(row=3,sticky=N)
Button(aman, text="Log in", font=('Calibri',12),width=30,command=login).grid(row=4,sticky=N,pady=10)
#bar
my = Menu(aman)
m=Menu(my)
m.add_command(label="Registeration",command=register)
m.add_command(label="Login",command=login)
m.add_command(label="setting",command=set)
aman.config(menu=my)
my.add_cascade(label="Menu",menu=m)
help=Menu(my)
help.add_command(label="Report Problem",command=rip)
help.add_command(label="Feedback",command=fb)
help.add_command(label="About",command=ab)
my.add_cascade(label="Help",menu=help)
my.add_command(label="Exit",command=exit1)



aman.mainloop()

