import pyautogui as pag

# The typewrite() function is used to type something in a text field
# pag.typewrite(text, interval)

# Here text is what you wish to type in the field and interval
#  is time in seconds between each key stroke

pag.typewrite('GitHub', 1)
pag.write('Hello world!', interval=0.25)

pag.typewrite(['G', 'i', 't', 'H', 'u', 'b', 'backspace', 'enter'])

# The typewrite() function would press both those buttons in a sequence, not simultaneously.
# To press two or more keys simultaneously, you can use the hotkey() function

pag.hotkey('shift', 'enter')
pag.hotkey('alt', 'tab' ) # For the @ symbol
pag.hotkey('ctrl', 'c')  # For the copy command

pag.press('esc') # Simulate pressing the Escape key.
pag.keyDown('shift')
pag.write(['left', 'left', 'left', 'left', 'left', 'left'])
pag.keyUp('shift')
pag.hotkey('ctrl', 'c')

