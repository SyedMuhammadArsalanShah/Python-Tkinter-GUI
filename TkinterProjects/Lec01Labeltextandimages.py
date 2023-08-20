from tkinter import *
from PIL import Image,ImageTk

pf_root = Tk()

pf_root.geometry("500x500")


pf_root.minsize(300,300)
pf_root.maxsize(800,800)

itext = Label(text="Here Is your Text")
itext.pack()

# only use for  png images
# photo = PhotoImage(file="images/p1.jpg")


#for jpg images

image = Image.open("images/p1.jpg")

photo = ImageTk.PhotoImage(image)

photo_label = Label(image=photo)


photo_label.pack()
pf_root.mainloop()

