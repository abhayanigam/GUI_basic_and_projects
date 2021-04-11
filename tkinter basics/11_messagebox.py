from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("655x344")
root.title("MessageBox")

def help():
    print("I will help you")
    tmsg.showinfo("Help","This gui will help you.")
    # a = tmsg.showinfo("Help","This gui will help you.")
    # print(a)

def rate():
    print("Rate Us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes" :
        msg = "Great"
    else:
        msg = "Tell us what went wrong"
    tmsg.showinfo("Experience",msg)

def gui_func():
    ans = tmsg.askretrycancel("GUI is your friend","Sorry for this")
    if ans:
        print("Retring...")
    else:
        print("Canceling...")

main_menu = Menu(root)
m1 = Menu(main_menu,tearoff = 0)
m1.add_command(label = "Help",command = help)
m1.add_command(label = "Rate us",command = rate)
m1.add_command(label = "Friend",command = gui_func)
root.config(menu = main_menu)
main_menu.add_cascade(label = "Help",menu = m1)


root.mainloop()