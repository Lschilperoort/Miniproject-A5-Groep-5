from tkinter import *

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
