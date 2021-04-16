from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("The Simple Calculator.")

    def values(self):
        self.value1 = Label(self,text = "Value for A",font = "Helvetica 12 bold").grid(padx = 30,row = 1, column = 1)
        self.value2 = Label(self,text = "Value for B",font = "Helvetica 12 bold").grid(padx = 30,row = 2, column = 1)

        self.var_1 = StringVar()
        self.var_2 = StringVar()

        self.var_1_entry = Entry(self,textvariable = self.var_1,width = 10,font =('Helvetica',30)).grid(row = 1, column = 2,padx = 10,pady = 10)
        self.var__entry = Entry(self,textvariable = self.var_2,width = 10,font =('Helvetica',30)).grid(row = 2, column = 2,padx = 10,pady = 10)

    def add(self):
        s1 = float(self.var_1.get())
        s2 = float(self.var_2.get())
        ans = s1+s2
        operation = f"The addition is {ans}"
        Label(self,text = operation,font = "Helvetica 12 bold").grid(column = 1,pady = 10)

    def sub(self):
        s1 = float(self.var_1.get())
        s2 = float(self.var_2.get())
        ans = s1-s2
        operation = f"The substraction is {ans}"
        Label(self,text = operation,font = "Helvetica 12 bold").grid(column = 1,pady = 10)

    def multi(self):
        s1 = float(self.var_1.get())
        s2 = float(self.var_2.get())
        ans = s1*s2
        operation = f"The multiplication is {ans}"
        Label(self,text = operation,font = "Helvetica 12 bold").grid(column = 1,pady = 10)

    def div(self):
        s1 = float(self.var_1.get())
        s2 = float(self.var_2.get())
        ans = s1/s2
        operation = f"The division is {ans}"
        Label(self,text = operation,font = "Helvetica 12 bold").grid(column = 1,pady = 10)

    def create_button1(self):
        Button(self,text = "+",command = self.add, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 10).grid(row = 4,column = 1,padx = 10,pady = 20)

    def create_button2(self):
        Button(self,text = "-",command = self.sub, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 10).grid(row = 5,column = 1,padx = 10,pady = 10)

    def create_button3(self):
        Button(self,text = "*",command = self.multi, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 10).grid(row = 4,column = 2,padx = 10,pady = 20)

    def create_button4(self):
        Button(self,text = "/",command = self.div, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 10).grid(row = 5,column = 2,padx = 10,pady = 10)


if __name__ == '__main__':
    window = GUI()
    window.values()
    window.create_button1()
    window.create_button2()
    window.create_button3()
    window.create_button4()
    window.mainloop()