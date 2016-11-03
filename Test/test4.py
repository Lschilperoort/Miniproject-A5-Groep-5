from tkinter import *
root = Tk()

def additem():
    global items
    items += 1
    b.configure(text="I have %s items" % (items))

items = 14
b = Button(root, text="I have %s items" % (items), command=additem)
b.pack()

root.mainloop()