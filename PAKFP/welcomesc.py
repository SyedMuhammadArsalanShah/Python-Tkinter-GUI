import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import ScreenFour
import ScreenOne
import ScreenThree
import ScreenTwo
import signupandlogin

def dash():
    global welcomeScreen
    welcomeScreen = customtkinter.CTk()
    welcomeScreen._set_appearance_mode("dark")
    welcomeScreen.title("Welcome Screen")

    welcomeScreen.geometry("750x360")
    welcomeScreen.maxsize(750, 360)
    welcomeScreen.config(bg='#333333')
    bg = '#333333'
    font1 = ("Helvetica", 25, "bold")
    font2 = ("Arial", 17, "bold")

    def selectone():
        welcomeScreen.destroy()
        ScreenOne.appscr()

    def selecttwo():
        welcomeScreen.destroy()
        ScreenTwo.appscr()

    def selectthree():
        welcomeScreen.destroy()
        ScreenThree.appscr()

    def selectfour():
        welcomeScreen.destroy()
        ScreenFour.appscr()

    def order():
        if alignment_var.get() == "1. Loss of card information.":
            selectone()
        elif alignment_var.get() == "2.Loss of vehicle information.":
            selecttwo()
        elif alignment_var.get() == "3.List of black listed firms.":
            selectthree()
        elif alignment_var.get() == "4.list of black listed personnel":
            selectfour()

    var = StringVar()
    lf = LabelFrame(welcomeScreen, text="Select An Option", width=600, height=100, labelanchor="nw",
                    font=('Helvetica 14 bold'), background=bg, foreground="#fff")
    lf.pack(ipadx=50, expand=TRUE, pady=50)

    alignment_var = StringVar()
    alignments = ("1. Loss of card information.", "2.Loss of vehicle information.",
                  "3.List of black listed firms.", "4.list of black listed personnel")

    grid_row = 1
    for alignment in alignments:
        radio = customtkinter.CTkRadioButton(lf, text=alignment, value=alignment, variable=alignment_var,
                                             text_color="#fff")
        radio.grid(column=0, row=grid_row, sticky="w", padx=40, ipady=20)
        grid_row += 1

    customtkinter.CTkButton(lf, text="Submit", command=order, corner_radius=5, bg_color=bg).grid(column=0, pady=20)
    welcomeScreen.mainloop()
