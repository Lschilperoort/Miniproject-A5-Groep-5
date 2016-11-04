from tkinter import *
from Functies import *


#Opent de feedback scherm
def b():
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

    def Tweetveranderen():
        print('tweetfunctie')
        ingelezenTweet = tweetLezen()
        print(ingelezenTweet)
        tweetMod.set(ingelezenTweet)
        text.pack()
        text.place(x=25, y=250)
        return ingelezenTweet
    def TweetAccept():
        ingelezenTweet = tweetLezen()
        print(ingelezenTweet)
        tweetMod.set(ingelezenTweet)
        text.pack()
        text.place(x=25, y=250)
        Tweetlog(ingelezenTweet)
    def TweetReject():
        Ingelezentweet = Tweetveranderen()
        Tweetlog(Ingelezentweet)

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



    rootframec.pack()
    rootc.mainloop()

#Opent de tweet display scherm
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

    label1 = Label(rootframed,text="GOP strategist Steve Schmidt: #Trump camp's dishonest criminalization of HRC is \"yet another attack on the pillars of democracy\" #NeverTrump",font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
    label1.pack()
    label1.place(x=175, y=175)

    label2 = Label(rootframed,text="If we make it easier for more foreign visitors to visit... (it) grows the #economy.” Pss the #JOLTAct http://tiny.cc/PassJOLT @dddddddddddd!",font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
    label2.pack()
    label2.place(x=175, y=303)

    label3 = Label(rootframed,text="If we make it easier for more foreign visitors to visit... (it) grows the #economy.” Pss the #JOLTAct http://tiny.cc/PassJOLT @dddddddddddd!",font=("Helvetica", 13), bg="white", wraplength=710, justify=LEFT)
    label3.pack()
    label3.place(x=175, y=431)

    rootframed.pack()
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
print(teller)
rootframe.pack()
root.mainloop()


