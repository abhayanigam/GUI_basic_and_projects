from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("655x344")
root.title("Slider GUI")

def Number():
    print(f"You get {slider.get()}")
    tmsg.showinfo("Number you get!",f"Number {slider.get()}")

# # For vertical slider
# slider = Scale(root, from_=0, to=100)
# slider.pack()

Label(root,text = "How many number do you want.?").pack()

#For horizontal slider
slider = Scale(root, from_ =0 ,to =100,orient = HORIZONTAL,tickinterval = 50)
# slider.set(34) # It sets the scale's value. For example, if we give set(30) the initial scale value will show 30 (the scale will starts from 30)
slider.pack()

Button(root, text ="Get NUM",pady = 10,command = Number).pack()

root.mainloop()