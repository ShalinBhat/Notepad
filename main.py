
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()


root.title("Notepad")

root.geometry('644*600+350+40')
TextArea = scrolledtext.ScrolledText(root, front="lucida 13")
TextArea.pack(ecpand=True, fill=BOTH)
file = None

# create manue bar

MenuBar = Menu(root)
root.config(menu=MenuBar)

# configure File and Edit menus with MenuBar

FileMenu = Menu(MenuBar)

FileMenu: Menu = Menu(MenuBar, tearoff=0)
EditMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="File", menu=FileMenu)
MenuBar.add_cascade(label="Edit", menu=EditMenu)


def newFile():
    global file
    root.title("Untitled - Notepad")
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")

        # TextArea.delete(1.0),END)

        f = open(file, "r")

        # f.write(TectArea.get(1.0,END))

        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetype=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open((file, "w"))
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")

    else:
        f = open((file, "w"))
        f.write(TextArea.get(1.0, END))
        f.close()


def exitFile():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


# adding new, open, and save file functionality to File menu

FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=saveFile)

# sapret inside menu

FileMenu.add_command(label="Exit", command=exitFile)

# adding cut,paste, copy

EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
root.mainloop()
