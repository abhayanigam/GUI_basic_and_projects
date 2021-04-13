from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Creating scrollbar gui")

# #To connect scrollbar to a widget
# 1. widget(yscrollcommmand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill = Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(50):
    listbox.insert(END, "Item ",i)

listbox.pack(fill = "both")
scrollbar.config(command=listbox.yview)

#text = Text(root, yscrollcommand = scrollbar.set)
#text.pack(fill=BOTH)
#scrollbar.config(command=text.yview)

root.mainloop()