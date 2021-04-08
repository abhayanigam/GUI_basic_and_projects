from tkinter import *

# This is the global function.
def global_function():
    print("I'm the global function.!!")

root = Tk()
root.geometry("655x344")
root.title("Packing buttons")

def hello():
    print("Hello there !")

frame = Frame(root,borderwidth = 8 ,relief = SUNKEN,bg = 'red')
frame.pack(side = LEFT,anchor ="nw")

b1 = Button(frame,fg = "black",bg = "blue",text = "Demo button") # if write pady and padx here then it will cover x & y axix to the borderwidth (in short large click button).
b1.pack(side = LEFT,pady = 23,padx =23) # if write pady and padx here then it will leave space in x & y axix from button to the borderwidth and the button appear small like normal.

b2 = Button(frame,fg = "black",bg = "blue",text = "Function button",command = hello) # command use to call function (remember alwaye write the function name when we use command.)
b2.pack(side = LEFT,pady = 23,padx =23) 

b3 = Button(frame,fg = "black",bg = "blue",text = "quit button",command = quit)  #quit is function use to quit the program.
b3.pack(side = LEFT,pady = 23,padx =23) 

b4 = Button(frame,fg = "black",bg = "blue",text = " Global Function button",command =global_function) # calling the global function. 
b4.pack(side = LEFT,pady = 23,padx =23) 

root.mainloop()