# Import module
from tkinter import *
from PIL import Image,ImageTk

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("800x350+300+200")
# splash_root.eval('tk::PlaceWindow . center')
splash_root.configure(bg='#333333')

# Hide title bar
splash_root.overrideredirect(True)

# Set Label
splash_label1 = Label(splash_root, text="4th FP BN ", bg='#333333', fg="white", font=("Roboto", 28, "bold"))

splash_label1.pack()

image = Image.open("images/p2.png")

new_width = 200
new_height = 200
resized_image = image.resize((new_width, new_height))  # Corrected usage


photo = ImageTk.PhotoImage(resized_image)

photo_label = Label(image=photo, bg='#333333' )

photo_label.pack(pady=10 )

splash_label = Label(splash_root, text="Security Information Software ", bg='#333333', fg="white", font=("Times New Roman", 18, "bold"))

splash_label.pack()

# Main window function
def main():
    # Destroy splash window
    splash_root.destroy()

    # Execute tkinter
    # root = Tk()
    # # Adjust size
    # root.geometry("400x400")

    # Center the window on the screen
    # root.eval('tk::PlaceWindow . center')
    import tkinter
    from tkinter import messagebox
    from tkinter import ttk

    window = tkinter.Tk()
    window.title("Login form")
    window.geometry('400x440')
    window.configure(bg='#333333')

    def login():
        username = "admin"
        password = "123"
        if username_entry.get() == username and password_entry.get() == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    frame = tkinter.Frame(bg='#333333')

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Login", bg='#333333', fg="navy", font=("Arial", 30))
    username_label = tkinter.Label(
        frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    title_label = tkinter.Label(frame, text="User Role", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    user_combobox = ttk.Combobox(frame, values=["admin","guest"])
    login_button = tkinter.Button(
        frame, text="Login", bg="navy", fg="#FFFFFF", font=("Arial", 16), command=login)

    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=2, column=0)
    username_entry.grid(row=2, column=1, pady=20)
    password_label.grid(row=3, column=0)
    password_entry.grid(row=3, column=1, pady=20)
    title_label.grid(row=1, column=0)
    user_combobox.grid(row=1, column=1, columnspan=3, sticky="news", pady=10)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()






# Set Interval
splash_root.after(3000, main)

# Execute tkinter event loop
splash_root.mainloop()
