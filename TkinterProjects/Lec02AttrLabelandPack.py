from tkinter import *



root=Tk()


root.geometry("500x500")

root.minsize(300,300)
root.maxsize(800,800)

root.title("MY GUI")

#important label options
# text => addtext
# bg   => background
# fg   => foreground
# font => sets the font
# 1 font=("comicsansms",20,"bold")
# 2 font="comicsansms 20 bold"
# padx => sets the padding x=axis
# pady => sets the padding y=axis
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE



title_label= Label(
    text='''Syed Muhammad Arsalan Shah\n Tkinter App Testing''',
    bg="teal",
    fg="white",
    padx=50,
    pady=50,
    font="comicsansms 20 bold",
    borderwidth=4,
    relief=SUNKEN)


# IMPORTANT PACK OPTIONS
# ANCHOR => NW, NE, SE,SW
# SIDE   => TOP, BOTTOM, LEFT, RIGHT
# FILL X,Y
# padx
# pady



# title_label.pack(padx=20,pady=20, side=BOTTOM,  anchor="nw", fill=X )
title_label.pack(padx=20,pady=20, side=RIGHT,  anchor="se", fill=Y)



root.mainloop()