from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640,400)
        self.configure(background = "#4D4D4D")

        self.createWidget()

    def createWidget(self):
        label = Label(self, text="Hello Tkinter")
        label.grid(column = 0, row = 0)

        label2 = Label(self, text="Second Tkinter Lesson")
        label2.grid(column = 0, row = 1)

root = Root()
root.mainloop()