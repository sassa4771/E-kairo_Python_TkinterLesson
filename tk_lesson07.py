from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640,400)      

        self.label1 = ttk.Label(self, text = "チェックボックスを選択してね！")
        self.label1.grid(column=1, row=1)

        self.check2_value = BooleanVar(value = False)
        self.check3_value = BooleanVar(value = True)
        
        self.checkButton()

    def checkButton(self):
        self.check1 = ttk.Checkbutton(self, text = "Disabled", state="disabled")
        self.check1.grid(row=0, column=0, sticky=W)

        self.check2 = ttk.Checkbutton(self, text = "Unchecked", variable=self.check2_value, command = self.check2_click)
        self.check2.grid(row=0, column=1)

        self.check3 = ttk.Checkbutton(self, text = "Checked", variable=self.check3_value, command = self.check3_click)
        self.check3.grid(row=0, column=2)

    def check2_click(self):
        if(self.check2_value.get()):
            self.label1.configure(text = "Check2を選択しました")
        else:
            self.label1.configure(text = "Check2を外しました")
    
    def check3_click(self):
        if(self.check3_value.get()):
            self.label1.configure(text = "Check3を選択しました")
        else:
            self.label1.configure(text = "Check3を外しました")

root = Root()
root.mainloop()