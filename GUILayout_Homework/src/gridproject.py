from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for row in range(4):
            self.rowconfigure(row, weight=1)
        for col in range(5):
            self.columnconfigure(col, weight=1)
        f1 = Frame(self, bg="green")
        f1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)
        l1 = Label(f1, text="Frame 1", bg="green")
        l1.pack(fill=BOTH, expand=True)
        f2 = Frame(self, bg="blue")
        f2.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
        l2 = Label(f2, text="Frame 2", bg="blue")
        l2.pack(fill=BOTH, expand=True)
        for col in range(5):
            self.columnconfigure(col, weight=1)
            Button(self, text="Button {0}".format(col+1)).grid(row=5, column=col, sticky=ALL)
        f3 = Frame(self, bg="red")
        f3.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)
        l3 = Label(f3, text="Frame 3", bg="red")
        l3.pack(fill=BOTH, expand=True)
        
root = Tk()
app = Application(master=root)
app.mainloop()


        
        