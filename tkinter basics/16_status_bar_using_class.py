from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("655x344")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvariable = self.var,relief = SUNKEN,anchor = "w")
        self.statusbar.pack(side = BOTTOM,fill = X)

    def upload(self):
        self.var.set("Busy..")
        self.statusbar.update()
        import time
        time.sleep(2)
        self.var.set("Ready Now")

    def create_button(self,inp_text):
        Button(self,text = inp_text,command = self.upload).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.create_button('Click me')
    window.mainloop()

#--------------------------------------------------------------------------------
exit() # is use to exit from Here.

# For Status bar program

from tkinter import *

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.geometry("455x233")
root.title("Status bar tutorial")


statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()
root.mainloop()