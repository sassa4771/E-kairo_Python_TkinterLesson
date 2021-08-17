from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640,400)
        self.configure(background = "#4D4D4D")

        # self.label = Label(self, text = "Hello Tkinter")
        # self.label.grid(column=1, row=0)

        # button = Button(self, text = "Click this")
        # button.grid(column=0, row = 0)
        

        self.label1 = ttk.Label(self, text = "Hello Tkinter")
        self.label1.grid(column=1, row=1)

        self.button1 = ttk.Button(self, text = "Click this", command=self.ClickFunction)
        self.button1.grid(column=0, row = 1)  

    def ClickFunction(self):
        self.label1.configure(text = "Button Clicked")
        self.label1.configure(foreground = 'green')

root = Root()
root.mainloop()