# This code creates a window with a button "Click Here" that prints "Clicked" once pressed.

from tkinter import *
def clicked():
    print("Clicked")
app = Tk()
app.title("GUI Basic Button")
app.geometry('200x200')
button1 = Button(app, text="Click Here", command=clicked)
button1.pack(side='bottom')
app.mainloop()
