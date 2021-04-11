from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas GUI")

can_widget = Canvas(root,width = canvas_width,height = canvas_height)

# This line goes from the point x1, y1 to x2,y2.
can_widget.create_line(0,0,800,400,fill = "red")
can_widget.create_line(0,400,800,0,fill = "red")

# To create a rectangel specify parameter in this order coors of the top left and coor of bottom right.
can_widget.create_rectangle(3,5,700,300,fill = "blue")

can_widget.create_text(200,200,text = "Python GUI")

can_widget.create_oval(344,233,244,355)

can_widget.pack()

root.mainloop()