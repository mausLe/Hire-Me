from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label
from tkinter_uix.Entry import Entry
import mysql.connector as sql
import modules.login as l
from modules.creds import user_pwd

def logi(root):
    try:
        r2.destroy()
        r3.destroy()
    except:
        pass
    l.log(root)

def recruiter_regis(root):
    global name, email, pwd, cpwd, pos, role
    # r1.destroy()
    r2 = Frame(root, height=700, width=1050)
    r2.place(x=0, y=0)
    r2.render = PhotoImage(file="elements/reg_bg.png")
    img = Label(r2, image=r2.render)
    img.place(x=0, y=0)
    name_l = Label(r2, text="Name : ", bg='#FFFFFF', fg="#00B9ED",
                   font=('normal', 20, 'bold'))
    name_l.place(x=100, y=200)
    name = Entry(r2, placeholder='Enter Your Full Name...', width=20)
    name.place(x=290, y=200)

    email_l = Label(r2, text="Code : ", bg='#FFFFFF', fg="#00B9ED",
                    font=('normal', 20, 'bold'))
    email_l.place(x=100, y=250)
    email = Entry(r2, placeholder='Employee Code', width=20)
    email.place(x=290, y=250)

    # My new fields
    role_l = Label(r2, text="Role : ", bg='#FFFFFF', fg="#00B9ED",
                    font=('normal', 20, 'bold'))
    role_l.place(x=100, y=300)
    role = ttk.Combobox(r2, values = ["Admin", "Manager", "Employee"], 
                    font=('normal', 13), width=21)
    # role = Entry(r2, placeholder='Your Role', width=20)
    role.place(x=290, y=300)


    pos_l = Label(r2, text="Position : ", bg='#FFFFFF', fg="#00B9ED",
                    font=('normal', 20, 'bold'))
    pos_l.place(x=100, y=350)
    pos = Entry(r2, placeholder='Your Position', width=20)
    pos.place(x=290, y=350)
    # End of my new fields

    pwd_l = Label(r2, text="Password : ", bg='#FFFFFF', fg="#00B9ED",
                  font=('normal', 20, 'bold'))
    pwd_l.place(x=100, y=400)
    pwd = Entry(r2, placeholder='Password', show="*", width=20)
    pwd.place(x=290, y=400)

    con_pwd_l = Label(r2, text="Confirm : ", bg='#FFFFFF', fg="#00B9ED",
                      font=('normal', 20, 'bold'))
    con_pwd_l.place(x=100, y=450)
    cpwd = Entry(r2, placeholder='Confirm Password', show="*", width=20)
    cpwd.place(x=290, y=450)

    # r2.bn = PhotoImage(file="elements\\next1.png")
    r2.bn = PhotoImage(file="elements\\reg.png")
    
    btn = Button(r2, image=r2.bn, bg='#FFFFFF', bd=0,
                 activebackground="#ffffff", command=lambda: recruiter_check(root))
    btn.place(x=342, y=550)

    # TAL Code
    r2.back = PhotoImage(file="elements\\backlogin.png")
    btn2 = Button(r2, image=r2.back, bg='#FFFFFF', bd=0,
                  activebackground="#ffffff", command=lambda: logi(root))
    btn2.place(x=103, y=550)
    # End of TAL Code


def recruiter_check(root):
    global name1, email1, pwd1, cpwd1, role1, pos1
    name1 = name.get()
    email1 = email.get()
    pwd1 = pwd.get()
    cpwd1 = cpwd.get()
    pos1 = pos.get()
    role1 = role.get()
    

    print("Name {} Code {} Pass {} - {}; Position {}; Role {}".format(name1, email1, pwd1, cpwd1, pos1, role1))
    if name1 and email1 and pwd1 and cpwd1:
        mycon = sql.connect(host='localhost', user='root',
                            passwd=user_pwd, database='mydb')
        cur = mycon.cursor()
        cur.execute('select email from users')
        total = cur.fetchall()
        mycon.close()
        exist_email = []
        for i in total:
            exist_email.append(i[0])
        print("existing users:", exist_email)

        if email1 in exist_email:
            messagebox.showinfo('ALERT!', 'CODE ALREADY REGISTERED')
            email.delete(0, END)

        else:
            if pwd1 == cpwd1:
                # recruit_complete(root)
                recruiter_submit(root)
            else:
                messagebox.showinfo('ALERT!', 'PASSWORDS DO NOT MATCH')

    else:
        messagebox.showinfo('ALERT!', 'ALL FIELDS ARE MUST BE FILLED')


def recruit_complete(root):
    print("hello ", name1, ", Let's complete your profile")
    r3 = Frame(root, height=700, width=1050)
    r3.place(x=0, y=0)
    r3.render = PhotoImage(file="elements/reg_bg.png")
    img = Label(r3, image=r3.render)
    img.place(x=0, y=0)

    global gender, company, loc
    gender = StringVar()

    style = ttk.Style(r3)
    style.configure("TRadiobutton", background="white",
                    foreground="#696969", font=("arial", 16, "bold"))

    gender_l = Label(r3, text="Gender : ", bg='#FFFFFF', fg="#00B9ED",
                     font=('normal', 20, 'bold'))
    gender_l.place(x=100, y=250)
    ttk.Radiobutton(r3, text="Male", value="M", variable=gender).place(
        x=300, y=250)
    ttk.Radiobutton(r3, text="Female", value="F", variable=gender).place(
        x=400, y=250)

    company_l = Label(r3, text="Company : ", bg='#FFFFFF', fg="#00B9ED",
                      font=('normal', 20, 'bold'))
    company_l.place(x=100, y=300)
    company = Entry(r3, placeholder='Company', width=20)
    company.place(x=290, y=300)

    loc_l = Label(r3, text="Location : ", bg='#FFFFFF', fg="#00B9ED",
                  font=('normal', 20, 'bold'))
    loc_l.place(x=100, y=350)
    loc = Entry(r3, placeholder='Location', width=20)
    loc.place(x=290, y=350)

    r3.bn = PhotoImage(file="elements\\reg.png")
    btn = Button(r3, image=r3.bn, bg='#FFFFFF', bd=0,
                 activebackground="#ffffff", command=lambda: recruiter_submit(root))
    btn.place(x=320, y=500)


def recruiter_submit(root):
    print(name1, email1, role1, pos1)
    exe = f'insert into users values("{name1}","{email1}", "{pos1}", "{role1}","{pwd1}")'
    # exe1 = f'INSERT INTO mydb.Recruiter(RID, RName, REmail, CompanyName, CompanyLocation ,RGender) VALUES (NULL,"{name1}","{email1}","{company1}","{loc1}","{gender1}")'
    try:
        mycon = sql.connect(host='localhost', user='root',
                            passwd=user_pwd, database='mydb')
        cur = mycon.cursor()
        cur.execute(exe)
        # cur.execute(exe1)
        name.delete(0, END)
        email.delete(0, END)
        pos.delete(0, END)
        role.delete(0, END)
        pwd.delete(0, END)
        cpwd.delete(0, END)
        # gender.delete(0, END)
        # loc.delete(0, END)
        # company.delete(0, END)
        mycon.commit()
        mycon.close()
        messagebox.showinfo('SUCCESS!', 'Registration Successful')
        logi(root)
    except:
        messagebox.showinfo('FAILED!', 'Registration NOT Successful')
        pass
