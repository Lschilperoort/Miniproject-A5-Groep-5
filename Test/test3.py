from tkinter import *
def a():
    root=Tk()
    root.title("NS Consumenten Zuil - Beheer")
    rootframe = Frame(root, bg="#ffb400", width=960, height=540)
    rootframe.pack_propagate(0)
    root.resizable(width=False, height=False)
    titelBeginscherm = PhotoImage(file="beginScherm.png")
    beginschermTitel = Label(rootframe, image=titelBeginscherm, bg="#ffb400")
    beginschermTitel.pack()
    beginschermTitel.image = titelBeginscherm
    beginschermTitel.place(x=47, y=47)
    inputButton = PhotoImage(file="inputButton.png")
    buttonInput = Button(rootframe, width=256, height=96, image=inputButton, borderwidth=0, command=b(), bg="#ffb400", activebackground="#ffb400")
    buttonInput.pack()
    buttonInput.image = inputButton
    buttonInput.place(x=47, y=282)
    tweetDisplayButton = PhotoImage(file="tweetDisplayButton.png")
    displayTweetButton = Button(rootframe, width=256, height=96, image=tweetDisplayButton, borderwidth=0, command=c(), bg="#ffb400", activebackground="#ffb400")
    displayTweetButton.pack()
    displayTweetButton.image = tweetDisplayButton
    displayTweetButton.place(x=353, y=282)
    modPanelButton = PhotoImage(file="moderationPanelButton.png")
    modCPButton = Button(rootframe, width=256, height=96, image=modPanelButton, borderwidth=0, command=d(), bg="#ffb400", activebackground="#ffb400")
    modCPButton.pack()
    modCPButton.image = modPanelButton
    modCPButton.place(x=659, y=282)
    rootframe.pack()
    root.mainloop()

def b():
    root=Tk()
    root.title("NS Consumenten Zuil - Feedback")
    rootframe = Frame(root, bg="#ffb400", width=960, height=540)
    rootframe.pack_propagate(0)
    root.resizable(width=False, height=False)
    titelBeginscherm = PhotoImage(file="invoerSchermTitel.png")
    beginschermTitel = Label(rootframe, image=titelBeginscherm, bg="#ffb400")
    beginschermTitel.pack()
    beginschermTitel.image = titelBeginscherm
    beginschermTitel.place(x=47, y=47)
    e = Text(rootframe)
    e.pack()
    e.place(x=47, y=282, relwidth=1, relheight=1, width=-91, height=-400)
    tweetButton = PhotoImage(file="tweetButton.png")
    buttonTweet = Button(rootframe, width=285, height=73, image=tweetButton, borderwidth=0, command=rootframe.quit, bg="#ffb400", activebackground="#ffb400")
    buttonTweet.pack()
    buttonTweet.image = tweetButton
    buttonTweet.place(x=631, y=441)
    rootframe.pack()
    root.mainloop()



def c():
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

def d():
    root=Tk()
    root.title("NS Consumenten Zuil - Display Scherm")
    rootframe = Frame(root, bg="#ffb400", width=960, height=540)
    rootframe.pack_propagate(0)
    root.resizable(width=False, height=False)
    tweetDisplayTitel = PhotoImage(file="tweetDisplayTitel.png")
    titelDisplayTweet = Label(rootframe, image=tweetDisplayTitel, bg="#ffb400")
    titelDisplayTweet.pack()
    titelDisplayTweet.image = tweetDisplayTitel
    titelDisplayTweet.place(x=47, y=47)
    rootframe.pack()
    root.mainloop()

a()
