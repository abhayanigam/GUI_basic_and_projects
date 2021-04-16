from tkinter import *

# event handler for button

def addition():
    x = int(e1.get())
    y = int(e2.get())
    leftdata = "hello" + str(x+y)
    leftinput.insert(1, leftdata)


# first paned window
w1 = PanedWindow()
w1.pack(fill=BOTH, expand=1)

leftinput = Entry(w1, bd=5)
w1.add(leftinput)

# second paned window
w2 = PanedWindow(w1, orient=VERTICAL)
w1.add(w2)

e1 = Entry(w2)
e2 = Entry(w2)

w2.add(e1)
w2.add(e2)

bottomBtn = Button(w2, text="Addition", command=addition)
w2.add(bottomBtn)

mainloop()
