# This code show what selection option did the user clicked.

from tkinter import *

root = Tk()

def sel():
   selection = "You selected the option " + str(var.get())
   label["text"] = selection
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )

label = Label(root)
label.pack()

root.mainloop()
