from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.maxsize(400,400)
        self.minsize(400,400)
        self.title("The EXTRA Simple Calculator.")
        self.heading = Label(self,text = "Calculator",font = "Helvetica 20 bold").grid(padx = 30,row = 1, column = 2)

    def values(self):
        self.value1 = Label(self,text = "Value for A",font = "Helvetica 12 bold").grid(padx = 30,row = 2, column = 1)
        self.value2 = Label(self,text = "Value for B",font = "Helvetica 12 bold").grid(padx = 30,row = 3, column = 1)
        self.op = Label(self,text = "Operation",font = "Helvetica 12 bold").grid(padx = 30,row = 4, column = 1)

        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.operation = StringVar()

        Entry(self,textvariable = self.var_1,width = 3,font =('Helvetica',30)).grid(row = 2, column = 2,padx = 10,pady = 10)
        Entry(self,textvariable = self.var_2,width = 3,font =('Helvetica',30)).grid(row = 3, column = 2,padx = 10,pady = 10)
        Entry(self,textvariable = self.operation,width = 3,font =('Helvetica',30)).grid(row = 4, column = 2,padx = 10,pady = 10)

    def upload(self):
        if self.operation.get() == '+':
            s1 = int(self.var_1.get())
            s2 = int(self.var_2.get())
            ans = s1+s2
            operation = f"The addition is {ans}"

        elif self.operation.get() == '-':
            s1 = int(self.var_1.get())
            s2 = int(self.var_2.get())
            ans = s1-s2
            operation = f"The substraction is {ans}" 

        elif self.operation.get() == '*':
            s1 = int(self.var_1.get())
            s2 = int(self.var_2.get())
            ans = s1*s2
            operation = f"The multiplication is {ans}" 

        elif self.operation.get() == '/':
            s1 = int(self.var_1.get())
            s2 = int(self.var_2.get())
            ans = s1/s2
            operation = f"The division is {ans}" 

        Label(self,text = operation,font = "Helvetica 12 bold").grid(row = 5,column = 2,pady = 10)

    def create_button(self):
        Button(self,text = "Calculate",command = self.upload).grid(row = 5,column = 2)

if __name__ == '__main__':
    window = GUI()
    window.values()
    window.create_button()
    window.mainloop()