# The selected button's color will change depending on what button did the user clicked. 

from tkinter import *

root = Tk()

def sel():
   rb = var.get()
   selection = "You selected the option " + str(rb)
   label["text"] = selection
   if rb == 1:
      label["background"] = "red"
   elif rb == 2:
      label["background"] = "green"
   else:
      label["background"] = "blue"

var = IntVar()
R1 = Radiobutton(root, text="Red", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Green", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Blue", variable=var, value=3, command=sel)
R3.pack( anchor = W)

label = Label(root, background = "pink", text="No selection")
label.pack()

root.mainloop()
