from tkinter import *

class View(Frame):
    count = 0
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        b = Button(self, text="Open new window", command=self.new_window)
        b.pack(side="top")

    def new_window(self):
        self.count += 1
        id = "New window #%s" % self.count
        window = Toplevel(self)
        label = Label(window, text=id)
        label.pack(side="top", fill="both", padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    view = View(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
