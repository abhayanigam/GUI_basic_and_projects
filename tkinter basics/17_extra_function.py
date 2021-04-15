from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("GUI Window")

# root.wm_iconbitmap("1.ico") # To change icon of a tkinter GUI

root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command = root.destroy,).place(relx=0.5, rely=0.5, anchor=CENTER)
# root.destroy is used to destroy window or exit from window.

root.mainloop()