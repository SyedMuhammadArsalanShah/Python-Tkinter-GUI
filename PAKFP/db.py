import sqlite3 as sql
from tkinter import messagebox
def connection_db():
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()

    lostofcard = '''
    CREATE TABLE IF NOT EXISTS LOSTOFCARDINFO (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name TEXT,
        FatherName TEXT,
        CNIC_no TEXT UNIQUE,
        phone_Number TEXT,
        DateofMissing DATETIME DEFAULT CURRENT_TIMESTAMP,
        PNo TEXT UNIQUE,
        CardNo Text
    )
    '''
    lostofvehicle = '''
    CREATE TABLE IF NOT EXISTS LOSTOFVEHICLEINFO (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name TEXT,
        FatherName TEXT,
        CNIC_no TEXT UNIQUE,
        phone_Number TEXT,
        DateofMissing DATETIME DEFAULT CURRENT_TIMESTAMP,
        PNo TEXT ,
        REGISTRATION_NUMBER TEXT
    )
    '''
    blacklistedfirms= '''
        CREATE TABLE IF NOT EXISTS blacklistedfirmsINFO (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Name TEXT,
            FatherName TEXT,
            CNIC_no TEXT UNIQUE,
            phone_Number TEXT,
            firm_Name TEXT,
            PNo TEXT 
        )
        '''
    blacklistedpersonnel='''
        CREATE TABLE IF NOT EXISTS blacklistedpersonnelinfo(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Name TEXT,
            FatherName TEXT,
            CNIC_no TEXT UNIQUE,
            phone_Number TEXT,
            DateofBlacklist DATETIME DEFAULT CURRENT_TIMESTAMP,
            PNo TEXT, 
            reasonofblacklist Text
        )
        '''
    cursor.execute(lostofcard)
    cursor.execute(lostofvehicle)
    cursor.execute(blacklistedfirms)
    cursor.execute(blacklistedpersonnel)

    conn.commit()
    conn.close()

def fetchdata(table_name):
    conn= sql.connect("PAK.db")
    cursor=conn.cursor()
    cursor.execute(f"select * from {table_name}")
    showdata= cursor.fetchall()
    conn.close()
    print(showdata)

    return  showdata

# lost of card info insert
def inserttableLOF(Name,FatherName ,CNIC_no ,phone_Number ,DateofMissing , PNo, card):
    conn=sql.connect("PAK.db")
    cursor=conn.cursor()
    cursor.execute('''
    INSERT INTO LOSTOFCARDINFO(Name,FatherName ,CNIC_no ,phone_Number ,DateofMissing , PNo, CardNo) Values(?,?,?,?,?,?,?)
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card))

    conn.commit()
    conn.close()



# lost of card info update
def updatetableLOF(Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card, id):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''

    UPDATE LOSTOFCARDINFO SET Name=?,FatherName=? ,CNIC_no=? ,phone_Number=? ,DateofMissing =?, PNo=?  , CardNo =? WHERE ID = ? 
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card, id))
    conn.commit()
    conn.close()


# lost of vehicle info insert
def inserttableLOV(Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, registration):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO LOSTOFVEHICLEINFO(Name,FatherName ,CNIC_no ,phone_Number ,DateofMissing , PNo, REGISTRATION_NUMBER) Values(?,?,?,?,?,?,?)
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, registration))

    conn.commit()
    conn.close()


# lost of vehicle info  update
def updatetableLOV(Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, registration, id):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''

    UPDATE LOSTOFVEHICLEINFO SET Name=?,FatherName=? ,CNIC_no=? ,phone_Number=? ,DateofMissing =?, PNo=?  , REGISTRATION_NUMBER =? WHERE ID = ? 
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, registration, id))
    conn.commit()
    conn.close()

# Insert method for blacklisted firms
def inserttableBLF(Name, FatherName, CNIC_no, phone_Number, firm_Name, PNo):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO blacklistedfirmsINFO(Name, FatherName, CNIC_no, phone_Number, firm_Name, PNo) VALUES(?, ?, ?, ?, ?, ?)
    ''', (Name, FatherName, CNIC_no, phone_Number, firm_Name, PNo))
    conn.commit()
    conn.close()

# Update method for blacklisted firms
def updatetableBLF(Name, FatherName, CNIC_no, phone_Number, firm_Name, PNo, id):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE blacklistedfirmsINFO SET Name=?, FatherName=?, CNIC_no=?, phone_Number=?, firm_Name=?, PNo=? WHERE ID=?
    ''', (Name, FatherName, CNIC_no, phone_Number, firm_Name, PNo, id))
    conn.commit()
    conn.close()

# Insert method for blacklisted personnel
def inserttableBLP(Name, FatherName, CNIC_no, phone_Number, dateofBlacklist, PNo, reasonofblacklist):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO blacklistedpersonnelinfo(Name, FatherName, CNIC_no, phone_Number,DateofBlacklist, PNo, reasonofblacklist) VALUES(?, ?, ?,? ,?, ?, ?)
    ''', (Name, FatherName, CNIC_no, phone_Number, dateofBlacklist,PNo, reasonofblacklist))
    conn.commit()
    conn.close()

# Update method for blacklisted personnel
def updatetableBLP(Name, FatherName, CNIC_no, phone_Number,dateofBlacklist, PNo, reasonofblacklist, id):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE blacklistedpersonnelinfo SET Name=?, FatherName=?, CNIC_no=?, phone_Number=?,DateofBlacklist=?, PNo=?, reasonofblacklist=? WHERE ID=?
    ''', (Name, FatherName, CNIC_no, phone_Number,dateofBlacklist ,PNo, reasonofblacklist, id))
    conn.commit()
    conn.close()


def deletetable(tablename, id):
    conn=sql.connect("PAK.db")
    cursor=conn.cursor()
    cursor.execute(f"delete from {tablename} where id =? ", (id,))

    conn.commit()
    conn.close()

def id_exists(tblname,cnic, pno):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT CNIC_no , PNo FROM {tblname} WHERE CNIC_No=? or PNo=?", (cnic,pno))
    if cursor.fetchone() is not None:
        messagebox.showerror("error", "CNIC No OR Pno Already exist ")
    conn.close()


connection_db()



