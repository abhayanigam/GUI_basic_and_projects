import tkinter as tk 
from tkinter import *

win = Tk() 

#to specify size of window. 
win.geometry("250x170") 

# To Create a text widget and specify size. 
T = Text(win, height = 6, width = 53) 

# TO Create label 
l = Label(win, text = "Quote for the Day") 
l.config(font =("Courier", 14)) 

Quote = """Success usually comes to those who are too busy to be looking for it"""

# Create a button for the next text. 
b1 = Button(win, text = "Next", ) 

# Create an Exit button. 
b2 = Button(win, text = "Exit", 
			command = win.destroy) 

l.pack() 
T.pack() 
b1.pack() 
b2.pack() 

# Insert the Quote 
T.insert(tk.END, Quote) 

tk.mainloop() 
