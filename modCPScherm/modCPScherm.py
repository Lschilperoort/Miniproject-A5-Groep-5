from tkinter import *

root=Tk()
root.title("NS Consumenten Zuil - Moderation")

rootframe = Frame(root, bg="#ffb400", width=960, height=540)
rootframe.pack_propagate(0)
root.resizable(width=False, height=False)

titelBeginscherm = PhotoImage(file="modCPSchermTitel.png")
beginschermTitel = Label(rootframe, image=titelBeginscherm, bg="#ffb400")
beginschermTitel.pack()
beginschermTitel.image = titelBeginscherm
beginschermTitel.place(x=47, y=47)

approveButton = PhotoImage(file="approveButton.png")
buttonApprove = Button(rootframe, width=285, height=73, image=approveButton, borderwidth=0, command=rootframe.quit, bg="#ffb400", activebackground="#ffb400")
buttonApprove.pack()
buttonApprove.image = approveButton
buttonApprove.place(x=171, y=422)

denyButton = PhotoImage(file="denyButton.png")
buttonDeny = Button(rootframe, width=285, height=73, image=denyButton, borderwidth=0, command=rootframe.quit, bg="#ffb400", activebackground="#ffb400")
buttonDeny.pack()
buttonDeny.image = denyButton
buttonDeny.place(x=506, y=422)

rootframe.pack()
root.mainloop()
