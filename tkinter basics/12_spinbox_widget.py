from tkinter import *

root = Tk()
root.geometry("300x200")

spin = Label(root,text = "Spin Box widget",fg = "navyblue",font = "50").pack()

sp = Spinbox(root,from_ = 0, to = 50).pack()

root.mainloop()