from tkinter import *

class Application(Frame):
    """Application Main"""
    def __init__(self, master=None):
        """Main Frame initialization"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        #Enter number 1 label and textbox
        top_frame_section1 = Frame(self)
        self.number1 = Label(top_frame_section1, text="Enter a number").pack(side=LEFT)
        self.text_in_number1 = Entry(top_frame_section1)
        self.text_in_number1.pack(side=LEFT)
        top_frame_section1.pack(side=TOP)
        #Enter number 2 label and textbox
        top_frame_section2 = Frame(self)
        self.number2 = Label(top_frame_section2, text="Enter a number").pack(side=LEFT)
        self.text_in_number2 = Entry(top_frame_section2)
        self.text_in_number2.pack(side=LEFT)
        top_frame_section2.pack(side=TOP)
        #Result label
        top_frame_section3 = Frame(self)
        self.result = Label(top_frame_section3, text="Waiting...")
        self.result.pack()
        top_frame_section3.pack(side=TOP)
        #Calculate and Close buttons
        bottom_frame = Frame(self)
        self.calculation = Button(bottom_frame, text="Calculate", command=self.Sum_numbers)
        self.calculation.pack(side=LEFT)
        self.close = Button(bottom_frame, text="Close", command=self.quit)
        self.close.pack(side=RIGHT)
        bottom_frame.pack(side=TOP)
        
    def Sum_numbers(self):
        """Get 2 numbers and return the result of the sum of both numbers"""
        try:
            self.text_in_number1
            num1 = float(self.text_in_number1.get())
            num2 = float(self.text_in_number2.get())
            result = num1 + num2
            self.result.config(text=result)
        except ValueError:
            self.result.config(text="***ERROR***") 
        
root = Tk()
app = Application(master=root)
app.mainloop()
        
        
        
        
        