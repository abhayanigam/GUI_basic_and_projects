from tkinter import *

root = Tk()
root.geometry("655x344")

frame = Frame(root,borderwidth = 8 ,relief = SUNKEN,bg = 'red')
frame.grid()

frame2 = Frame(root,borderwidth = 8 ,relief = SUNKEN,bg = 'red')
frame2.grid()

b1 = Button(frame,fg = "black",bg = "blue",text = "click me 1") # if write pady and padx here then it will cover x & y axix to the borderwidth (in short large click button).
b1.pack(side = LEFT) # if write pady and padx here then it will leave space in x & y axix from button to the borderwidth and the button appear small like normal.

b3 = Button(frame2,fg = "black",bg = "blue",text = "click me 2") 
b3.grid(row=0, column=0)

b4 = Button(frame2,fg = "black",bg = "blue",text = "click me 3") 
b4.grid(row=1, column=0)

root.mainloop()