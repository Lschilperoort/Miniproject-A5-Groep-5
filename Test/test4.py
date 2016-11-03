from tkinter import *


root=Tk()

def evaluate(event):
    data=e.get("1.0", END)[0:140]
    print(data)

e = Text(root)
e.bind("<Return>", evaluate)
e.pack()

root.mainloop()