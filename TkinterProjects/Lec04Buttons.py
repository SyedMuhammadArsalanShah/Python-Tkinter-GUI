from tkinter import *

def create():
    print("You Can Create")

def read():
    print("You Can Read")

def update():
    print("You Can Update")
def delete():
    print("You Can Delete")

root= Tk()
root.geometry("500x500")

f1 = Frame(root, bg="black", pady=12, height=100 ,width=500)
f1.pack(fill=X , side=TOP)


b1= Button(f1, text="Create" ,bg="blue",fg="white",command=create,pady=20, padx=40)
b1.pack(side=LEFT , padx="20" )

b2= Button(f1, text="Read",bg="green",fg="white",command=read,pady=20, padx=40)
b2.pack(side=LEFT , padx="20")

b3= Button(f1, text="Update",bg="navy",fg="white",command=update,pady=20, padx=40)
b3.pack(side=LEFT , padx="20" )

b4= Button(f1, text="Delete",bg="red",fg="white",command=delete ,pady=20, padx=40)
b4.pack(side=LEFT , padx="20")


root.mainloop()