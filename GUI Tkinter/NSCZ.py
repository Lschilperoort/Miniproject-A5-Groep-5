from tkinter import *
from projectbestand import *

def b():
    def enter():
        root = Tk()

        def evaluate(event):
            data = e.get("1.0", END)[0:140]
            print(data)

        e = Text(root)
        e.bind("<Return>", evaluate)
        e.pack()

        root.mainloop()


    rootb=Toplevel(root)
    rootb.title("NS Consumenten Zuil - Feedback")
    rootframeb = Frame(rootb, bg="#ffb400", width=960, height=540)
    rootb.geometry("+570+315")
    rootframeb.pack_propagate(0)
    rootb.resizable(width=False, height=False)

    titelBeginscherm = PhotoImage(file="invoerSchermTitel.png")
    beginschermTitel = Label(rootframeb, image=titelBeginscherm, bg="#ffb400")
    beginschermTitel.pack()
    beginschermTitel.image = titelBeginscherm
    beginschermTitel.place(x=47, y=47)

    e = Text(rootframeb)
    e.pack()
    e.place(x=47, y=282, relwidth=1, relheight=1, width=-91, height=-400)

    tweetButton = PhotoImage(file="tweetButton.png")
    buttonTweet = Button(rootframeb, width=285, height=73, image=tweetButton, borderwidth=0, command=enter(), bg="#ffb400", activebackground="#ffb400")
    buttonTweet.pack()
    buttonTweet.image = tweetButton
    buttonTweet.place(x=631, y=441)

    rootframeb.pack()
    rootb.mainloop()

def c():
    rootc=Toplevel(root)
    rootc.title("NS Consumenten Zuil - Moderation")
    rootframec = Frame(rootc, bg="#ffb400", width=960, height=540)
    rootc.geometry("+590+335")
    rootframec.pack_propagate(0)
    rootc.resizable(width=False, height=False)

    titelBeginscherm = PhotoImage(file="modCPSchermTitel.png")
    beginschermTitel = Label(rootframec, image=titelBeginscherm, bg="#ffb400")
    beginschermTitel.pack()
    beginschermTitel.image = titelBeginscherm
    beginschermTitel.place(x=47, y=47)

    approveButton = PhotoImage(file="approveButton.png")
    buttonApprove = Button(rootframec, width=285, height=73, image=approveButton, borderwidth=0, command=NONE, bg="#ffb400", activebackground="#ffb400")
    buttonApprove.pack()
    buttonApprove.image = approveButton
    buttonApprove.place(x=171, y=422)

    denyButton = PhotoImage(file="denyButton.png")
    buttonDeny = Button(rootframec, width=285, height=73, image=denyButton, borderwidth=0, command=NONE, bg="#ffb400", activebackground="#ffb400")
    buttonDeny.pack()
    buttonDeny.image = denyButton
    buttonDeny.place(x=506, y=422)

    rootframec.pack()
    rootc.mainloop()

def d():
    rootd=Toplevel(root)
    rootd.title("NS Consumenten Zuil - Display Scherm")
    rootframed = Frame(rootd, bg="#ffb400", width=960, height=540)
    rootd.geometry("+610+355")
    rootframed.pack_propagate(0)
    rootd.resizable(width=False, height=False)

    tweetDisplayTitel = PhotoImage(file="tweetDisplayTitel.png")
    titelDisplayTweet = Label(rootframed, image=tweetDisplayTitel, bg="#ffb400")
    titelDisplayTweet.pack()
    titelDisplayTweet.image = tweetDisplayTitel
    titelDisplayTweet.place(x=47, y=47)

    rootframed.pack()
    rootd.mainloop()

root=Tk()
root.title("NS Consumenten Zuil - Beheer")
rootframe = Frame(root, bg="#ffb400", width=960, height=540)
root.geometry("+470+215")
rootframe.pack_propagate(0)
root.resizable(width=False, height=False)

titelBeginscherm = PhotoImage(file="beginScherm.png")
beginschermTitel = Label(rootframe, image=titelBeginscherm, bg="#ffb400")
beginschermTitel.pack()
beginschermTitel.image = titelBeginscherm
beginschermTitel.place(x=47, y=47)

inputButton = PhotoImage(file="inputButton.png")
buttonInput = Button(rootframe, width=256, height=96, image=inputButton, borderwidth=0, command=b, bg="#ffb400", activebackground="#ffb400")
buttonInput.pack()
buttonInput.image = inputButton
buttonInput.place(x=47, y=282)

tweetDisplayButton = PhotoImage(file="tweetDisplayButton.png")
displayTweetButton = Button(rootframe, width=256, height=96, image=tweetDisplayButton, borderwidth=0, command=d, bg="#ffb400", activebackground="#ffb400")
displayTweetButton.pack()
displayTweetButton.image = tweetDisplayButton
displayTweetButton.place(x=353, y=282)

modPanelButton = PhotoImage(file="moderationPanelButton.png")
modCPButton = Button(rootframe, width=256, height=96, image=modPanelButton, borderwidth=0, command=c, bg="#ffb400", activebackground="#ffb400")
modCPButton.pack()
modCPButton.image = modPanelButton
modCPButton.place(x=659, y=282)

tweetuploaden('importtest')
