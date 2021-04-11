from tkinter import *
root = Tk()

root.geometry("1255x944")

photo = PhotoImage(file="image.png")

photo_label = Label(image=photo)
photo_label.pack()

root.mainloop()