from tkinter import *

root = Tk()
root.geometry("655x444")

def getValue():
    print(f"Username is {uservalue.get()}and Password is {passwordValue.get()} ")
    #gets is use to get the value.
user = Label(root,text = "Username ")
user.grid() # by default row is 0.

password = Label(root,text = "Password ")
password.grid(row= 1)

# Note :- Variable classes in Tkinter.
#         1. BooleanVar
#         2. DoubleVar
#         3. IntVar
#         4. StringVar

uservalue = StringVar()
passwordValue = StringVar()

userEntry = Entry(root,textvariable = uservalue)
userEntry.grid(row = 0,column = 1,pady = 10)

passwordEntry = Entry(root,textvariable = passwordValue)
passwordEntry.grid(row = 1,column = 1,pady = 10)

button1 = Button(root,text = "Submit",command = getValue)
button1.grid(row = 2,column =1,pady = 10)

root.mainloop()