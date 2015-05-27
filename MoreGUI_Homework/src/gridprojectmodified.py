from tkinter import *
from tkinter.messagebox import showwarning

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
        
        #Frame 1 configuration
        f1 = Frame(self, bg="green")      
        f1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)
        self.l1 = Label(f1, text="Frame 1", bg="green")
        self.l1.bind("<Button-1>", self.handlerf1)
        self.l1.pack(fill=BOTH, expand=True)
        
        #Frame 2 configuration
        f2 = Frame(self, bg="blue")
        f2.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
        self.l2 = Label(f2, text="Frame 2", bg="blue")
        self.l2.bind("<Button-1>", self.handlerf2)
        self.l2.pack(fill=BOTH, expand=True)
        
        #Buttons creation and configuration
        #self.columnconfigure(num, weight=1)
        self.red_button = Button(self, text="Red", width=25, command=lambda: self.changecolor("Red")).grid(row=5, column=0, sticky=ALL)
        self.blue_button = Button(self, text="Blue", width=25, command=lambda: self.changecolor("Blue")).grid(row=5, column=1, sticky=ALL)
        self.green_button = Button(self, text="Green", width=25, command=lambda: self.changecolor("green")).grid(row=5, column=2, sticky=ALL)
        self.black_button = Button(self, text="Black", width=25, command=lambda: self.changecolor("black")).grid(row=5, column=3, sticky=ALL)
        self.open_button = Button(self, text="Open", width=25, command=self.opendoc).grid(row=5, column=4, sticky=ALL) 
        
        #Frame 3 configuration
        self.f3 = Frame(self, bg="red")
        self.f3.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)
        self.browse_doc = Entry(self.f3)
        self.browse_doc.pack(fill=BOTH, expand=True)
        self.doc_text = Text(self.f3)
        self.doc_text.pack(fill=BOTH, expand=True)
        
    def handlerf1(self, event):
        self.l1.config(text="Click on Frame 1, x: {0}, y: {1}".format(event.x, event.y))
        print("Click on Frame 1, x: {0}, y: {1}".format(event.x, event.y))
    
    def handlerf2(self, event):
        self.l2.config(text="Click on Frame 2, x: {0}, y: {1}".format(event.x, event.y))
        print("Click on Frame 2, x: {0}, y: {1}".format(event.x, event.y))
    
    def changecolor(self,thecolor):
        self.browse_doc.config(fg=thecolor)
        self.doc_text.config(fg=thecolor)
    
    def opendoc(self):
        file_name = self.browse_doc.get()
        try:
            f = open(file_name, "r")
            self.file_text = f.read()
            f.close()
            self.doc_text.delete(1.0, END)
            self.doc_text.insert(END, self.file_text)
        except FileNotFoundError:
            showwarning("Open","{0}\n File not found".format(file_name))
root = Tk()
app = Application(master=root)
app.mainloop()


        
        