import  customtkinter
import  sqlite3
from tkinter import *
from tkinter import messagebox
# Import module
from PIL import Image, ImageTk

import scrone
import signupandlogin
import db
import sqlite3 as sql
from tkinter import messagebox


def dash():


    welcome = customtkinter.CTk()
    welcome._set_appearance_mode("dark")
    welcome.title("Welcome Screen")

    welcome.geometry("750x360")

    welcome.maxsize(750, 360)
    welcome.config(bg='#333333')
    bg = '#333333'
    font1 = ("Helvetica", 25, "bold")
    font2 = ("Arial", 17, "bold")
    font3 = ("Arial", 13, "bold")
    font4 = ("Arial", 13, "bold", "underline")

    def selectone():
        welcomes1 = customtkinter.CTk()
        welcomes1._set_appearance_mode("dark")
        welcomes1.title("Screen one")

        welcomes1.geometry("750x360")

        # welcomes1.maxsize(750, 360)
        welcomes1.config(bg='#333333')

        global selone
        selone = customtkinter.CTkFrame(welcomes1, bg_color=bg, fg_color=bg)
        selone.place(x=0, y=0)
        signuplabel = customtkinter.CTkLabel(selone, font=font1, text="Search by an Option", text_color="#fff",
                                             bg_color=bg).grid(column=2, row=1, pady=20)

        global username_entry
        username_entry = customtkinter.CTkEntry(selone, font=font2, text_color="#fff", fg_color=bg, bg_color=bg,
                                                border_color='#fff', border_width=3, placeholder_text="Search Here....",
                                                placeholder_text_color="#a3a3a3", width=350, height=50)
        username_entry.grid(column=1, row=2, padx=15)
        alignment_vars = StringVar()
        alignmentss = ("1.Name", "2.Card No", "3.P.No")

        # create radio buttons and place them on the label frame

        grid_col = 2
        for alignment in alignmentss:
            # create a radio button
            radio = customtkinter.CTkRadioButton(selone, text=alignment, value=alignment, variable=alignment_vars,
                                                 text_color="#fff")
            radio.grid(column=grid_col, row=2, ipadx=5)
            # grid column
            grid_col += 1
        customtkinter.CTkButton(selone, text="Search", command=order, corner_radius=5, bg_color=bg).grid(column=5,
                                                                                                         row=2, pady=20)

        welcomes1.mainloop()

    def selecttwo():
        welcomes2 = customtkinter.CTk()
        welcomes2._set_appearance_mode("dark")
        welcomes2.title("Screen two")

        welcomes2.geometry("750x360")

        welcomes2.maxsize(750, 360)
        welcomes2.config(bg='#333333')
        welcomes2.mainloop()

    def selectthree():
        welcomes3 = customtkinter.CTk()
        welcomes3._set_appearance_mode("dark")
        welcomes3.title("Screen three")

        welcomes3.geometry("750x360")

        welcomes3.maxsize(750, 360)
        welcomes3.config(bg='#333333')
        welcomes3.mainloop()

    def selectfour():
        welcomes4 = customtkinter.CTk()
        welcomes4._set_appearance_mode("dark")
        welcomes4.title("Screen four")

        welcomes4.geometry("750x360")

        welcomes4.maxsize(750, 360)
        welcomes4.config(bg='#333333')
        welcomes4.mainloop()

    def order():
        if alignment_var.get() == "1. Loss of card information.":
            print("select 1")
            welcome.destroy()
            scrone.appscr()
        elif alignment_var.get() == "2.Loss of vehicle information.":
            print("select 2")
            welcome.destroy()
            selecttwo()
        elif alignment_var.get() == "3.List of black listed firms.":
            print("select 3")
            welcome.destroy()
            selectthree()
        elif alignment_var.get() == "4.list of black listed personnel":
            print("select 4")
            welcome.destroy()
            selectfour()
        else:
            print("error")

    var = StringVar()
    lf = LabelFrame(welcome, text="Select An Option", width=600, height=100, labelanchor="nw",
                    font=('Helvetica 14 bold'), background=bg, foreground="#fff")
    lf.pack(ipadx=50, expand=TRUE, pady=50, )

    alignment_var = StringVar()
    alignments = ("1. Loss of card information.", "2.Loss of vehicle information.", "3.List of black listed firms.",
                  "4.list of black listed personnel")

    # create radio buttons and place them on the label frame

    grid_row = 1
    for alignment in alignments:
        # create a radio button
        radio = customtkinter.CTkRadioButton(lf, text=alignment, value=alignment, variable=alignment_var,
                                             text_color="#fff")
        radio.grid(column=0, row=grid_row, sticky="w", padx=40, ipady=20)
        # grid column
        grid_row += 1

    customtkinter.CTkButton(lf, text="Submit", command=order, corner_radius=5, bg_color=bg).grid(column=0, pady=20)
    welcome.mainloop()
dash()