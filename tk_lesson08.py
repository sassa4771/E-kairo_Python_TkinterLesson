from tkinter import *
from tkinter import ttk

COLOR1 = "blue"
COLOR2 = "Red"
COLOR3 = "Gold"

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter RadioButton")
        self.minsize(640,400)

        self.radioButton()

    def radioEvent(self):
        radSeleted = self.radValues.get()

        if radSeleted == 1:
            self.configure(background= COLOR1)
        elif radSeleted == 2:
            self.configure(background= COLOR2)
        elif radSeleted == 3:
            self.configure(background= COLOR3)

    def radioButton(self):
        self.radValues = IntVar()
        red1 = ttk.Radiobutton(self, text=COLOR1, value=1, variable=self.radValues, command=self.radioEvent)
        red1.grid(column = 0, row = 0, sticky = W, columnspan=3)
        
        red2 = ttk.Radiobutton(self, text=COLOR2, value=2, variable=self.radValues, command=self.radioEvent)
        red2.grid(column = 0, row = 1, sticky = W, columnspan=3)
        
        red3 = ttk.Radiobutton(self, text=COLOR3, value=3, variable=self.radValues, command=self.radioEvent)
        red3.grid(column = 0, row = 2, sticky = W, columnspan=3)

root = Root()
root.mainloop()