from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter ComboBox")
        self.minsize(640,400)

        self.initUI()

    def ClickFunction(self):
        self.label1.configure(text = "好きな果物は " + self.fruit.get())

    def initUI(self):    
        # 「""」のこと
        self.fruit = StringVar()

        self.label1 = ttk.Label(self, text = "果物を選択")
        self.label1.grid(column=0, row=0)

        self.combo = ttk.Combobox(self, width = 15, textvariable=self.fruit)
        self.combo['value'] = ("りんご", "ナシ", "メロン", "スイカ", "バナナ")
        self.combo.grid(column=1, row=0)

        self.button1 = ttk.Button(self, text = "ボタンを押す", command=self.ClickFunction)
        self.button1.grid(column=0, row = 2)  

root = Root()
root.mainloop()