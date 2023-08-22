from  tkinter import *

def getvals():
   print(f"{userval.get(),passval.get(),phoneval.get(),paymentmodeval.get(),addressval.get(),checkboxval.get()}")
   with open("records.txt","a") as a:
       a.write(f"{userval.get(),passval.get(),phoneval.get(),paymentmodeval.get(),addressval.get(),checkboxval.get()}")


root = Tk()

root.geometry("500x500")

#Label and grid packing
Label(root, text=" Registration Form").grid(row=0,column=3)
Label(root, text="Username").grid(row=1, column=2 )
Label(root, text="Password").grid(row=2, column=2 )
Label(root, text="Phone").grid(row=3, column=2 )
Label(root, text="PaymentMode").grid(row=4, column=2 )
Label(root, text="Address").grid(row=5, column=2 )

# variables Classes In tkinter
# BooleanVar, IntVar, StringVar, DoubleVar

#variable Classes
userval = StringVar()
passval = StringVar()
phoneval = StringVar()
paymentmodeval = StringVar()
addressval = StringVar()
checkboxval = IntVar()

#entries and grid packing
Entry(root, textvariable=userval).grid(row=1,column=3)
Entry(root, textvariable=passval).grid(row=2,column=3)
Entry(root, textvariable=phoneval).grid(row=3,column=3)
Entry(root, textvariable=paymentmodeval).grid(row=4,column=3)
Entry(root, textvariable=addressval).grid(row=5,column=3)

# check box and its packing
Checkbutton(root,text="You Are Eligible", variable=checkboxval).grid(row=6,column=3)

Button(text="Submit",command=getvals).grid(row=7,column=3)


root.mainloop()