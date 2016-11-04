from tkinter import *
from tkinter import messagebox as msg
from Functies import *


#Opent de feedback scherm
def b():
    """Opent invoer scherm voor tweets"""
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
    invoertweet = e.get("1.0",END)

    def retrieve_input():
        """Verkrijgt de input uit de textbox"""
        input = e.get("1.0", 'end-1c')
        print(input)
        tweet_raw(input)

    tweetButton = PhotoImage(file="tweetButton.png")
    buttonTweet = Button(rootframeb, width=285, height=73, image=tweetButton, borderwidth=0, command=retrieve_input, bg="#ffb400", activebackground="#ffb400")
    buttonTweet.pack()
    buttonTweet.image = tweetButton
    buttonTweet.place(x=631, y=441)




    rootframeb.pack()
    rootb.mainloop()

#Opent de moderation panel
def c():
    """Opent moderation paneel"""
    rootc=Toplevel(root)
    rootc.title("NS Consumenten Zuil - Moderation")
    rootframec = Frame(rootc, bg="#ffb400", width=960, height=540)
    rootc.geometry("+590+335")
    rootframec.pack_propagate(0)
    rootc.resizable(width=False, height=False)
    ingelezenTweet = tweetLezen()
    tweetMod = StringVar()
    text = Label(rootc, textvariable= tweetMod, font=("Helvetica", 20), bg = "#ffb400", wraplength = 960)
    tweetMod.set(ingelezenTweet)
    text.pack()
    text.place(x=25, y=250)

    titelBeginscherm = PhotoImage(file="modCPSchermTitel.png")
    beginschermTitel = Label(rootframec, image=titelBeginscherm, bg="#ffb400")
    beginschermTitel.pack()
    beginschermTitel.image = titelBeginscherm
    beginschermTitel.place(x=47, y=47)

    def rejectconfirm():
        """Bevestigd of je de tweet wil rejecten."""
        if msg.askyesno('Reject Tweet', 'are you sure you wanna reject this tweet?'):
            lees = tweetLezen()
            a = lees
            Tweetlog(a)
            return lees



    def Tweetveranderen(inlees):
        """Verandert tweet op moderation scherm"""
        tweetMod.set(inlees)
        text.pack()
        text.place(x=25, y=250)
        return ingelezenTweet


    def TweetReject():
        """dit wordt uitgevoerd door reject button"""
        inlees = rejectconfirm()
        Tweetveranderen(inlees)

    def TweetAccept():
        """Upload een tweet naar twitter en laat nieuwe tweet zien"""
        lijst = tweetLezen()
        tweetuploaden(lijst)
        Tweetveranderen(lijst)






    approveButton = PhotoImage(file="approveButton.png")
    buttonApprove = Button(rootframec, width=285, height=73, image=approveButton, borderwidth=0, command=TweetAccept, bg="#ffb400", activebackground="#ffb400")
    buttonApprove.pack()
    buttonApprove.image = approveButton
    buttonApprove.place(x=171, y=422)

    denyButton = PhotoImage(file="denyButton.png")
    buttonDeny = Button(rootframec, width=285, height=73, image=denyButton, borderwidth=0, command=TweetReject, bg="#ffb400", activebackground="#ffb400")
    buttonDeny.pack()
    buttonDeny.image = denyButton
    buttonDeny.place(x=506, y=422)

    def sluiten():
        """Bevestiging om moderation window te sluiten, vraagt om bevestiging waarna unmoderated tweets worden verwijdert"""
        if msg.askokcancel("Quit", "Quitting will delete all unmoderated tweets, do you wanna continue?"):
            quit()
            rootc.destroy()


    rootframec.pack()
    rootc.protocol("WM_DELETE_WINDOW", sluiten)
    rootc.mainloop()



#Opent de tweet display scherm
def d():
    """Display scherm voor tweets"""
    rootd=Toplevel(root)
    rootd.title("NS Consumenten Zuil - Display Scherm")
    rootframed = Frame(rootd, bg="#ffb400", width=960, height=540)
    rootd.geometry("+610+355")
    rootframed.pack_propagate(0)
    rootd.resizable(width=False, height=False)

    def display():
        """Plaatst de achtergrond van de display voor tweets"""
        tweetDisplayTitel = PhotoImage(file="tweetDisplayTitel.png")
        titelDisplayTweet = Label(rootframed, image=tweetDisplayTitel, bg="#ffb400")
        titelDisplayTweet.pack()
        titelDisplayTweet.image = tweetDisplayTitel
        titelDisplayTweet.place(x=47, y=47)
    display()

    def refresh():
        """Tweets refreshen op  na 5 seconden indien venster aangeklikt is/open staat en actief is"""
        display()
        tweets = tweetweergeven()
        labeltext1 = StringVar()
        label1 = Label(rootframed,textvariable=labeltext1,font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
        labeltext1.set(tweets[0])
        label1.pack()
        label1.place(x=175, y=175)
        labeltext2 = StringVar()
        label2 = Label(rootframed,textvariable=labeltext2,font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
        labeltext2.set(tweets[1])
        label2.pack()
        label2.place(x=175, y=303)
        labeltext3 = StringVar()
        label3 = Label(rootframed,textvariable=labeltext3,font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
        labeltext3.set(tweets[2])
        label3.pack()
        label3.place(x=175, y=431)

        root.after(5000, refresh)

    rootframed.pack()
    refresh()
    rootd.mainloop()



#Opent de beheer scherm
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
rootframe.pack()
root.mainloop()


