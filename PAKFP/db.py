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


def inserttableLOF(Name,FatherName ,CNIC_no ,phone_Number ,DateofMissing , PNo, card):
    conn=sql.connect("PAK.db")
    cursor=conn.cursor()
    cursor.execute('''
    INSERT INTO LOSTOFCARDINFO(Name,FatherName ,CNIC_no ,phone_Number ,DateofMissing , PNo, CardNo) Values(?,?,?,?,?,?,?)
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card))

    conn.commit()
    conn.close()


def updatetableLOF(Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card, id):
    conn = sql.connect("PAK.db")
    cursor = conn.cursor()
    cursor.execute('''

    UPDATE LOSTOFCARDINFO SET Name=?,FatherName=? ,CNIC_no=? ,phone_Number=? ,DateofMissing =?, PNo=?  , CardNo =? WHERE ID = ? 
    ''', (Name, FatherName, CNIC_no, phone_Number, DateofMissing, PNo, card, id))
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



