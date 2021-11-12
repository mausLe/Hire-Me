CREATE_SCHEMA = """
CREATE SCHEMA IF NOT EXISTS `mydb`;
"""

Create_users_Table = """
CREATE TABLE IF NOT EXISTS mydb.Users( 
        name VARCHAR(45) NOT NULL, 
        email Varchar(120) Not NULL,   
        position VARCHAR(45) NOT NULL, 
        type VARCHAR(45) NOT NULL,
        password VARCHAR(45) NULL,  
        UNIQUE INDEX email_UNIQUE (email), 
        CHECK (type in ('Admin','Manager', 'Employee')),
        PRIMARY KEY (email)   );
  """
# 			
# 	
# 	
# Sales	Quantity	Discount	Profit

Create_Entry_Table_1 = """
CREATE TABLE IF NOT EXISTS mydb.Entry1 (
  Row_ID INT NOT NULL AUTO_INCREMENT,
  Order_ID VARCHAR(20) NOT NULL,
  Order_Date DATE NOT NULL,
  Ship_Date	DATE NOT NULL,
  ShipMode_ID	INT NOT NULL,
  Customer_ID VARCHAR(20) NOT NULL,  
  PRIMARY KEY (Row_ID)
  );
  """

Create_Entry_Table = """
CREATE TABLE IF NOT EXISTS mydb.Entry (
  Row_ID INT NOT NULL AUTO_INCREMENT,
  Order_ID VARCHAR(20) NOT NULL,
  Order_Date DATE NOT NULL,
  Ship_Date	DATE NOT NULL,
  ShipMode_ID	INT NOT NULL,
  Customer_ID VARCHAR(20) NOT NULL,
  Segment_ID INT NOT NULL, 
  City_ID	INT NOT NULL,
  State_ID	INT NOT NULL, 
  Postal_Code	INT NOT NULL, 
  Region_ID INT NOT NULL,
  Product_ID	VARCHAR(20) NOT NULL,
  Category_ID	INT NOT NULL,
  SubCategory_ID INT NOT NULL,
  Sales	DOUBLE(14, 6) NOT NULL,
  Quantity INT NOT NULL, 
  Discount DOUBLE(5, 4) NOT NULL,
  Profit DOUBLE(14, 6) NOT NULL,
  PRIMARY KEY (Row_ID)
  );
  """


Create_recruiter_Table = """
CREATE TABLE IF NOT EXISTS mydb.Recruiter(
  RID INT NOT NULL AUTO_INCREMENT,

  
  RName VARCHAR(45) NOT NULL,
  REmail VARCHAR(45) NOT NULL,
  CompanyName VARCHAR(45) NOT NULL,
  CompanyLocation VARCHAR(45) NOT NULL,
  RGender VARCHAR(2) NOT NULL,
   PRIMARY KEY (RID),
   UNIQUE (REmail)
   );
  """
Create_client_Table = """
CREATE TABLE IF NOT EXISTS mydb.Client (
  CID INT NOT NULL AUTO_INCREMENT,
  CName VARCHAR(45) NOT NULL,
  CEmail VARCHAR(45) NOT NULL,
  CAge INT NOT NULL,
  CLocation VARCHAR(45) NOT NULL,
  CGender VARCHAR(2) NOT NULL,
  CExp INT NOT NULL,
  CSkills VARCHAR(45) NOT NULL,
  CQualification VARCHAR(45) NOT NULL,
  UNIQUE (CEmail),
  PRIMARY KEY (CID)
  );
  """

Create_Job_Table = """
CREATE TABLE IF NOT EXISTS mydb.Job (
  RID INT NOT NULL,
  JID INT NOT NULL AUTO_INCREMENT,
  JobRole VARCHAR(45) NOT NULL,
  JobType VARCHAR(45) NOT NULL,
  Qualification VARCHAR(45) NOT NULL,
  MinExp INT NOT NULL,
  Salary INT NOT NULL,
  FOREIGN KEY (RID) REFERENCES mydb.Recruiter(RID),
  PRIMARY KEY (JID)
  );
  """

Create_Application_Table="""
CREATE TABLE IF NOT EXISTS mydb.Application(
    AID INT NOT NULL AUTO_INCREMENT,
    RID INT NOT NULL,
    JID INT NOT NULL,
    CID INT NOT NULL,
    PRIMARY KEY(AID),
    FOREIGN KEY(RID) REFERENCES mydb.Recruiter(RID),
    FOREIGN KEY(JID) REFERENCES mydb.Job(JID),
    FOREIGN KEY(CID) REFERENCES mydb.Client(CID)
);
"""

