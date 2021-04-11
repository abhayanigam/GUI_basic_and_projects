from tkinter import *

root = Tk()
root.geometry("733x566")

def func():
    print("Function for menu bar")

# Use these to create a non  dropdown menu
# my_menu = Menu(root)
# my_menu.add_command(label = "File", command = func)
# my_menu.add_command(label = "Exit", command = func)
# root.config(menu = my_menu)

main_menu = Menu(root)
m1 = Menu(main_menu,tearoff = 0)
# Tearoff=0 is used so that the menu will not have a tear-off feature, and choices will be added starting at position 0 (the menu section will be attached with GUI window always).

# ------------- Making Menu 1-------------
m1.add_command(label = "New projects",command = func)
m1.add_command(label = "Save",command = func)

# adding a separator line to the menu we use add_separator() method.
m1.add_separator()

m1.add_command(label = "Save as",command = func)
m1.add_command(label = "Print",command = func)
root.config(menu = main_menu)
main_menu.add_cascade(label = "File",menu = m1)

# ------------- Make Menu 2-------------
m2 = Menu(main_menu, tearoff=0)
# Tearoff=0 is used so that the menu will not have a tear-off feature, and choices will be added starting at position 0 (the menu section will be attached with GUI window always).

m2.add_command(label="Cut", command=func)
m2.add_command(label="Copy", command=func)

# Adding a separator line to the menu we use add_separator() method.
m2.add_separator()

m2.add_command(label="Paste", command=func)
m2.add_command(label="Find", command=func)
root.config(menu=main_menu)
main_menu.add_cascade(label="Edit", menu=m2)

root.mainloop()