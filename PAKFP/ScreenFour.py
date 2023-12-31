import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import db
import customtkinter
from tkinter import *
from tkcalendar import Calendar, DateEntry
import sqlite3


def appscr():
    appone = customtkinter.CTk()
    appone.title("LIST oF PERSONNEL SCREEN")
    appone.geometry('1000x420')
    appone.config(bg="#333333")
    appone.resizable(False, False)

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
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', width=10, anchor=tk.CENTER)
    tree.column('Name', width=120, anchor=tk.CENTER)
    tree.column('FatherName', width=120, anchor=tk.CENTER)
    tree.column('CNIC_No', width=120, anchor=tk.CENTER)
    tree.column('Phone_Number', width=120, anchor=tk.CENTER)
    tree.column('DateofMissing', width=120, anchor=tk.CENTER)
    tree.column('PNo', width=100, anchor=tk.CENTER)
    tree.column('Reason ', width=130, anchor=tk.CENTER)

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


appscr()
