from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Creating Radio Buttons")

def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

#For string.
var = StringVar()
var.set("Radio")

# #For integer.
# var = IntVar()
# var.set(1)

Label(root, text = "What would you like to have sir?",font="lucida 19 bold",justify=LEFT, padx=14).pack()

radio = Radiobutton(root,text = "Dosa",variable = var,padx=10, value = "Dosa").pack()
radio = Radiobutton(root,text = "Idly",variable = var,padx=10, value = "Idly").pack()
radio = Radiobutton(root,text = "Samosa",variable = var,padx=10, value = "Samosa").pack()

Button(root,text = "Order Now",command = order).pack()

root.mainloop()