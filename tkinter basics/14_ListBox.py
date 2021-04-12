from tkinter import *

def add():
    global i 
    list_box.insert(ACTIVE,i);
    i+=1

i = 0

"""
Note:
    Within this function, insert() method is used to insert the new lines with the specified 
    number of elements before the specified index. 
    Here the index is i and it will be incremented. 
    Here a special index ACTIVE is used, which refers to the “active” 
    item (set when you click on an item, or by the arrow keys) 
    and start insert further items before that index only
"""
root = Tk()
root.geometry("455x233")
root.title("Listbox in GUI")

list_box = Listbox(root)
list_box.pack()

list_box.insert(END,"First item")
#  END is used to append items to the list.

Button(root,text = "Add item",command = add).pack()

root.mainloop()