from tkinter import *


class TweetScherm:

    def __init__(self, master):
        frame = Frame(master, width=960, height=540)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")


class Screening:

    def __init__(self, master):
        frame = Frame(master, width=960, height=540)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked too!")


class Invoer:

    def __init__(self, master):
        frame = Frame(master, width=960, height=540)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked for the third time!")

root = Tk()
root.title("GebruikerInterface")
frame4 = Frame(root, width=960, height=540)
frame4.pack()

#TweetScherm
top1 = Toplevel()
top1.title("Meest Recente Tweets")
a = TweetScherm(top1)
frame1 = Frame(top1, width=960, height=540)
frame1.pack()
msg = Message(top1, text="about_message")
msg.pack()
button = Button(top1, text="Dismiss", command=top1.destroy)
button.pack()

#Screening
top2 = Toplevel()
frame2 = Frame(top2, width=960, height=540)
frame2.pack()
top2.title("NS Screening")
b = Screening(top2)

#TekstInvoer
top3 = Toplevel()
frame3 = Frame(top2, width=960, height=540)
frame3.pack()
top3.title("Invoer")
c = Invoer(top3)



root.mainloop()

