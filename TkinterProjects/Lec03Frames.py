from  tkinter import *


root = Tk()

root.geometry("300x300")


f1 = Frame(root,bg="teal", borderwidth=5)
f1.pack(fill=X , side=TOP)
l1 = Label(f1, text="Welcome to sublime text", font="Helvetica 16 bold", bg="teal",fg= "White", pady=10)
l1.pack()


f2 = Frame(root,bg="blue", borderwidth=3)
f2.pack(fill=Y ,side=LEFT)
l2 = Label(f2, text="Here is your Text", font="Helvetica 16 bold", bg="black",fg= "White", pady=10)
l2.pack()


root.mainloop()
