from tkinter import *

root = Tk()

root.geometry("655x434")
root.maxsize(1200,989)
root.minsize(200,100)  

f1 = Frame(root,bg = "grey", borderwidth = 6,relief = SUNKEN)
f1.pack(side = LEFT,fill = Y)

f2 = Frame(root,bg = "grey", borderwidth = 8,relief = SUNKEN)
f2.pack(side = TOP,fill = X)

l = Label(f1,text = "Project")
l.pack(pady = 14)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()
