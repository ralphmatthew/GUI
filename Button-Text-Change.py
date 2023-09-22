# This code creates a window with a button "Hello!" that changes to "Hi!" once pressed.

from tkinter import *
app = Tk()
app.title("Button Text Change")
app.geometry('200x100')

def changetext():
    if  label['text'] == "Hello!":
        label['text'] = "Hi!"
    else:
        label['text'] = "Hello!"

button = Button(app, text="Change Text", command=changetext)
label = Label(app, text="Hello!")

label.pack(side='bottom')
button.pack(side='bottom')

app.mainloop()
