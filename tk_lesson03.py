from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640,400)
        self.configure(background = "#4D4D4D")

        self.createWidget()

    def createWidget(self):
        label1 = Label(self, text="grid1 Geometry")
        label2 = Label(self, text="grid2 Geometry")
        label3 = Label(self, text="grid3 Geometry")

        # gridの例
        # label1.grid(column = 0, row = 0)
        # label2.grid(column = 0, row = 1)
        # label3.grid(column = 0, row = 2)

        # placeの例
        # label1.place(x = 20, y = 30)
        # label2.place(x = 50, y = 70)
        # label3.place(x = 30, y = 50)

        # packの例
        # label1.pack()
        # label2.pack()
        # label3.pack()


root = Root()
root.mainloop()