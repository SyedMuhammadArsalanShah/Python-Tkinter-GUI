from PIL import Image as img, ImageTk
from tkinter import ttk
# import tkinter as tk
from tkinter import messagebox
import customtkinter
from tkinter import *
from tkcalendar import  DateEntry
import sqlite3


# Create object
splash_root = Tk()
# Adjust size
splash_root.geometry("800x350+300+200")
# splash_root.eval('tok::PlaceWindow . center')
splash_root.configure(bg='#333333')
# Hide title bar
splash_root.overrideredirect(True)
# Set Label
splash_label1 = Label(splash_root, text="4th FP BN ", bg='#333333', fg="white", font=("Roboto", 28, "bold"))
splash_label1.pack()
image = img.open("Images/p2.png")
# E:\TkinterApplications\PakNavyFP\Images
new_width = 200
new_height = 200
resized_image = image.resize((new_width, new_height))  # Corrected usage

photo = ImageTk.PhotoImage(resized_image)

photo_label = Label(image=photo, bg='#333333')

photo_label.pack(pady=10)

splash_label = Label(splash_root, text="Security Information Software ",
                     bg='#333333', fg="white", font=("Times New Roman", 18, "bold"))

splash_label.pack()


# Screen One
def appscrOne():
  try:
    welcomeScreen.destroy()
    appone = customtkinter.CTk()
    appone.title("LOST OF CARD SCREEN")
    appone.geometry('1000x420')
    appone.config(bg="#333333")
    # appone.resizable(False, False)

    bg = '#333333'
    font2 = ("Arial", 20, "bold")
    font3 = ("Arial", 13, "bold")

    def add_to_tree():
        lofitbl = db.fetchdata("LOSTOFCARDINFO")
        tree.delete(*tree.get_children())
        for lofi in lofitbl:
            tree.insert('', END, values=lofi)

    # def add_to_tree():
    #         threading.Thread(target=add_to_tree).start()
    def insert():
        name = name_entry.get()
        fathername = fathername_entry.get()
        cnic = cnic_entry.get()
        phoneNum = phoneNum_entry.get()
        date = date_entry.get()
        pno = pno_entry.get()
        card = card_entry.get()
        if not (name and fathername and cnic and phoneNum and date and pno and card):

            messagebox.showerror("Error", "Enter All Fields")

        elif db.id_exists(tblname="LOSTOFCARDINFO", cnic=cnic, pno=pno):
            print("executed")
        else:
            db.inserttableLOF(name, fathername, cnic, phoneNum, date, pno, card)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been inserted")

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            # id_entry.insert(0,row[0])
            name_entry.insert(0, row[1])
            fathername_entry.insert(0, row[2])
            cnic_entry.insert(0, row[3])
            phoneNum_entry.insert(0, row[4])
            date_entry.insert(0, row[5])
            pno_entry.insert(0, row[6])
            card_entry.insert(0, row[7])

        else:
            pass

    def delete():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to delete")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)

            db.deletetable("LOSTOFCARDINFO", id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been Deleted")

    def update():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to Update")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)
            name = name_entry.get()
            fathername = fathername_entry.get()
            cnic = cnic_entry.get()
            phoneNum = phoneNum_entry.get()
            date = date_entry.get()
            pno = pno_entry.get()
            card = card_entry.get()
            db.updatetableLOF(name, fathername, cnic, phoneNum, date, pno, id, card)
            add_to_tree()
            clear()
            messagebox.showinfo("Success!", "Data has been Updated .")

    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
        name_entry.delete(0, END)
        fathername_entry.delete(0, END)
        cnic_entry.delete(0, END)
        phoneNum_entry.delete(0, END)
        date_entry.delete(0, END)
        pno_entry.delete(0, END)
        card_entry.delete(0, END)

    def searchRecord():
        # open database
        conn = sqlite3.connect('PAK.db')
        # checking search text is empty or not
        if SEARCH.get() != "":
            # clearing current display data
            tree.delete(*tree.get_children())

            # select query with where clause

            if search_role.get() == "NAME":
                cursor = conn.execute("SELECT * FROM LOSTOFCARDINFO  WHERE name LIKE ?",
                                  ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "CNIC NO":
                cursor = conn.execute("SELECT * FROM LOSTOFCARDINFO  WHERE CNIC_no LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "P.NO":
                cursor = conn.execute("SELECT * FROM LOSTOFCARDINFO  WHERE PNo LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            else:
                cursor = conn.execute("SELECT * FROM LOSTOFCARDINFO ")
                fetch = cursor.fetchall()
            # loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()

    name_label = customtkinter.CTkLabel(appone, font=font2, text="Name", text_color="#fff", bg_color=bg)
    name_label.place(x=20, y=40)
    name_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="UserName",
                                        placeholder_text_color="#a3a3a3", width=180)
    name_entry.place(x=200, y=40)

    fathername_label = customtkinter.CTkLabel(appone, font=font2, text="Father Name", text_color="#fff", bg_color=bg)
    fathername_label.place(x=20, y=80)
    fathername_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                              border_color="#a3a3a3", border_width=2, placeholder_text="Father Name",
                                              placeholder_text_color="#a3a3a3", width=180)
    fathername_entry.place(x=200, y=80)

    cnic_label = customtkinter.CTkLabel(appone, font=font2, text="CNIC Number", text_color="#fff", bg_color=bg)
    cnic_label.place(x=20, y=120)
    cnic_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="CNIC Number",
                                        placeholder_text_color="#a3a3a3", width=180)
    cnic_entry.place(x=200, y=120)

    phoneNum_label = customtkinter.CTkLabel(appone, font=font2, text="Phone Number", text_color="#fff", bg_color=bg)
    phoneNum_label.place(x=20, y=160)
    phoneNum_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                            border_color="#a3a3a3", border_width=2, placeholder_text="Phone Number",
                                            placeholder_text_color="#a3a3a3", width=180)
    phoneNum_entry.place(x=200, y=160)

    date_label = customtkinter.CTkLabel(appone, font=font2, text="Date of Missing", text_color="#fff", bg_color=bg)
    date_label.place(x=20, y=200)
    date_entry = DateEntry(appone, width=16, font=font2, background=bg, foreground="white", bd=2)
    date_entry.pack(padx=300, anchor="w", side="left")

    pno_label = customtkinter.CTkLabel(appone, font=font2, text="PNo", text_color="#fff", bg_color=bg)
    pno_label.place(x=20, y=240)
    pno_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                       border_color="#a3a3a3", border_width=2, placeholder_text="PNo",
                                       placeholder_text_color="#a3a3a3", width=180)
    pno_entry.place(x=200, y=240)

    card_label = customtkinter.CTkLabel(appone, font=font2, text="Card No.", text_color="#fff", bg_color=bg)
    card_label.place(x=20, y=280)
    card_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="CardNo",
                                        placeholder_text_color="#a3a3a3", width=180)
    card_entry.place(x=200, y=280)

    add_button = customtkinter.CTkButton(appone, command=insert, font=font2, text_color="#fff", text="Add",
                                         fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                         corner_radius=5, width=150)
    add_button.place(x=40, y=320)

    update_button = customtkinter.CTkButton(appone, command=update, font=font2, text_color="#fff", text="update",
                                            fg_color="blue", hover_color="navy", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    update_button.place(x=200, y=320)

    clear_button = customtkinter.CTkButton(appone, command=lambda: clear(True), font=font2, text_color="#fff",
                                           text="Clear",
                                           fg_color="orange", hover_color="purple", bg_color=bg, cursor="hand2",
                                           corner_radius=5, width=150)
    clear_button.place(x=40, y=360)

    delete_button = customtkinter.CTkButton(appone, font=font2, command=delete, text_color="#fff", text="Delete",
                                            fg_color="red", hover_color="brown", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    delete_button.place(x=200, y=360)



    # serach work
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Search By ", text_color="#fff", bg_color=bg)
    name_label.place(x=400, y=40)
    search_role_values = [ "NAME", "CNIC NO", "P.NO", "Show All Records"]
    global search_role
    search_role = customtkinter.CTkComboBox(appone, fg_color=bg, bg_color=bg, text_color="#fff", width=100,
                                          values=search_role_values)
    search_role.place(x=520, y=40)
    global SEARCH
    SEARCH = StringVar()
    search_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="Search Here...",
                                        placeholder_text_color="#a3a3a3",textvariable=SEARCH,  width=180)
    search_entry.place(x=640, y=40)

    search_button = customtkinter.CTkButton(appone, command=searchRecord, font=font2, text_color="#fff", text="Search",
                                         fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                         corner_radius=5)
    search_button.place(x=830, y=40)
    style = ttk.Style(appone)
    style.theme_use('clam')
    style.configure('Treeview', font=font3, foreground="#fff", background=bg, fieldbackground="#313837")
    style.map('Treeview', background=[('selected', "#1A8f2d")])
    tree = ttk.Treeview(appone, height=20)

    tree['columns'] = ('ID', 'Name', 'FatherName', 'CNIC_No', 'Phone_Number', 'DateofMissing', 'PNo', 'CardNo')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ID', width=10, anchor=CENTER)
    tree.column('Name', width=120, anchor=CENTER)
    tree.column('FatherName', width=120, anchor=CENTER)
    tree.column('CNIC_No', width=120, anchor=CENTER)
    tree.column('Phone_Number', width=120, anchor=CENTER)
    tree.column('DateofMissing', width=120, anchor=CENTER)
    tree.column('PNo', width=100, anchor=CENTER)
    tree.column('CardNo', width=100, anchor=CENTER)

    tree.heading('ID', text="Id")
    tree.heading('Name', text="name")
    tree.heading('FatherName', text="FatherName")
    tree.heading('CNIC_No', text="CNIC_No")
    tree.heading('Phone_Number', text="Phone_Number")
    tree.heading('DateofMissing', text="DateofMissing")
    tree.heading('PNo', text="PNo")
    tree.heading('CardNo', text="CardNo")
    tree.place(x=590, y=120)

    tree.bind('<ButtonRelease>', display_data)
    add_to_tree()
    appone.mainloop()
  except:
      print("ERROR")

# Screen Two
def appscrTwo():
  try:
    welcomeScreen.destroy()
    appone = customtkinter.CTk()
    appone.title("LOST OF VEHICLE SCREEN")
    appone.geometry('1000x420')
    appone.config(bg="#333333")
    # appone.resizable(False, False)

    bg = '#333333'
    font2 = ("Arial", 20, "bold")
    font3 = ("Arial", 13, "bold")

    def add_to_tree():
        lofitbl = db.fetchdata("LOSTOFVEHICLEINFO")
        tree.delete(*tree.get_children())
        for lofi in lofitbl:
            tree.insert('', END, values=lofi)

    def insert():
        name = name_entry.get()
        fathername = fathername_entry.get()
        cnic = cnic_entry.get()
        phoneNum = phoneNum_entry.get()
        date = date_entry.get()
        pno = pno_entry.get()
        registration = registration_entry.get()
        if not (name and fathername and cnic and phoneNum and date and pno and registration):

            messagebox.showerror("Error", "Enter All Fields")

        elif db.id_exists(tblname="LOSTOFVEHICLEINFO", cnic=cnic, pno=pno):
            print("executed")
        else:
            db.inserttableLOV(name, fathername, cnic, phoneNum, date, pno, registration)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been inserted")

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            # id_entry.insert(0,row[0])
            name_entry.insert(0, row[1])
            fathername_entry.insert(0, row[2])
            cnic_entry.insert(0, row[3])
            phoneNum_entry.insert(0, row[4])
            date_entry.insert(0, row[5])
            pno_entry.insert(0, row[6])
            registration_entry.insert(0, row[7])

        else:
            pass

    def delete():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to delete")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)

            db.deletetable("LOSTOFVEHICLEINFO", id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been Deleted")

    def update():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Entity to Update")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)
            name = name_entry.get()
            fathername = fathername_entry.get()
            cnic = cnic_entry.get()
            phoneNum = phoneNum_entry.get()
            date = date_entry.get()
            pno = pno_entry.get()
            registration = registration_entry.get()
            db.updatetableLOV(name, fathername, cnic, phoneNum, date, pno, id, registration)
            add_to_tree()
            clear()
            messagebox.showinfo("Success!", "Data has been Updated .")

    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
        name_entry.delete(0, END)
        fathername_entry.delete(0, END)
        cnic_entry.delete(0, END)
        phoneNum_entry.delete(0, END)
        date_entry.delete(0, END)
        pno_entry.delete(0, END)
        registration_entry.delete(0, END)


    def searchRecord():
        # open database
        conn = sqlite3.connect('PAK.db')
        # checking search text is empty or not
        if SEARCH.get() != "":
            # clearing current display data
            tree.delete(*tree.get_children())

            # select query with where clause

            if search_role.get() == "NAME":
                cursor = conn.execute("SELECT * FROM LOSTOFVEHICLEINFO  WHERE name LIKE ?",
                                  ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "CNIC NO":
                cursor = conn.execute("SELECT * FROM LOSTOFVEHICLEINFO  WHERE CNIC_no LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "P.NO":
                cursor = conn.execute("SELECT * FROM LOSTOFVEHICLEINFO  WHERE PNo LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "VEHICLE REGISTRATION_N0":
                cursor = conn.execute("SELECT * FROM LOSTOFVEHICLEINFO  WHERE REGISTRATION_NUMBER LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            else:
                cursor = conn.execute("SELECT * FROM LOSTOFVEHICLEINFO ")
                fetch = cursor.fetchall()
            # loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()

    name_label = customtkinter.CTkLabel(appone, font=font2, text="Name", text_color="#fff", bg_color=bg)
    name_label.place(x=20, y=40)
    name_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="UserName",
                                        placeholder_text_color="#a3a3a3", width=180)
    name_entry.place(x=200, y=40)

    fathername_label = customtkinter.CTkLabel(appone, font=font2, text="Father Name", text_color="#fff", bg_color=bg)
    fathername_label.place(x=20, y=80)
    fathername_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                              border_color="#a3a3a3", border_width=2, placeholder_text="Father Name",
                                              placeholder_text_color="#a3a3a3", width=180)
    fathername_entry.place(x=200, y=80)

    cnic_label = customtkinter.CTkLabel(appone, font=font2, text="CNIC Number", text_color="#fff", bg_color=bg)
    cnic_label.place(x=20, y=120)
    cnic_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="CNIC Number",
                                        placeholder_text_color="#a3a3a3", width=180)
    cnic_entry.place(x=200, y=120)

    phoneNum_label = customtkinter.CTkLabel(appone, font=font2, text="Phone Number", text_color="#fff", bg_color=bg)
    phoneNum_label.place(x=20, y=160)
    phoneNum_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                            border_color="#a3a3a3", border_width=2, placeholder_text="Phone Number",
                                            placeholder_text_color="#a3a3a3", width=180)
    phoneNum_entry.place(x=200, y=160)

    date_label = customtkinter.CTkLabel(appone, font=font2, text="Date of Missing", text_color="#fff", bg_color=bg)
    date_label.place(x=20, y=200)
    date_entry = DateEntry(appone, width=16, font=font2, background=bg, foreground="white", bd=2)
    date_entry.pack(padx=300, anchor="w", side="left")

    pno_label = customtkinter.CTkLabel(appone, font=font2, text="PNo", text_color="#fff", bg_color=bg)
    pno_label.place(x=20, y=240)
    pno_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                       border_color="#a3a3a3", border_width=2, placeholder_text="PNo",
                                       placeholder_text_color="#a3a3a3", width=180)
    pno_entry.place(x=200, y=240)

    registration_label = customtkinter.CTkLabel(appone, font=font2, text="registration No.", text_color="#fff", bg_color=bg)
    registration_label.place(x=20, y=280)
    registration_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="registrationNo",
                                        placeholder_text_color="#a3a3a3", width=180)
    registration_entry.place(x=200, y=280)

    add_button = customtkinter.CTkButton(appone, command=insert, font=font2, text_color="#fff", text="Add",
                                         fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                         corner_radius=5, width=150)
    add_button.place(x=40, y=320)

    update_button = customtkinter.CTkButton(appone, command=update, font=font2, text_color="#fff", text="update",
                                            fg_color="blue", hover_color="navy", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    update_button.place(x=200, y=320)

    clear_button = customtkinter.CTkButton(appone, command=lambda: clear(True), font=font2, text_color="#fff",
                                           text="Clear",
                                           fg_color="orange", hover_color="purple", bg_color=bg, cursor="hand2",
                                           corner_radius=5, width=150)
    clear_button.place(x=40, y=360)

    delete_button = customtkinter.CTkButton(appone, font=font2, command=delete, text_color="#fff", text="Delete",
                                            fg_color="red", hover_color="brown", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    delete_button.place(x=200, y=360)

    # serach work
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Search By ", text_color="#fff", bg_color=bg)
    name_label.place(x=400, y=40)
    search_role_values = ["NAME", "CNIC NO", "P.NO", "VEHICLE REGISTRATION_N0"]
    global search_role
    search_role = customtkinter.CTkComboBox(appone, fg_color=bg, bg_color=bg, text_color="#fff", width=100,
                                            values=search_role_values)
    search_role.place(x=520, y=40)
    global SEARCH
    SEARCH = StringVar()
    search_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                          border_color="#a3a3a3", border_width=2, placeholder_text="Search Here...",
                                          placeholder_text_color="#a3a3a3", textvariable=SEARCH, width=180)
    search_entry.place(x=640, y=40)

    search_button = customtkinter.CTkButton(appone, command=searchRecord, font=font2, text_color="#fff", text="Search",
                                            fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                            corner_radius=5)
    search_button.place(x=830, y=40)

    style = ttk.Style(appone)
    style.theme_use('clam')
    style.configure('Treeview', font=font3, foreground="#fff", background=bg, fieldbackground="#313837")
    style.map('Treeview', background=[('selected', "#1A8f2d")])
    tree = ttk.Treeview(appone, height=20)

    tree['columns'] = ('ID', 'Name', 'FatherName', 'CNIC_No', 'Phone_Number', 'DateofMissing', 'PNo', 'registration')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ID', width=10, anchor=CENTER)
    tree.column('Name', width=120, anchor=CENTER)
    tree.column('FatherName', width=120, anchor=CENTER)
    tree.column('CNIC_No', width=120, anchor=CENTER)
    tree.column('Phone_Number', width=120, anchor=CENTER)
    tree.column('DateofMissing', width=120, anchor=CENTER)
    tree.column('PNo', width=100, anchor=CENTER)
    tree.column('registration', width=100, anchor=CENTER)

    tree.heading('ID', text="Id")
    tree.heading('Name', text="name")
    tree.heading('FatherName', text="FatherName")
    tree.heading('CNIC_No', text="CNIC_No")
    tree.heading('Phone_Number', text="Phone_Number")
    tree.heading('DateofMissing', text="DateofMissing")
    tree.heading('PNo', text="PNo")
    tree.heading('registration', text="Registration No")
    tree.place(x=590, y=120)

    tree.bind('<ButtonRelease>', display_data)
    add_to_tree()
    appone.mainloop()
  except:
      print("ERROR")

# Screen Three

def appscrThree():
  try:
    welcomeScreen.destroy()
    appone = customtkinter.CTk()
    appone.title("BLACK LISTED FIRMS SCREEN")
    appone.geometry('1000x420')
    appone.config(bg="#333333")
    # appone.resizable(False, False)

    bg = '#333333'
    font2 = ("Arial", 20, "bold")
    font3 = ("Arial", 13, "bold")

    def add_to_tree():
        blfitbl = db.fetchdata("blacklistedfirmsINFO")
        tree.delete(*tree.get_children())
        for blfi in blfitbl:
            tree.insert('', END, values=blfi)

    def insert():
        name = name_entry.get()
        fathername = fathername_entry.get()
        cnic = cnic_entry.get()
        phoneNum = phoneNum_entry.get()
        firm_name = firm_name_entry.get()
        pno = pno_entry.get()

        if not (name and fathername and cnic and phoneNum and firm_name and pno):
            messagebox.showerror("Error", "Enter All Fields")
        elif db.id_exists(tblname="blacklistedfirmsINFO", cnic=cnic, pno=pno):
            print("executed")
        else:
            db.inserttableBLF(name, fathername, cnic, phoneNum, firm_name, pno)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been inserted")

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            # id_entry.insert(0,row[0])
            name_entry.insert(0, row[1])
            fathername_entry.insert(0, row[2])
            cnic_entry.insert(0, row[3])
            phoneNum_entry.insert(0, row[4])
            firm_name_entry.insert(0, row[5])
            pno_entry.insert(0, row[6])


        else:
            pass

    def delete():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to delete")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)

            db.deletetable("blacklistedfirmsINFO", id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been Deleted")

    def update():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose a Firm to Update")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            name = name_entry.get()
            fathername = fathername_entry.get()
            cnic = cnic_entry.get()
            phoneNum = phoneNum_entry.get()
            firm_name = firm_name_entry.get()
            pno = pno_entry.get()

            db.updatetableBLF(name, fathername, cnic, phoneNum, firm_name, pno, id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success!", "Data has been Updated.")

    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
        name_entry.delete(0, END)
        fathername_entry.delete(0, END)
        cnic_entry.delete(0, END)
        phoneNum_entry.delete(0, END)

        pno_entry.delete(0, END)
        firm_name_entry.delete(0, END)
    def searchRecord():
        # open database
        conn = sqlite3.connect('PAK.db')
        # checking search text is empty or not
        if SEARCH.get() != "":
            # clearing current display data
            tree.delete(*tree.get_children())

            # select query with where clause

            if search_role.get() == "NAME":
                cursor = conn.execute("SELECT * FROM blacklistedfirmsINFO  WHERE name LIKE ?",
                                  ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "CNIC NO":
                cursor = conn.execute("SELECT * FROM blacklistedfirmsINFO  WHERE CNIC_no LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "P.NO":
                cursor = conn.execute("SELECT * FROM blacklistedfirmsINFO  WHERE PNo LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "Firm Name":
                cursor = conn.execute("SELECT * FROM blacklistedfirmsINFO  WHERE firm_Name LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            else:
                cursor = conn.execute("SELECT * FROM blacklistedfirmsINFO ")
                fetch = cursor.fetchall()
            # loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Name", text_color="#fff", bg_color=bg)
    name_label.place(x=20, y=40)
    name_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="UserName",
                                        placeholder_text_color="#a3a3a3", width=180)
    name_entry.place(x=200, y=40)

    fathername_label = customtkinter.CTkLabel(appone, font=font2, text="Father Name", text_color="#fff", bg_color=bg)
    fathername_label.place(x=20, y=80)
    fathername_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                              border_color="#a3a3a3", border_width=2, placeholder_text="Father Name",
                                              placeholder_text_color="#a3a3a3", width=180)
    fathername_entry.place(x=200, y=80)

    cnic_label = customtkinter.CTkLabel(appone, font=font2, text="CNIC Number", text_color="#fff", bg_color=bg)
    cnic_label.place(x=20, y=120)
    cnic_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="CNIC Number",
                                        placeholder_text_color="#a3a3a3", width=180)
    cnic_entry.place(x=200, y=120)

    phoneNum_label = customtkinter.CTkLabel(appone, font=font2, text="Phone Number", text_color="#fff", bg_color=bg)
    phoneNum_label.place(x=20, y=160)
    phoneNum_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                            border_color="#a3a3a3", border_width=2, placeholder_text="Phone Number",
                                            placeholder_text_color="#a3a3a3", width=180)
    phoneNum_entry.place(x=200, y=160)

    # date_label = customtkinter.CTkLabel(appone, font=font2, text="Date of Missing", text_color="#fff", bg_color=bg)
    # date_label.place(x=20, y=200)
    # date_entry = DateEntry(appone, width=16, font=font2, background=bg, foreground="white", bd=2)
    # date_entry.pack(padx=300, anchor="w", side="left")

    pno_label = customtkinter.CTkLabel(appone, font=font2, text="PNo", text_color="#fff", bg_color=bg)
    pno_label.place(x=20, y=240)
    pno_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                       border_color="#a3a3a3", border_width=2, placeholder_text="PNo",
                                       placeholder_text_color="#a3a3a3", width=180)
    pno_entry.place(x=200, y=240)

    firm_name_label = customtkinter.CTkLabel(appone, font=font2, text="Firm Name", text_color="#fff", bg_color=bg)
    firm_name_label.place(x=20, y=200)
    firm_name_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                             border_color="#a3a3a3", border_width=2, placeholder_text="Firm Name",
                                             placeholder_text_color="#a3a3a3", width=180)
    firm_name_entry.place(x=200, y=200)
    add_button = customtkinter.CTkButton(appone, command=insert, font=font2, text_color="#fff", text="Add",
                                         fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                         corner_radius=5, width=150)
    add_button.place(x=40, y=320)

    update_button = customtkinter.CTkButton(appone, command=update, font=font2, text_color="#fff", text="update",
                                            fg_color="blue", hover_color="navy", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    update_button.place(x=200, y=320)

    clear_button = customtkinter.CTkButton(appone, command=lambda: clear(True), font=font2, text_color="#fff",
                                           text="Clear",
                                           fg_color="orange", hover_color="purple", bg_color=bg, cursor="hand2",
                                           corner_radius=5, width=150)
    clear_button.place(x=40, y=360)

    delete_button = customtkinter.CTkButton(appone, font=font2, command=delete, text_color="#fff", text="Delete",
                                            fg_color="red", hover_color="brown", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    delete_button.place(x=200, y=360)
    # serach work
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Search By ", text_color="#fff", bg_color=bg)
    name_label.place(x=400, y=40)
    search_role_values = ["NAME", "CNIC NO", "P.NO", "Firm Name"]
    global search_role
    search_role = customtkinter.CTkComboBox(appone, fg_color=bg, bg_color=bg, text_color="#fff", width=100,
                                            values=search_role_values)
    search_role.place(x=520, y=40)
    global SEARCH
    SEARCH = StringVar()
    search_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                          border_color="#a3a3a3", border_width=2, placeholder_text="Search Here...",
                                          placeholder_text_color="#a3a3a3", textvariable=SEARCH, width=180)
    search_entry.place(x=640, y=40)

    search_button = customtkinter.CTkButton(appone, command=searchRecord, font=font2, text_color="#fff", text="Search",
                                            fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                            corner_radius=5)
    search_button.place(x=830, y=40)
    style = ttk.Style(appone)
    style.theme_use('clam')
    style.configure('Treeview', font=font3, foreground="#fff", background=bg, fieldbackground="#313837")
    style.map('Treeview', background=[('selected', "#1A8f2d")])
    tree = ttk.Treeview(appone, height=20)

    tree['columns'] = ('ID', 'Name', 'FatherName', 'CNIC_No', 'Phone_Number', 'Firm_Name', 'PNo')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ID', width=10, anchor=CENTER)
    tree.column('Name', width=120, anchor=CENTER)
    tree.column('FatherName', width=120, anchor=CENTER)
    tree.column('CNIC_No', width=120, anchor=CENTER)
    tree.column('Phone_Number', width=120, anchor=CENTER)
    tree.column('Firm_Name', width=150, anchor=CENTER)
    tree.column('PNo', width=100, anchor=CENTER)

    tree.heading('ID', text="Id")
    tree.heading('Name', text="Name")
    tree.heading('FatherName', text="Father Name")
    tree.heading('CNIC_No', text="CNIC No")
    tree.heading('Phone_Number', text="Phone Number")
    tree.heading('Firm_Name', text="Firm Name")
    tree.heading('PNo', text="PNo")
    tree.place(x=590, y=120)

    tree.bind('<ButtonRelease>', display_data)
    add_to_tree()
    appone.mainloop()
  except:
      print("ERROR")


def appscrFour():
    welcomeScreen.destroy()
    appone = customtkinter.CTk()
    appone.title("LIST oF PERSONNEL SCREEN")
    appone.geometry('1000x420')
    appone.config(bg="#333333")
    # appone.resizable(False, False)

    bg = '#333333'
    font2 = ("Arial", 20, "bold")
    font3 = ("Arial", 13, "bold")

    def add_to_tree():
        lofitbl = db.fetchdata("blacklistedpersonnelinfo")
        tree.delete(*tree.get_children())
        for lofi in lofitbl:
            tree.insert('', END, values=lofi)

    def insert():
        name = name_entry.get()
        fathername = fathername_entry.get()
        cnic = cnic_entry.get()
        phoneNum = phoneNum_entry.get()
        date = date_entry.get()
        pno = pno_entry.get()
        reason =reason_entry.get()
        if not (name and fathername and cnic and phoneNum and date and pno and reason):

            messagebox.showerror("Error", "Enter All Fields")

        elif db.id_exists(tblname="blacklistedpersonnelinfo", cnic=cnic, pno=pno):
            print("executed")
        else:
            db.inserttableBLP(name, fathername, cnic, phoneNum, date, pno, reason)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been inserted")

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            # id_entry.insert(0,row[0])
            name_entry.insert(0, row[1])
            fathername_entry.insert(0, row[2])
            cnic_entry.insert(0, row[3])
            phoneNum_entry.insert(0, row[4])
            date_entry.insert(0, row[5])
            pno_entry.insert(0, row[6])
            reason_entry.insert(0, row[7])

        else:
            pass

    def delete():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to delete")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)

            db.deletetable("blacklistedpersonnelinfo", id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success", "Data has been Deleted")

    def update():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose an Employee to Update")
        else:
            id = tree.item(selected_item, "values")[0]  # Get the value of the first column
            print("First Column Value:", id)
            name = name_entry.get()
            fathername = fathername_entry.get()
            cnic = cnic_entry.get()
            phoneNum = phoneNum_entry.get()
            date = date_entry.get()
            pno = pno_entry.get()
            reason = reason_entry.get()
            db.updatetableBLP(name, fathername, cnic, phoneNum, date, pno, reason,id)
            add_to_tree()
            clear()
            messagebox.showinfo("Success!", "Data has been Updated .")

    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
        name_entry.delete(0, END)
        fathername_entry.delete(0, END)
        cnic_entry.delete(0, END)
        phoneNum_entry.delete(0, END)
        date_entry.delete(0, END)
        pno_entry.delete(0, END)
        reason_entry.delete(0, END)

    def searchRecord():
        # open database
        conn = sqlite3.connect('PAK.db')
        # checking search text is empty or not
        if SEARCH.get() != "":
            # clearing current display data
            tree.delete(*tree.get_children())

            # select query with where clause

            if search_role.get() == "NAME":
                cursor = conn.execute("SELECT * FROM blacklistedpersonnelinfo  WHERE name LIKE ?",
                                  ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "CNIC NO":
                cursor = conn.execute("SELECT * FROM blacklistedpersonnelinfo  WHERE CNIC_no LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            elif search_role.get() == "P.NO":
                cursor = conn.execute("SELECT * FROM blacklistedpersonnelinfo  WHERE PNo LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
            else:
                cursor = conn.execute("SELECT * FROM blacklistedpersonnelinfo ")
                fetch = cursor.fetchall()
            # loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=data)
                cursor.close()
                conn.close()
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Name", text_color="#fff", bg_color=bg)
    name_label.place(x=20, y=40)
    name_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="UserName",
                                        placeholder_text_color="#a3a3a3", width=180)
    name_entry.place(x=200, y=40)

    fathername_label = customtkinter.CTkLabel(appone, font=font2, text="Father Name", text_color="#fff", bg_color=bg)
    fathername_label.place(x=20, y=80)
    fathername_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                              border_color="#a3a3a3", border_width=2, placeholder_text="Father Name",
                                              placeholder_text_color="#a3a3a3", width=180)
    fathername_entry.place(x=200, y=80)

    cnic_label = customtkinter.CTkLabel(appone, font=font2, text="CNIC Number", text_color="#fff", bg_color=bg)
    cnic_label.place(x=20, y=120)
    cnic_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="CNIC Number",
                                        placeholder_text_color="#a3a3a3", width=180)
    cnic_entry.place(x=200, y=120)

    phoneNum_label = customtkinter.CTkLabel(appone, font=font2, text="Phone Number", text_color="#fff", bg_color=bg)
    phoneNum_label.place(x=20, y=160)
    phoneNum_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                            border_color="#a3a3a3", border_width=2, placeholder_text="Phone Number",
                                            placeholder_text_color="#a3a3a3", width=180)
    phoneNum_entry.place(x=200, y=160)

    date_label = customtkinter.CTkLabel(appone, font=font2, text="Date of Missing", text_color="#fff", bg_color=bg)
    date_label.place(x=20, y=200)
    date_entry = DateEntry(appone, width=16, font=font2, background=bg, foreground="white", bd=2)
    date_entry.pack(padx=300, anchor="w", side="left")

    pno_label = customtkinter.CTkLabel(appone, font=font2, text="PNo", text_color="#fff", bg_color=bg)
    pno_label.place(x=20, y=240)
    pno_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                       border_color="#a3a3a3", border_width=2, placeholder_text="PNo",
                                       placeholder_text_color="#a3a3a3", width=180)
    pno_entry.place(x=200, y=240)

    reason_label = customtkinter.CTkLabel(appone, font=font2, text="reason No.", text_color="#fff", bg_color=bg)
    reason_label.place(x=20, y=280)
    reason_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                        border_color="#a3a3a3", border_width=2, placeholder_text="Reason ",
                                        placeholder_text_color="#a3a3a3", width=180)
    reason_entry.place(x=200, y=280)

    add_button = customtkinter.CTkButton(appone, command=insert, font=font2, text_color="#fff", text="Add",
                                         fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                         corner_radius=5, width=150)
    add_button.place(x=40, y=320)

    update_button = customtkinter.CTkButton(appone, command=update, font=font2, text_color="#fff", text="update",
                                            fg_color="blue", hover_color="navy", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    update_button.place(x=200, y=320)

    clear_button = customtkinter.CTkButton(appone, command=lambda: clear(True), font=font2, text_color="#fff",
                                           text="Clear",
                                           fg_color="orange", hover_color="purple", bg_color=bg, cursor="hand2",
                                           corner_radius=5, width=150)
    clear_button.place(x=40, y=360)

    delete_button = customtkinter.CTkButton(appone, font=font2, command=delete, text_color="#fff", text="Delete",
                                            fg_color="red", hover_color="brown", bg_color=bg, cursor="hand2",
                                            corner_radius=5, width=150)
    delete_button.place(x=200, y=360)
    # serach work
    name_label = customtkinter.CTkLabel(appone, font=font2, text="Search By ", text_color="#fff", bg_color=bg)
    name_label.place(x=400, y=40)
    search_role_values = ["NAME", "CNIC NO", "P.NO", "Show All Records"]
    global search_role
    search_role = customtkinter.CTkComboBox(appone, fg_color=bg, bg_color=bg, text_color="#fff", width=100,
                                            values=search_role_values)
    search_role.place(x=520, y=40)
    global SEARCH
    SEARCH = StringVar()
    search_entry = customtkinter.CTkEntry(appone, font=font2, text_color="#000", fg_color="#fff", bg_color=bg,
                                          border_color="#a3a3a3", border_width=2, placeholder_text="Search Here...",
                                          placeholder_text_color="#a3a3a3", textvariable=SEARCH, width=180)
    search_entry.place(x=640, y=40)

    search_button = customtkinter.CTkButton(appone, command=searchRecord, font=font2, text_color="#fff", text="Search",
                                            fg_color="teal", hover_color="green", bg_color=bg, cursor="hand2",
                                            corner_radius=5)
    search_button.place(x=830, y=40)
    style = ttk.Style(appone)
    style.theme_use('clam')
    style.configure('Treeview', font=font3, foreground="#fff", background=bg, fieldbackground="#313837")
    style.map('Treeview', background=[('selected', "#1A8f2d")])
    tree = ttk.Treeview(appone, height=20 )

    tree['columns'] = ('ID', 'Name', 'FatherName', 'CNIC_No', 'Phone_Number', 'DateofMissing', 'PNo', 'Reason ')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ID', width=10, anchor=CENTER)
    tree.column('Name', width=120, anchor=CENTER)
    tree.column('FatherName', width=120, anchor=CENTER)
    tree.column('CNIC_No', width=120, anchor=CENTER)
    tree.column('Phone_Number', width=120, anchor=CENTER)
    tree.column('DateofMissing', width=120, anchor=CENTER)
    tree.column('PNo', width=100, anchor=CENTER)
    tree.column('Reason ', width=130, anchor=CENTER)

    tree.heading('ID', text="Id")
    tree.heading('Name', text="name")
    tree.heading('FatherName', text="FatherName")
    tree.heading('CNIC_No', text="CNIC_No")
    tree.heading('Phone_Number', text="Phone_Number")
    tree.heading('DateofMissing', text="DateofMissing")
    tree.heading('PNo', text="PNo")
    tree.heading('Reason ', text="Reason ")
    tree.place(x=590, y=120)

    tree.bind('<ButtonRelease>', display_data)
    add_to_tree()
    appone.mainloop()






def dash():
  try:
    app.destroy()
    global welcomeScreen
    welcomeScreen = customtkinter.CTk()
    # welcomeScreen._set_appearance_mode("dark")
    welcomeScreen.title("Welcome Screen")

    welcomeScreen.geometry("750x360")
    welcomeScreen.maxsize(750, 360)
    welcomeScreen.config(bg='#333333')
    bg = '#333333'
    font1 = ("Helvetica", 25, "bold")
    font2 = ("Arial", 17, "bold")


    def order():
        print("----", alignment_var.get())
        if alignment_var.get() == "1. Loss of card information.":
            appscrOne()
        elif alignment_var.get() == "2.Loss of vehicle information.":
            appscrTwo()
        elif alignment_var.get() == "3.List of black listed firms.":
            appscrThree()
        elif alignment_var.get() == "4.list of black listed personnel":
            appscrFour()


    lf = LabelFrame(welcomeScreen, text="Select An Option", width=600, height=100, labelanchor="nw",
                    font=('Helvetica 14 bold'), background=bg, foreground="#fff")
    lf.pack(ipadx=50, expand=TRUE, pady=50)

    alignment_var = StringVar()
    alignments = ("1. Loss of card information.", "2.Loss of vehicle information.",
                  "3.List of black listed firms.", "4.list of black listed personnel")

    grid_row = 1
    for alignment in alignments:
        radio = customtkinter.CTkRadioButton(lf, text=alignment, value=alignment, command=order, variable=alignment_var,
                                             text_color="#fff")
        radio.grid(column=0, row=grid_row, sticky="w", padx=40, ipady=20)
        grid_row += 1

    # customtkinter.CTkButton(lf, text="Submit", command=order, corner_radius=5, bg_color=bg).grid(column=0, pady=20)
    welcomeScreen.mainloop()
  except :
       print("ERROR in welcome")
def main():
  try:
    # Destroy splash window
    splash_root.destroy()
    global app
    app = customtkinter.CTk()
    # app._set_appearance_mode("dark")
    app.title("Login")

    app.geometry("750x360")

    app.maxsize(750, 360)
    app.config(bg='#333333')



    font1 = ("Helvetica", 25, "bold")
    font2 = ("Arial", 17, "bold")
    font3 = ("Arial", 13, "bold")
    font4 = ("Arial", 13, "bold", "underline")

    bg = '#333333'

    fg_color = '#001a2e'

    # create database

    conn = sqlite3.connect("PAK.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user ( username TEXT NOT NULL , password TEXT NOT NULL , user_category)
    """)


    def signup():

        username = username_entry.get()
        password = password_entry.get()
        userrole = user_role.get()

        if username != '' and password != '' and userrole != '':
            cursor.execute("SELECT username FROM USER WHERE username=?", [username])
            if cursor.fetchone() is not None:
                messagebox.showerror("error", "username already exist ")
            else:
                cursor.execute("INSERT INTO USER VALUES (?,?,?)", [username, password, userrole])
                conn.commit()
                messagebox.showinfo("Success!", "Account has been created")
                if(userrole == "ADMIN"):

                    messagebox.showinfo("Admin Account ", "Welcome to Admin Account")

                    dash()
                else:
                    messagebox.showinfo("Guest Account ", "Coming Soon InshaAllah....")

        else:
            messagebox.showerror("Error! ", "Enter All Fields")

    def loginaccount():
        username = username_entry2.get()
        password = password_entry2.get()
        userrole = user_role2.get()

        if username != '' and password != '' and userrole != '':
            cursor.execute("SELECT * FROM USER WHERE username=? and password =? and user_category=?",
                           [username, password, userrole])
            if cursor.fetchone():
                messagebox.showinfo("Success!", "Account has been Login")

                if(userrole == "ADMIN"):


                    messagebox.showinfo("Admin Account ", "Welcome to Admin Account")
                    dash()


                else:
                    messagebox.showinfo("Guest Account ", "Coming Soon InshaAllah....")


            else:
                messagebox.showerror("Error", "username or password is invalid  ")
        else:
            messagebox.showerror("Error! ", "Enter All Fields")

    def login():
        global frame2
        frame1.destroy()
        frame2 = customtkinter.CTkFrame(app, bg_color=bg, fg_color=bg, width=750, height=360)
        frame2.place(x=0, y=0)
        image1 = PhotoImage(file="images/p2.png")
        Label(frame2, image=image1, bg=bg).place(x=0, y=0)
        frame2.image1 = image1

        login_label = customtkinter.CTkLabel(frame2, font=font1, text="Login", text_color="#fff",
                                             bg_color=bg).place(x=380, y=20)
        global username_entry2
        username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color="#fff", fg_color=bg, bg_color=bg,
                                                 border_color='#fff', border_width=3, placeholder_text="UserName",
                                                 placeholder_text_color="#a3a3a3", width=250, height=50)
        username_entry2.place(x=350, y=80)
        global password_entry2
        password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show="*", text_color="#fff", fg_color=bg,
                                                 bg_color=bg,
                                                 border_color="#fff", border_width=3, placeholder_text="Password",
                                                 placeholder_text_color="#a3a3a3", width=250, height=50)
        password_entry2.place(x=350, y=140)

        user_role_values = ["ADMIN", "GUEST"]
        global user_role2
        user_role2 = customtkinter.CTkComboBox(frame2, fg_color=bg, bg_color=bg, text_color="#fff", width=200,
                                               values=user_role_values)
        user_role2.place(x=350, y=200)
        login_button2 = customtkinter.CTkButton(frame2, command=loginaccount, font=font2, text_color="#fff",
                                                text="Login",
                                                fg_color=fg_color, hover_color="navy", bg_color=bg, cursor="hand2",
                                                corner_radius=5, width=100)
        login_button2.place(x=350, y=240)
        signuplabel2 = customtkinter.CTkLabel(frame2, font=font3, text="don't have an account ?", text_color="#fff",
                                              bg_color=bg).place(x=350, y=280)

        signup_button2 = customtkinter.CTkButton(frame2, command=switch_to_frame1,
                                                 font=font3, text_color="#fff", text="SignUP", fg_color=fg_color,
                                                 bg_color=bg, hover_color="navy", cursor="hand2", corner_radius=5,
                                                 width=40)
        signup_button2.place(x=520, y=280)
    def switch_to_frame1():
        frame2.destroy()  # Destroy frame2
        create_frame1()

    def create_frame1():
        global frame1
        frame1 = customtkinter.CTkFrame(app, bg_color=bg, fg_color=bg, width=750, height=360)
        frame1.place(x=0, y=0)
        image1 = PhotoImage(file="images/p2.png")
        Label(frame1, image=image1, bg=bg).place(x=0, y=0)
        frame1.image1 = image1
        signuplabel = customtkinter.CTkLabel(frame1, font=font1, text="Signup", text_color="#fff",
                                             bg_color=bg).place(x=380, y=20)

        global username_entry
        username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#fff", fg_color=bg, bg_color=bg,
                                                border_color='#fff', border_width=3, placeholder_text="UserName",
                                                placeholder_text_color="#a3a3a3", width=250, height=50)
        username_entry.place(x=350, y=80)
        global password_entry
        password_entry = customtkinter.CTkEntry(frame1, font=font2, show="*", text_color="#fff", fg_color=bg,
                                                bg_color=bg,
                                                border_color="#fff", border_width=3, placeholder_text="Password",
                                                placeholder_text_color="#a3a3a3", width=250, height=50)
        password_entry.place(x=350, y=140)

        user_role_values = ["ADMIN", "GUEST"]
        global user_role
        user_role = customtkinter.CTkComboBox(frame1, fg_color=bg, bg_color=bg, text_color="#fff", width=200,
                                              values=user_role_values)
        user_role.place(x=350, y=200)
        signup_button = customtkinter.CTkButton(frame1, command=signup, font=font2, text_color="#fff", text="SignUp",
                                                fg_color=fg_color, hover_color="navy", bg_color=bg, cursor="hand2",
                                                corner_radius=5, width=100)
        signup_button.place(x=350, y=240)

        loginlabel = customtkinter.CTkLabel(frame1, font=font3, text="Already have an account ?", text_color="#fff",
                                            bg_color=bg).place(x=350, y=280)

        login_button = customtkinter.CTkButton(frame1, command=login, font=font3, text_color="#fff", text="Login",
                                               fg_color=fg_color, bg_color=bg, hover_color="navy", cursor="hand2",
                                               corner_radius=5, width=40)
        login_button.place(x=520, y=280)

    create_frame1()
    app.mainloop()

  except:
      print("ERROR abc")



if __name__ == '__main__':
     import db
     splash_root.after(3000, main)
     splash_root.mainloop()
     import threading


     def my_background_function():
         tkinter.Tk().update()


     thread = threading.Thread(target=my_background_function)
     thread.daemon = True
     thread.start()



