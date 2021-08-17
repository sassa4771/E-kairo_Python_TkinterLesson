from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Scroll Text")
        self.minsize(640,400)

        self.labelFrame = ttk.LabelFrame(self, text = "Label Frame")
        self.labelFrame.grid(column=0, row = 7, padx=0, pady=0)

        self.labels()

    def labels(self):
        ttk.Label(self.labelFrame, text="Label1").grid(column=0, row=0, sticky=W)
        ttk.Label(self.labelFrame, text="Label2").grid(column=0, row=1, sticky=W)
        ttk.Label(self.labelFrame, text="Label3").grid(column=0, row=2, sticky=W)

root = Root()
root.mainloop()