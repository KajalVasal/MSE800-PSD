import sqlite3
conn = sqlite3.connect('money_exchange.db')
cursor = conn.cursor()

# Bank 
cursor.execute('''
CREATE TABLE IF NOT EXISTS Bank(
    Bank_id INTEGER PRIMARY KEY,
    Bank_Name TEXT NOT NULL,
    SWIFT_Code TEXT NOT NULL,
    Branch_Code TEXT NOT NULL,
    Bank_Country TEXT NOT NULL,
    UNIQUE(SWIFT_Code, Branch_Code)
);''')

# Customer 
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer(
    Customer_id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Phone INTEGER NOT NULL,
    Passport_no INTEGER NOT NULL
);''')

# Account
cursor.execute('''
CREATE TABLE IF NOT EXISTS Account(
    Account_no INTEGER PRIMARY KEY,
    Customer_id INTEGER NOT NULL,
    Bank_id INTEGER NOT NULL,
    Account_Type TEXT NOT NULL,
    Balance REAL NOT NULL,
    FOREIGN KEY (Customer_id)REFERENCES Customer(Customer_id),
    FOREIGN KEY (Bank_id)REFERENCES Bank(Bank_id)
);''')

# Currency
cursor.execute('''
CREATE TABLE IF NOT EXISTS Currency(
    Currency_Code CHAR(50) PRIMARY KEY,
    Currency_Name TEXT NOT NULL,
    Exchange_Rate REAL NOT NULL,
    Symbol TEXT NOT NULL,
    Active_Status BOOLEAN NOT NULL
);''')

# Transaction
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions(
    Trans_id INTEGER PRIMARY KEY,
    Account_no INTEGER NOT NULL,
    Currency_Code CHAR(50) NOT NULL,
    Amount REAL NOT NULL,
    Trans_Date DATE NOT NULL,
    FOREIGN KEY (Account_no)REFERENCES Account(Account_no),
    FOREIGN KEY (Currency_Code)REFERENCES Currency(Currency_Code)
);''')

conn.commit()
conn.close()
print("Database money_exchange.db created successfully")

