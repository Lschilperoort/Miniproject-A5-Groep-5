from tkinter import *

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
