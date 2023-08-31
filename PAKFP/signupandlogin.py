import sqlite3
from PIL import Image as img, ImageTk
import customtkinter
from tkinter import *
from tkinter import messagebox
import welcomesc

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
image = img.open("images/p2.png")

new_width = 200
new_height = 200
resized_image = image.resize((new_width, new_height))  # Corrected usage

photo = ImageTk.PhotoImage(resized_image)

photo_label = Label(image=photo, bg='#333333')

photo_label.pack(pady=10)

splash_label = Label(splash_root, text="Security Information Software ",
                     bg='#333333', fg="white", font=("Times New Roman", 18, "bold"))

splash_label.pack()




def main():
    # Destroy splash window
    splash_root.destroy()
    global app
    app = customtkinter.CTk()
    app._set_appearance_mode("dark")
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
                    app.destroy()
                    welcomesc.dash()
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
                    app.destroy()
                    welcomesc.dash()

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
                                                corner_radius=5, width=100).place(x=350, y=240)

        signuplabel2 = customtkinter.CTkLabel(frame2, font=font3, text="don't have an account ?", text_color="#fff",
                                              bg_color=bg).place(x=350, y=280)

        signup_button2 = customtkinter.CTkButton(frame2, command=switch_to_frame1,
                                                 font=font3, text_color="#fff", text="SignUP", fg_color=fg_color,
                                                 bg_color=bg, hover_color="navy", cursor="hand2", corner_radius=5,
                                                 width=40).place(
            x=520, y=280)

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
                                                corner_radius=5, width=100).place(x=350, y=240)

        loginlabel = customtkinter.CTkLabel(frame1, font=font3, text="Already have an account ?", text_color="#fff",
                                            bg_color=bg).place(x=350, y=280)

        login_button = customtkinter.CTkButton(frame1, command=login, font=font3, text_color="#fff", text="Login",
                                               fg_color=fg_color, bg_color=bg, hover_color="navy", cursor="hand2",
                                               corner_radius=5, width=40).place(x=520, y=280)

    create_frame1()
    app.mainloop()

splash_root.after(3000, main)
splash_root.mainloop()





