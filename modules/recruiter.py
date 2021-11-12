from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label
from tkinter_uix.Entry import Entry
import mysql.connector as sql
import modules.login as l
from modules.creds import user_pwd

def get_details(email):
    global name, code, pos, role
    q = f'select name, email, position, type from Users where Email="{email}"'
    mycon = sql.connect(host='localhost', user='root',
                        passwd=user_pwd, database='mydb')
    cur = mycon.cursor()
    cur.execute(q)
    d = cur.fetchall()
    mycon.close()

    name = d[0][0]
    code = d[0][1] # I replaced email -> code
    pos = d[0][2]
    role = d[0][3]


def logi(root):
    try:
        bg.destroy()
    except:
        pass
    l.log(root)


def submit_job():
    global role1, jtype1, qual1, exp1, sal1
    role1 = role.get()
    jtype1 = jtype.get()
    qual1 = qual.get()
    exp1 = exp.get()
    sal1 = sal.get()
    print(role1, jtype1, qual1, exp1, sal1)
    if role1 and jtype1 and qual1 and exp1 and sal1:
        if jtype1 == "Select":
            messagebox.showinfo('ALERT!', 'Please provide Job Type')
        else:
            exe1 = f'INSERT INTO mydb.Job(RID, JID, JobRole, JobType, Qualification, MinExp, Salary) VALUES({recid}, NULL, "{role1}", "{jtype1}", "{qual1}", {exp1}, {sal1})'
            try:
                mycon = sql.connect(host='localhost', user='root',
                                    passwd=user_pwd, database='mydb')
                cur = mycon.cursor()
                cur.execute(exe1)
                role.delete(0, END)
                jtype.delete(0, END)
                qual.delete(0, END)
                exp.delete(0, END)
                sal.delete(0, END)
                mycon.commit()
                mycon.close()
                messagebox.showinfo('SUCCESS!', 'You have successfully created a Job')
            except:
                pass
    else:
        messagebox.showinfo('ALERT!', 'ALL FIELDS ARE MUST BE FILLED')


# -------------------------------------------- Sort Queries --------------------------------------------------------
def sort_all(table):
    criteria = search_d.get()
    if(criteria == "Select"):
        pass
    else:
        table.delete(*table.get_children())
        mycon = sql.connect(host='localhost', user='root',
                            passwd=user_pwd, database='mydb')

        cur = mycon.cursor()
        cur.execute(
            f'select RID,JID, JobRole, JobType, Qualification, MinExp, Salary FROM mydb.Job where RID={recid} order by {criteria}')
        all_jobs = cur.fetchall()
        mycon.close()
    i = 0
    for r in all_jobs:
        table.insert('', i, text="", values=(
            r[1], r[2], r[3], r[4], r[5], r[6]))
        i += 1


def sort_applicants(table):
    criteria = search_d.get()
    if(criteria == "Select"):
        pass
    else:
        table.delete(*table.get_children())
        mycon = sql.connect(host='localhost', user='root',
                            passwd=user_pwd, database='mydb')

        cur = mycon.cursor()
        cur.execute(
            f'SELECT job.JobRole, client.CName, client.CEmail, client.CAge, client.CLocation, client.CGender, client.CExp, client.CSkills, client.CQualification FROM application JOIN client ON application.cid=client.CID JOIN job ON job.jid=application.jid where job.rid={recid} order by {criteria}')
        applicats = cur.fetchall()
        mycon.close()
        print(applicats)
        i = 0
        for x in applicats:
            table.insert('', i, text="", values=(
                x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))
            i += 1
# ----------------------------------------------Posted jobs Query-----------------------------------------------


def show_all(table):
    mycon = sql.connect(host='localhost', user='root',
                        passwd=user_pwd, database='mydb')
    cur = mycon.cursor()
    cur.execute(
        f'select RID,JID, JobRole, JobType, Qualification, MinExp, Salary FROM mydb.Job where RID={recid}')
    all_jobs = cur.fetchall()
    mycon.close()
    i = 0
    for r in all_jobs:
        table.insert('', i, text="", values=(
            r[1], r[2], r[3], r[4], r[5], r[6]))
        i += 1

# ----------------------------------------------Applicants-----------------------------------------------------


def show_applicants(table):
    mycon = sql.connect(host='localhost', user='root',
                        passwd=user_pwd, database='mydb')
    cur = mycon.cursor()
    cur.execute(
        f'SELECT job.JobRole, client.CName, client.CEmail, client.CAge, client.CLocation, client.CGender, client.CExp, client.CSkills, client.CQualification FROM application JOIN client ON application.cid=client.CID JOIN job ON job.jid=application.jid where job.rid={recid}')
    applicats = cur.fetchall()
    mycon.close()
    print(applicats)
    i = 0
    for x in applicats:
        table.insert('', i, text="", values=(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))
        i += 1


# ---------------------------------------------Post a Job---------------------------------------------------
def create():
    global role, jtype, qual, exp, sal
    for widget in rt.winfo_children():
        widget.destroy()
    for widget in tab.winfo_children():
        widget.destroy()
    bgr.destroy()

    # Create Form
    f1 = Frame(rt, width=520)
    f1.load = PhotoImage(file="elements\\create.png")
    img = Label(rt, image=f1.load, bg="#FFFFFF")
    img.grid(row=0, column=1, padx=150, pady=10)

    # Form
    # Labels
    role_l = Label(tab, text="Role :", font=(
        'normal', 18, 'bold'), bg="#FFFFFF")
    role_l.grid(row=0, column=0, pady=10, padx=10)
    type_l = Label(tab, text="Type :", font=(
        'normal', 18, 'bold'), bg="#FFFFFF")
    type_l.grid(row=1, column=0, pady=10, padx=10)
    qual_l = Label(tab, text="Qualification :", font=(
        'normal', 18, 'bold'), bg="#FFFFFF")
    qual_l.grid(row=2, column=0, pady=10, padx=10)
    exp_l = Label(tab, text="Experience :", font=(
        'normal', 18, 'bold'), bg="#FFFFFF")
    exp_l.grid(row=3, column=0, pady=10, padx=10)
    sal_l = Label(tab, text="Salary :", font=(
        'normal', 18, 'bold'), bg="#FFFFFF")
    sal_l.grid(row=4, column=0, pady=10, padx=10)

    # Entries
    style = ttk.Style(tab)
    style.configure("TCombobox", background="white",
                    foreground="#696969")

    role = Entry(tab, placeholder="Enter Job Role")
    role.grid(row=0, column=1, pady=10, padx=10)
    jtype = ttk.Combobox(tab, font=("normal", 18),
                         width=23, state='readonly')
    jtype['values'] = ('Select', 'FullTime', 'PartTime', 'Intern')
    jtype.current(0)
    jtype.grid(row=1, column=1, pady=10, padx=10)
    qual = Entry(tab, placeholder="Enter Job Qualifications")
    qual.grid(row=2, column=1, pady=10, padx=10)
    exp = Entry(tab, placeholder="Enter Minimum Experience")
    exp.grid(row=3, column=1, pady=10, padx=10)
    sal = Entry(tab, placeholder="Enter Expected salary")
    sal.grid(row=4, column=1, pady=10, padx=10)

    btn = Button(tab, text="Submit", font=(20), bg="#45CE30",
                 fg="#FFFFFF", command=submit_job)
    btn.grid(row=5, column=1, pady=15)

# -------------------------------------------------Delete A Posted Job----------------------------------------------------------


def deletjob(table):
    selectedindex = table.focus()
    selectedvalues = table.item(selectedindex, 'values')
    ajid = selectedvalues[0]
    mycon = sql.connect(host='localhost', user='root',
                        passwd=user_pwd, database='mydb')
    cur = mycon.cursor()
    cur.execute(f'delete from mydb.application where jid={ajid}')
    cur.execute(f'delete from mydb.job where jid={ajid}')
    mycon.commit()
    mycon.close()
    messagebox.showinfo('Thanks', 'Your Job has been Deleted')
    posted()

# ----------------------------------------------Posted Jobs by Recruiter----------------------------------------------------


def posted():
    for widget in rt.winfo_children():
        widget.destroy()
    for widget in tab.winfo_children():
        widget.destroy()
    bgr.destroy()

    search_l = Label(rt, text="Order By : ", font=(
        'normal', 18), bg="#ffffff")
    search_l.grid(row=0, column=0, padx=10, pady=10)
    global search_d
    search_d = ttk.Combobox(rt, width=12, font=(
        'normal', 18), state='readonly')
    search_d['values'] = ('Select', 'JobRole', 'JobType')
    search_d.current(0)
    search_d.grid(row=0, column=2, padx=0, pady=10)
    search = Button(rt, text="Sort", font=('normal', 12, 'bold'),
                    bg="#00b9ed", fg="#ffffff", command=lambda: sort_all(table))
    search.grid(row=0, column=3, padx=10, pady=10, ipadx=15)
    dlt = Button(rt, text="Delete", font=('normal', 12, 'bold'),
                 bg="#00b9ed", fg="#ffffff", command=lambda: deletjob(table))
    dlt.grid(row=0, column=4, padx=10, pady=10, ipadx=5)

    scx = Scrollbar(tab, orient="horizontal")
    scy = Scrollbar(tab, orient="vertical")

    table = ttk.Treeview(tab, columns=('JID', 'JobRole', 'JobType', 'Qualification', 'MinExp', 'Salary'),
                         xscrollcommand=scx.set, yscrollcommand=scy.set)
    scx.pack(side="bottom", fill="x")
    scy.pack(side="right", fill="y")
    table.heading("JID", text="JobID")
    table.heading("JobRole", text="Role")
    table.heading("JobType", text='Type')
    table.heading("Qualification", text='Qualification')
    table.heading("MinExp", text='MinExp')
    table.heading("Salary", text="Salary")

    table['show'] = 'headings'

    scx.config(command=table.xview)
    scy.config(command=table.yview)

    table.column("JID", width=100)
    table.column("JobRole", width=150)
    table.column("JobType", width=150)
    table.column("Qualification", width=100)
    table.column("MinExp", width=100)
    table.column("Salary", width=150)
    show_all(table)
    table.pack(fill="both", expand=1)


# -----------------------------------------Applications on your recruiters posted jobs----------------------------------------------------------------
def app():
    for widget in rt.winfo_children():
        widget.destroy()
    for widget in tab.winfo_children():
        widget.destroy()
    bgr.destroy()

    search_l = Label(rt, text="Order By : ", font=('normal', 18), bg="#ffffff")
    search_l.grid(row=0, column=0, padx=10, pady=10)
    global search_d
    search_d = ttk.Combobox(rt, width=12, font=(
        'normal', 18), state='readonly')
    search_d['values'] = ('Select', 'JobRole', 'CName', 'CLocation')
    search_d.current(0)
    search_d.grid(row=0, column=2, padx=10, pady=10)
    search = Button(rt, text="Sort", font=('normal', 12, 'bold'),
                    bg="#00b9ed", fg="#ffffff", command=lambda: sort_applicants(table))
    search.grid(row=0, column=3, padx=45, pady=10, ipadx=30)

    scx = Scrollbar(tab, orient="horizontal")
    scy = Scrollbar(tab, orient="vertical")

    table = ttk.Treeview(tab, columns=('JobRole', 'CName', 'CEmail', 'CAge', 'CLocation', 'CGender', 'CExp', 'CSkills', 'CQualification'),
                         xscrollcommand=scx.set, yscrollcommand=scy.set)
    scx.pack(side="bottom", fill="x")
    scy.pack(side="right", fill="y")

    table.heading("JobRole", text="Job Role")
    table.heading("CName", text='Applicants Name')
    table.heading("CEmail", text='Email')
    table.heading("CAge", text='Age')
    table.heading("CLocation", text='Location')
    table.heading("CGender", text='Gender')
    table.heading("CExp", text='Experience')
    table.heading("CSkills", text='Skills')
    table.heading("CQualification", text='Qualification')

    table['show'] = 'headings'

    scx.config(command=table.xview)
    scy.config(command=table.yview)

    table.column("JobRole", width=150)
    table.column("CName", width=200)
    table.column("CEmail", width=100)
    table.column("CAge", width=50)
    table.column("CLocation", width=150)
    table.column("CGender", width=100)
    table.column("CExp", width=100)
    table.column("CSkills", width=200)
    table.column("CQualification", width=150)
    show_applicants(table)
    table.pack(fill="both", expand=1)


# ---------------------------------------------------------------------------------------------------------------------------
def rec(root, email1):
    global email
    email = email1
    bg = Frame(root, width=1050, height=700)
    bg.place(x=0, y=0)

    get_details(email)

    bg.load = PhotoImage(file=f'elements\\bgMenu.png')
    img = Label(root, image=bg.load)
    img.place(x=0, y=0)

    # Navbar
    nm = Label(root, text=f'{name}', font=(
        'normal', 36, 'bold'), bg="#ffffff", fg="#0A3D62")
    nm.place(x=300, y=50)
    pos_l = Label(root, text=f'{code + "  -  " + pos}', font=(
        'normal', 24), bg="#ffffff", fg="#0A3D62")
    pos_l.place(x=300, y=120)
    bn = Button(root, text="LOGOUT", font=(
        'normal', 20), bg="#b32e2e", fg="#ffffff", command=lambda: logi(root))
    bn.place(x=800, y=75)

    # Left
    lf = Frame(root, width=920, height=160, bg="#ffffff")
    # lf.place(x=70, y=220)
    lf.place(x=70, y=220)

    

    ### My Entry Grid

    # Configure the grid
    lf.columnconfigure(0, weight=1)
    lf.columnconfigure(2, weight=1)
    lf.columnconfigure(4, weight=1)
    lf.columnconfigure(1, weight=3)
    lf.columnconfigure(3, weight=3)
    lf.columnconfigure(5, weight=3)

    # Column 0
    Row_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Row ID")
    Row_ID_label.grid(column=0, row=0, sticky=W)

    Order_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Order ID")
    Order_ID_label.grid(column=0, row=1, sticky=W)

    Order_Date_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Order Date")
    Order_Date_label.grid(column=0, row=2, sticky=W)

    Ship_Date_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Ship Date")
    Ship_Date_label.grid(column=0, row=3, sticky=W)
    
    ShipMode_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Ship Mode")
    ShipMode_ID_label.grid(column=0, row=4, sticky=W)
    
    Customer_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Customer ID")
    Customer_ID_label.grid(column=0, row=5, sticky=W)
    
    # Colum 1
    Row_ID_entry = Entry(lf,  width=15, placeholder="Enter Row ID")
    Row_ID_entry.grid(column=1, row=0, sticky=W)

    Order_ID_entry = Entry(lf,  width=15, placeholder="E.g: CA-2017-152156")
    Order_ID_entry.grid(column=1, row=1, sticky=W)

    Order_Date_entry = Entry(lf,  width=15, placeholder="E.g: 11/8/2017")
    Order_Date_entry.grid(column=1, row=2, sticky=W)

    Ship_Date_entry = Entry(lf,  width=15, placeholder="E.g: 11/11/2017")
    Ship_Date_entry.grid(column=1, row=3, sticky=W)

    # Combobox
    ShipMode_ID_cbbox = ttk.Combobox(lf, values = [1, 2, 3, 4], 
                    font=('normal', 13), width=16)
    ShipMode_ID_cbbox.grid(column=1, row=4, sticky=W)
    
    Customer_ID_entry = Entry(lf,  width=15, placeholder="E.g: CG-12520")
    Customer_ID_entry.grid(column=1, row=5, sticky=W)
    


    # Column 2
    Segment_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Segment")
    Segment_ID_label.grid(column=2, row=0, padx = (30, 0), sticky=W)

    City_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="City ID")
    City_ID_label.grid(column=2, row=1, padx = (30, 0), sticky=W)

    State_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="State ID")
    State_ID_label.grid(column=2, row=2, padx = (30, 0), sticky=W)

    Postal_Code_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Postal Code")
    Postal_Code_label.grid(column=2, row=3, padx = (30, 0), sticky=W)
    
    Region_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Region ID")
    Region_ID_label.grid(column=2, row=4, padx = (30, 0), sticky=W)
    
    Product_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Product ID")
    Product_ID_label.grid(column=2, row=5, padx = (30, 0), sticky=W)


    # Column 3
    Segment_ID_cbbox = ttk.Combobox(lf, values = [1, 2, 3], 
                    font=('normal', 13), width=16)
    Segment_ID_cbbox.grid(column=3, row=0, sticky=W)

    City_ID_entry = Entry(lf,  width=15, placeholder="E.g: 3")
    City_ID_entry.grid(column=3, row=1, sticky=W)

    State_ID_entry = Entry(lf,  width=15, placeholder="E.g: 37")
    State_ID_entry.grid(column=3, row=2, sticky=W)

    Postal_Code_entry = Entry(lf,  width=15, placeholder="E.g: 90032")
    Postal_Code_entry.grid(column=3, row=3, sticky=W)

    Region_ID_cbbox = ttk.Combobox(lf, values = [1, 2, 3, 4], 
                    font=('normal', 13), width=16)
    Region_ID_cbbox.grid(column=3, row=4, sticky=W)

    Product_ID_entry = Entry(lf,  width=15, placeholder="E.g: CA-2017-152156")
    Product_ID_entry.grid(column=3, row=5, sticky=W)

    # Column 4
    Category_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Category ID")
    Category_ID_label.grid(column=4, row=0, padx = (30, 0), sticky=W)

    SubCategory_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Sub-Cat ID")
    SubCategory_ID_label.grid(column=4, row=1, padx = (30, 0), sticky=W)

    Sales_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Sales ($)")
    Sales_label.grid(column=4, row=2, padx = (30, 0), sticky=W)

    Quantity_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Quantity")
    Quantity_label.grid(column=4, row=3, padx = (30, 0), sticky=W)

    Discount_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Discount")
    Discount_label.grid(column=4, row=4, padx = (30, 0), sticky=W)

    Profit_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Profit")
    Profit_label.grid(column=4, row=5, padx = (30, 0), sticky=W)

    # Column 5
    Category_ID_cbbox = ttk.Combobox(lf, values = [1, 2, 3], 
                    font=('normal', 13), width=16)
    Category_ID_cbbox.grid(column=5, row=0, sticky=W)
    
    Sub_Category_values = [x for x in range(1, 18)]
    SubCategory_ID_entry = ttk.Combobox(lf, values = Sub_Category_values, 
                    font=('normal', 13), width=16)
    SubCategory_ID_entry.grid(column=5, row=1, sticky=W)

    Sales_entry = Entry(lf,  width=15, placeholder="E.g: 48.86")
    Sales_entry.grid(column=5, row=2, sticky=W)

    Quantity_entry = Entry(lf,  width=15, placeholder="E.g: 7")
    Quantity_entry.grid(column=5, row=3, sticky=W)

    Discount_entry = Entry(lf,  width=15, placeholder="E.g: 0.45")
    Discount_entry.grid(column=5, row=4, sticky=W)

    Profit_entry = Entry(lf,  width=15, placeholder="E.g: 34.47")
    Profit_entry.grid(column=5, row=5, sticky=W)

    # cj = Button(lf, text="Post a Job", font=(
    #     'normal', 20), bg="#b32e2e", fg="#ffffff", command=create)
    # cj.grid(row=0, column=0, padx=80, pady=40)
    
    """
    pj = Button(lf, text="Posted Jobs", font=(
        'normal', 20), bg="#b32e2e", fg="#ffffff", command=posted)
    pj.grid(row=1, column=0, padx=80, pady=40)
    ap = Button(lf, text="Applications", font=(
        'normal', 20), bg="#b32e2e", fg="#ffffff", command=app)
    ap.grid(row=2, column=0, padx=80, pady=40)
    """

    # Right
    global rt, tab, bgr
    # rt = Frame(root, width=95, height=200, bg="#ff33ff")
    # rt.place(x=60, y=520)
    tab = Frame(root, bg="#ffffff")
    tab.place(x=70, y=492, width=920, height=170)
    
    """
    bgrf = Frame(root, width=540, height=420)
    bgrf.load = PhotoImage(file="elements\\bgr.png")
    bgr = Label(root, image=bgrf.load, bg="#161E54")
    bgr.place(x=440, y=210)
    """