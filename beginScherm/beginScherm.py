from tkinter import *

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

inputButton = PhotoImage(file="input-button.png")
buttonInput = Button(rootframe, width=256, height=96, image=inputButton, borderwidth=0, command=rootframe.quit, bg="#ffb400")
buttonInput.pack()
buttonInput.image = inputButton
buttonInput.place(x=47, y=282)

tweetDisplayButton = PhotoImage(file="tweetDisplay-button.png")
displayTweetButton = Button(rootframe, width=256, height=96, image=tweetDisplayButton, borderwidth=0, command=rootframe.quit, bg="#ffb400")
displayTweetButton.pack()
displayTweetButton.image = tweetDisplayButton
displayTweetButton.place(x=353, y=282)

modPanelButton = PhotoImage(file="moderationPanel-button.png")
modCPButton = Button(rootframe, width=256, height=96, image=modPanelButton, borderwidth=0, command=rootframe.quit, bg="#ffb400")
modCPButton.pack()
modCPButton.image = modPanelButton
modCPButton.place(x=659, y=282)

rootframe.pack()
root.mainloop()
