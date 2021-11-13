from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label
from tkinter_uix.Entry import Entry
import mysql.connector as sql
import modules.login as l
from modules.creds import user_pwd
import datetime

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
    pos  = d[0][2]
    role = d[0][3]


def logi(root):
    try:
        bg.destroy()
    except:
        pass
    l.log(root)

def convertSlashDate(date_str):
    format_str = "%d/%m/%Y"
    date_obj = datetime.datetime.strptime(date_str, format_str)

    return date_obj.strftime("%Y-%m-%d")

def convertDashDate(date_str):
    format_str = "%d-%m-%Y"
    date_obj = datetime.datetime.strptime(date_str, format_str)

    return date_obj.strftime("%Y-%m-%d")

def Save():
    myList = [Order_ID_entry, Order_Date_entry, Ship_Date_entry, ShipMode_ID_cbbox,
    Customer_ID_entry, Segment_ID_cbbox, City_ID_entry, State_ID_entry, Postal_Code_entry,
    Region_ID_cbbox, Product_ID_entry, Category_ID_cbbox, SubCategory_ID_entry,
    Sales_entry, Quantity_entry, Discount_entry, Profit_entry]

    temp = -1 # Find the pos of "" in myList
    try:
        temp = myList.index("")
    except:
        pass
    
    if temp == -1:
        messagebox.showinfo('ALERT!', 'ALL FIELDS ARE MUST BE FILLED')
        return
    

    # Row_ID = Row_ID_entry.get()
    Order_ID = Order_ID_entry.get()
    Order_Date = Order_Date_entry.get()
    Ship_Date = Ship_Date_entry.get()
    # Convert DD/MM/YYYY -> YYYY-MM-DD
    try:
        Order_Date.index("/")
        Order_Date = convertSlashDate(Order_Date)
    except:
        Order_Date = convertDashDate(Order_Date)

    try:
        Ship_Date.index("/")
        Ship_Date = convertSlashDate(Ship_Date)
    except:
        Ship_Date = convertDashDate(Ship_Date)
    # print("Ship Date: ", Ship_Date)
    # ['CA-2017-152156', '2017-11-14', '2017-2-23', 3, 'CG-12520', 2, 3, 33, 42420, 1, 'FUR-BO-10001798', 
    # 2, 5, 1112.11, 20, 0.3, 340.5]
    
    ShipMode_ID = int(ShipMode_ID_cbbox.get())
    Customer_ID = Customer_ID_entry.get()
    Segment_ID = int(Segment_ID_cbbox.get())
    City_ID = int(City_ID_entry.get())
    State_ID = int(State_ID_entry.get())
    Postal_Code = int(Postal_Code_entry.get())
    Region_ID = int(Region_ID_cbbox.get())
    Product_ID = Product_ID_entry.get()
    Category_ID = int(Category_ID_cbbox.get())
    SubCategory_ID = int(SubCategory_ID_entry.get())
    Sales = float(Sales_entry.get())
    Quantity = int(Quantity_entry.get())
    Discount = float(Discount_entry.get())
    Profit = float(Profit_entry.get())

    
    exe1 = f'''INSERT INTO mydb.Entry(
    Order_ID, Order_Date, Ship_Date, ShipMode_ID, Customer_ID, 
    Segment_ID, City_ID, State_ID, Postal_Code, Region_ID, Product_ID, 
    Category_ID, SubCategory_ID, Sales, Quantity, Discount, Profit)

    VALUES("{Order_ID}", "{Order_Date}", "{Ship_Date}", "{ShipMode_ID}", "{Customer_ID}", 
    "{Segment_ID}", "{City_ID}", "{State_ID}", "{Postal_Code}", "{Region_ID}", "{Product_ID}", 
    "{Category_ID}", "{SubCategory_ID}", "{Sales}", "{Quantity}", "{Discount}", "{Profit}")'''
        
    # VALUES({ 'CA-2017-152156'}, { '11/8/2017'}, { '11/11/2017'}, { 3}, { 'CG-12520'}, { 2}, { 3}, { 33}, { 42420}, { 1}, { 'FUR-BO-10001798'}, { 2}, { 5}, { 1112.11}, { 20}, { 0.3}, { 340.5})'''

    try:
        mycon = sql.connect(host='localhost', user='root',
                            passwd=user_pwd, database='mydb')
        cur = mycon.cursor()
        cur.execute(exe1)

        Row_ID_entry.delete(0, END)
        Order_ID_entry.delete(0, END)
        Order_Date_entry.delete(0, END)
        Ship_Date_entry.delete(0, END)
        ShipMode_ID_cbbox.delete(0, END)
        Customer_ID_entry.delete(0, END)
        Segment_ID_cbbox.delete(0, END)
        City_ID_entry.delete(0, END)
        State_ID_entry.delete(0, END)
        Postal_Code_entry.delete(0, END)
        Region_ID_cbbox.delete(0, END)
        Product_ID_entry.delete(0, END)
        Category_ID_cbbox.delete(0, END)
        SubCategory_ID_entry.delete(0, END)
        Sales_entry.delete(0, END)
        Quantity_entry.delete(0, END)
        Discount_entry.delete(0, END)
        Profit_entry.delete(0, END)

        mycon.commit()
        mycon.close()

        # Also call list_records function
        show_records(True)

        messagebox.showinfo('SUCCESS!', 'You have successfully created a new record {}'.format(Order_Date))
    except:
        messagebox.showinfo('FAILED!', 'Faild to create a new record')
    
    


def count_blank(entry_list):
    count = 0
    for item in entry_list:
        if item == "" or item == "''":
            count += 1

    return count

def convertSlashDateObject(date_str):
    format_str = "%d/%m/%Y"
    date_obj = datetime.datetime.strptime(date_str, format_str)

    return date_obj.strftime("%Y-%m-%d")

def convertDashDateObject(date_str):
    format_str = "%d-%m-%Y"
    date_obj = datetime.datetime.strptime(date_str, format_str)

    return date_obj.strftime("%Y-%m-%d")

def Search():


    Order_ID1 = "'" + Order_ID_entry1.get() + "'"
    Order_Date1 = Order_Date_entry1.get()
    if Order_Date1 != "":
        # Convert DD/MM/YYYY -> YYYY-MM-DD
        try:
            Order_Date1.index("/")
            Order_Date1 = " DATE('" + convertSlashDate(Order_Date1) + "') "
        except:
            Order_Date1 = " DATE('" + convertDashDate(Order_Date1) + "') "
    
    ShipMode_ID1 = ShipMode_ID_cbbox1.get()
    if ShipMode_ID1 != "":
        ShipMode_ID1 = int(ShipMode_ID1)

    Customer_ID1 = "'" + Customer_ID_entry1.get() + "'"
    Segment_ID1 = Segment_ID_cbbox1.get()
    if Segment_ID1 != "":
        Segment_ID1 = int(Segment_ID1)

    City_ID1 = City_ID_entry1.get()
    if City_ID1 != "":
        City_ID1 = int(City_ID1)

    Product_ID1 = "'" + Product_ID_entry1.get() + "'"
    SubCategory_ID1 = SubCategory_ID_entry1.get()
    if SubCategory_ID1 != "":
        SubCategory_ID1 = int(SubCategory_ID1)
        
    Sales1 = Sales_entry1.get()
    if Sales1 != "":
        Sales1 = float(Sales1)

    Quantity1 = Quantity_entry1.get()
    if Quantity1 != "":
        Quantity1 = int(Quantity1)
    
    Discount1 = Discount_entry1.get()
    if Discount1 != "":
        Discount1 = float(Discount1)

    Profit1 = Profit_entry1.get()
    if Profit1 != "":
        Profit1 = float(Profit1)

    Query1 = Query_entry.get("1.0",'end-1c')

    myDict = {"Order_ID" : Order_ID1, "Order_Date" : Order_Date1, "ShipMode_ID" : ShipMode_ID1, 
    "Customer_ID" : Customer_ID1, "Segment_ID" : Segment_ID1, "City_ID" : City_ID1, 
    "Product_ID" : Product_ID1, "SubCategory_ID" : SubCategory_ID1, 
    "Sales" : Sales1, "Quantity" : Quantity1, "Discount" : Discount1, "Profit" : Profit1}

    # print("My List: ", myDict)

    blank = count_blank(myDict.values())

    if blank == 12 and Query1 == "":
        exe1 = ''' SELECT * 
                    FROM mydb.Entry 
                    LIMIT 15;'''
        try:
            mycon = sql.connect(host='localhost', user='root',
                                passwd=user_pwd, database='mydb')
            cur = mycon.cursor()
            cur.execute(exe1)

            show_query_records(cur.fetchall())
            mycon.close()

        except:
            messagebox.showinfo('FAILED!', 'Faild to search for your record')

        messagebox.showinfo('ALERT!', 'PLEASE FILL IN ENTRIES/SQL BOX')

    elif blank < 12 and Query1 != "":
        messagebox.showinfo('ALERT!', 'REMOVE ENTRIES/SQL BOX. CAN NOT APPLY BOTH!')
    elif blank < 12: # Entry box search
        
        filter = "WHERE ".format(Order_ID1)

        for key, value in myDict.items():
            if value != "" and value != "''":
                filter += key + " = {} AND ".format(value)
        filter = filter[: -4]

        exe1 = ''' SELECT * 
                    FROM mydb.Entry 
                    {}
                    LIMIT 15;'''.format(filter)
        # print("My Query: ", exe1)

        # VALUES({ 'CA-2017-152156'}, { '11/8/2017'}, { '11/11/2017'}, { 3}, { 'CG-12520'}, { 2}, { 3}, { 33}, { 42420}, { 1}, { 'FUR-BO-10001798'}, { 2}, { 5}, { 1112.11}, { 20}, { 0.3}, { 340.5})'''

        try:
            mycon = sql.connect(host='localhost', user='root',
                                passwd=user_pwd, database='mydb')
            cur = mycon.cursor()
            cur.execute(exe1)
            """
            Row_ID_entry.delete(0, END)
            Order_ID_entry.delete(0, END)
            Order_Date_entry.delete(0, END)
            Ship_Date_entry.delete(0, END)
            ShipMode_ID_cbbox.delete(0, END)
            Customer_ID_entry.delete(0, END)
            Segment_ID_cbbox.delete(0, END)
            City_ID_entry.delete(0, END)
            State_ID_entry.delete(0, END)
            Postal_Code_entry.delete(0, END)
            Region_ID_cbbox.delete(0, END)
            Product_ID_entry.delete(0, END)
            Category_ID_cbbox.delete(0, END)
            SubCategory_ID_entry.delete(0, END)
            Sales_entry.delete(0, END)
            Quantity_entry.delete(0, END)
            Discount_entry.delete(0, END)
            Profit_entry.delete(0, END)
            """

            # Also call list_records function
            show_query_records(cur.fetchall())
            mycon.close()

            # messagebox.showinfo('SUCCESS!', 'You have successfully created a new record')
        except:
            messagebox.showinfo('FAILED!', 'Failed to search for your record')
    else:
        exe1 = Query1

        try:
            mycon = sql.connect(host='localhost', user='root',
                                passwd=user_pwd, database='mydb')
            cur = mycon.cursor()
            cur.execute(exe1)

            show_query_records(cur.fetchall())
            mycon.close()
        except:
            messagebox.showinfo('FAILED!', 'Failed to search for your record')
    
# ----------------------------------------------Applicants-----------------------------------------------------


def show_records(update = False):
    mycon = sql.connect(host='localhost', user='root',
                        passwd=user_pwd, database='mydb')
    cur = mycon.cursor()
    if update:
        cur.execute(
        f'SELECT * FROM mydb.Entry ORDER BY Row_ID DESC LIMIT 15;')
    else:
        cur.execute(
        f'SELECT * FROM mydb.Entry LIMIT 15;')
    #    f'SELECT job.JobRole, client.CName, client.CEmail, client.CAge, client.CLocation, client.CGender, client.CExp, client.CSkills, client.CQualification FROM application JOIN client ON application.cid=client.CID JOIN job ON job.jid=application.jid where job.rid={recid}')
    records = cur.fetchall()
    mycon.close()
    i = 0

    for item in table.get_children():
        table.delete(item)

    for x in records:
        table.insert('', i, text="", values=(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10],
            x[11], x[12], x[13], x[14], x[15], x[16], x[17]))
        i += 1

def show_query_records(records):
    i = 0
    for item in table.get_children():
        table.delete(item)

    for x in records:
        table.insert('', i, text="", values=(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10],
            x[11], x[12], x[13], x[14], x[15], x[16], x[17]))
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

# -----------------------------------------Applications on your recruiters posted jobs----------------------------------------------------------------
def list_records():
    scx = Scrollbar(tab, orient="horizontal")
    scy = Scrollbar(tab, orient="vertical")

    global table
    table = ttk.Treeview(tab, columns=("Row_ID", "Order_ID", "Order_Date", "Ship_Date", 
    "ShipMode_ID","Customer_ID", "Segment_ID", "City_ID", "State_ID", "Postal_Code",
    "Region_ID", "Product_ID", "Category_ID", "SubCategory_ID",
    "Sales", "Quantity", "Discount", "Profit"),
                         xscrollcommand=scx.set, yscrollcommand=scy.set)
    scx.pack(side="bottom", fill="x")
    scy.pack(side="right", fill="y")

    table.heading("Row_ID", text='Row_ID')
    table.heading("Order_ID", text="Order_ID")
    table.heading("Order_Date", text='Order_Date')
    table.heading("Ship_Date", text='Ship_Date')
    table.heading("ShipMode_ID", text='ShipMode_ID')

    table.heading("Customer_ID", text='Customer_ID')
    table.heading("Segment_ID", text='Segment_ID')
    table.heading("City_ID", text='City_ID')
    table.heading("State_ID", text='State_ID')
    table.heading("Postal_Code", text='Postal_Code')
    table.heading("Region_ID", text='Region_ID')
    table.heading("Product_ID", text='Product_ID')

    table.heading("Category_ID", text='Category_ID')
    table.heading("SubCategory_ID", text='SubCategory_ID')
    table.heading("Sales", text='Sales')
    table.heading("Quantity", text='Quantity')
    table.heading("Discount", text='Discount')
    table.heading("Profit", text='Profit')


    table['show'] = 'headings'

    scx.config(command=table.xview)
    scy.config(command=table.yview)

    table.column("Row_ID", width=50)
    table.column("Order_ID", width=50)
    table.column("Order_Date", width=50)
    table.column("Ship_Date", width=50)
    table.column("ShipMode_ID", width=50)
    table.column("Customer_ID", width=50)
    table.column("Segment_ID", width=50)
    table.column("City_ID", width=50)
    table.column("State_ID", width=50)
    table.column("Postal_Code", width=50)
    table.column("Region_ID", width=50)
    table.column("Product_ID", width=50)
    table.column("Category_ID", width=50)
    table.column("SubCategory_ID", width=50)
    table.column("Sales", width=50)
    table.column("Quantity", width=50)
    table.column("Discount", width=50)
    table.column("Profit", width=50)
    show_records()
    table.pack(fill="both", expand=1)


# ---------------------------------------------------------------------------------------------------------------------------
def fill_in(root, email1):
    global email
    global Row_ID_entry, Order_ID_entry, Order_Date_entry, Ship_Date_entry, ShipMode_ID_cbbox, Customer_ID_entry
    global Segment_ID_cbbox, City_ID_entry, State_ID_entry, Postal_Code_entry, Region_ID_cbbox, Product_ID_entry
    global Category_ID_cbbox, SubCategory_ID_entry, Sales_entry, Quantity_entry, Discount_entry, Profit_entry

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

    Order_Date_entry = Entry(lf,  width=15, placeholder="E.g: DD/MM/YYYY")
    Order_Date_entry.grid(column=1, row=2, sticky=W)

    Ship_Date_entry = Entry(lf,  width=15, placeholder="E.g: DD/MM/YYYY")
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

    # global myWidgets
    # myWidgets = [Row_ID_entry, Order_ID_entry, Order_Date_entry, Ship_Date_entry, 
    # ShipMode_ID_cbbox, Customer_ID_entry, Segment_ID_cbbox, City_ID_entry, 
    # State_ID_entry, Postal_Code_entry, Region_ID_cbbox, Product_ID_entry, 
    # Category_ID_cbbox, SubCategory_ID_entry, Sales_entry, Quantity_entry, 
    # Discount_entry, Profit_entry]

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
    list_records()
    
    root.bn = PhotoImage(file="elements\\floppy.png") 
    Save_Record = Button(root, font=('normal', 13), bg='#FFFFFF', activebackground="#ffffff", image=root.bn, text="Save Record", compound="left", command=Save) 
    Save_Record.place(x=475, y=447)

    root.fill_in = PhotoImage(file="elements\\query.png") 
    Fill_In_btn = Button(root, font=('normal', 13, "bold"), bg='#FBF3E4', activebackground="#ffffff", 
    image=root.fill_in, text="  Switch to Query ", compound="left", command=lambda: query(root, email1)) 
    Fill_In_btn.place(x=150, y=447)


# Query Record---------------------------------------------------------------------------------------------------------------------------
def query(root, email1):
    global email
    global Order_ID_entry1, Order_Date_entry1, ShipMode_ID_cbbox1, Customer_ID_entry1
    global Segment_ID_cbbox1, City_ID_entry1, Product_ID_entry1
    global SubCategory_ID_entry1, Sales_entry1, Quantity_entry1, Discount_entry1
    global Profit_entry1, Query_entry

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
    Order_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Order ID")
    Order_ID_label.grid(column=0, row=0, sticky=W)

    Order_Date_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Order Date")
    Order_Date_label.grid(column=0, row=1, sticky=W)
    
    ShipMode_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Ship Mode")
    ShipMode_ID_label.grid(column=0, row=2, sticky=W)
    
    Customer_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Customer ID")
    Customer_ID_label.grid(column=0, row=3, sticky=W)

    Segment_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Segment")
    Segment_ID_label.grid(column=0, row=4, padx = (30, 0), sticky=W)

    City_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="City ID")
    City_ID_label.grid(column=0, row=5, padx = (30, 0), sticky=W)
    
    # Colum 1
    Order_ID_entry1 = Entry(lf,  width=15, placeholder="E.g: CA-2017-152156")
    Order_ID_entry1.grid(column=1, row=0, sticky=W)

    Order_Date_entry1 = Entry(lf,  width=15, placeholder="E.g: DD/MM/YYYY")
    Order_Date_entry1.grid(column=1, row=1, sticky=W)

            # Combobox
    ShipMode_ID_cbbox1 = ttk.Combobox(lf, values = [1, 2, 3, 4], 
                    font=('normal', 13), width=16)
    ShipMode_ID_cbbox1.grid(column=1, row=2, sticky=W)
    
    Customer_ID_entry1 = Entry(lf,  width=15, placeholder="E.g: CG-12520")
    Customer_ID_entry1.grid(column=1, row=3, sticky=W)

    Segment_ID_cbbox1 = ttk.Combobox(lf, values = [1, 2, 3], 
                    font=('normal', 13), width=16)
    Segment_ID_cbbox1.grid(column=1, row=4, sticky=W)

    City_ID_entry1 = Entry(lf,  width=15, placeholder="E.g: 3")
    City_ID_entry1.grid(column=1, row=5, sticky=W)
    


    # Column 2
    Product_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Product ID")
    Product_ID_label.grid(column=2, row=0, padx = (30, 0), sticky=W)

    SubCategory_ID_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Sub-Cat ID")
    SubCategory_ID_label.grid(column=2, row=1, padx = (30, 0), sticky=W)

    Sales_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Sales ($)")
    Sales_label.grid(column=2, row=2, padx = (30, 0), sticky=W)

    Quantity_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Quantity")
    Quantity_label.grid(column=2, row=3, padx = (30, 0), sticky=W)

    Discount_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Discount")
    Discount_label.grid(column=2, row=4, padx = (30, 0), sticky=W)

    Profit_label = Label(lf, bg='#FFFFFF', font=('normal', 14, 'bold'), fg="#161E54", text="Profit")
    Profit_label.grid(column=2, row=5, padx = (30, 0), sticky=W)

    # Column 3
    Product_ID_entry1 = Entry(lf,  width=15, placeholder="E.g: CA-2017-152156")
    Product_ID_entry1.grid(column=3, row=0, sticky=W)

    Sub_Category_values = [x for x in range(1, 18)]
    SubCategory_ID_entry1 = ttk.Combobox(lf, values = Sub_Category_values, 
                    font=('normal', 13), width=16)
    SubCategory_ID_entry1.grid(column=3, row=1, sticky=W)

    Sales_entry1 = Entry(lf,  width=15, placeholder="E.g: 48.86")
    Sales_entry1.grid(column=3, row=2, sticky=W)

    Quantity_entry1 = Entry(lf,  width=15, placeholder="E.g: 7")
    Quantity_entry1.grid(column=3, row=3, sticky=W)

    Discount_entry1 = Entry(lf,  width=15, placeholder="E.g: 0.45")
    Discount_entry1.grid(column=3, row=4, sticky=W)

    Profit_entry1 = Entry(lf,  width=15, placeholder="E.g: 34.47")
    Profit_entry1.grid(column=3, row=5, sticky=W)

    ####
    # Column 4-5
    Query_label = Label(lf, width=20, bg='#FFFFFF', font=('normal', 13, 'bold'), fg="#000D6B", text="SQL query Entry table")
    Query_label.grid(column=4, row=0, padx = (30, 0), sticky=N, columnspan=2)

    # Column 4-5
    Query_entry = Text(lf, width=30, height=9, font=("Helvetica", 13), bg="#FBF3E4")
    Query_entry.grid(column=4, row=1, padx = (30, 0), sticky=W, rowspan=5, columnspan=2)

    # Right
    global rt, tab, bgr
    # rt = Frame(root, width=95, height=200, bg="#ff33ff")
    # rt.place(x=60, y=520)
    tab = Frame(root, bg="#ffffff")
    tab.place(x=70, y=492, width=920, height=170)
    list_records()

    root.bn = PhotoImage(file="elements\\search.png") 
    Search_Record = Button(root, font=('normal', 13, "bold"), bg='#FFFFFF', activebackground="#ffffff", 
    image=root.bn, text="Search", compound="left", command=Search)
    Search_Record.place(x=475, y=447)

    root.fill_in = PhotoImage(file="elements\\fill-in.png") 
    Fill_In_btn = Button(root, font=('normal', 13, "bold"), bg='#FBF3E4', activebackground="#ffffff", 
    image=root.fill_in, text="  Switch to Fill-IN ", compound="left", command=lambda: fill_in(root, email1)) 
    Fill_In_btn.place(x=150, y=447)

    # Save_Record = Button(root, text="Save Record", font=(
    #     'normal', 13), bg="#b32e2e", fg="#ffffff", command=lambda: logi(root))
    
    

    