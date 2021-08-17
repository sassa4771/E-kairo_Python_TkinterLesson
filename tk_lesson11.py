from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Tab Controls")
        self.minsize(640,400)
        
        tabControl = ttk.Notebook(self)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Tab 1")
        
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Tab 2")
        
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text="Tab 3")

        tabControl.pack(expan = 1, fill = "both")

        label = Label(tab1, text="テストだよ1")
        label.grid(column = 0, row = 0)
        label = Label(tab2, text="テストだよ2")
        label.grid(column = 0, row = 0)
        label = Label(tab3, text="テストだよ3")
        label.grid(column = 0, row = 0)

root = Root()
root.mainloop()