from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640,400)

        # 「""」
        self.name = StringVar();

        self.label1 = ttk.Label(self, text = "名前を入力してね")
        self.label1.grid(column=0, row=0)

        # テキストボックス
        self.textbox = ttk.Entry(self, width=20, textvariable=self.name)
        self.textbox.grid(column=1, row=0)

        self.button1 = ttk.Button(self, text = "ボタンを押す！", command=self.ClickFunction)
        self.button1.grid(column=0, row = 1)  

    def ClickFunction(self):
        self.label1.configure(text = "こんにちは、" + self.name.get() + "さん")

root = Root()
root.mainloop()