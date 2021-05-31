import pyautogui

print(pyautogui.alert('This is an alert box.'))

print(pyautogui.confirm('Shall I proceed?'))

print(pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']))

print(pyautogui.prompt('What is your name?'))

print(pyautogui.password('Enter password (text will be hidden)'))
