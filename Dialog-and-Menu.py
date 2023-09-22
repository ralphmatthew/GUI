# This code allows to user to import, edit and save a text file using tkinter.

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def open_file():
    fpath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if fpath:
        try:
            file = open(fpath, "r")
            text.delete("1.0", END)
            text.insert(END, file.read())
            file.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file():
    fpath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if fpath:
        try:
            file = open(fpath, "w")
            file.write(text.get("1.0", END))
            file.close()
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def uppercase_change():
    text_content = text.get("1.0", END)
    converted_content = text_content.upper()
    text.delete("1.0", END)
    text.insert(END, converted_content)

def show_about():
    messagebox.showinfo("About", "This is a simple text editor.")

root = Tk()
root.title("Exercise 5")
root.geometry("400x300")

menu_bar = Menu(root)
root.config(menu=menu_bar)

fmenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=fmenu)
fmenu.add_command(label="Open", command=open_file)
fmenu.add_command(label="Save", command=save_file)
fmenu.add_separator()
fmenu.add_command(label="Quit", command=root.quit)

emenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=emenu)
emenu.add_command(label="Convert to Uppercase", command=uppercase_change)

hmenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=hmenu)
hmenu.add_command(label="About", command=show_about)

text = Text(root)
text.pack(expand=True, fill="both")

root.mainloop()
