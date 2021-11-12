import mysql.connector as mysql
import modules.login as l
from modules.creds import user_pwd
 
# , 
# Regieon_ID, Product_ID, Category_ID, SubCategory_ID, 
# Sales, Quantity, Discount, Profit

# { 2}, { 3}, { 33}, { 42420}, { 1}, { 'FUR-BO-10001798'}, { 2}, { 5}, { 1112.11}, { 20}, { 0.3}, { 340.5}

exe1 = f'''INSERT INTO mydb.Entry1(Order_ID, Order_Date, Ship_Date, ShipMode_ID, Customer_ID,
            Segment_ID, City_ID, State_ID, Postal_Code) 
VALUES('CG-12520', '2017-11-8', '2017-11-11',  3,  'FUR-BO-10001798', 
            2, 3, 3, 42420)'''


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "mydb"
)

cursor = db.cursor()

## getting all the tables which are present in 'datacamp' database
# cursor.execute(exe1)
# db.commit()

exe1 = "DROP TABLE mydb.entry"
# exe1 = "DELETE FROM mydb.entry WHERE Order_ID = 6"
cursor.execute(exe1)
# db.commit()

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)