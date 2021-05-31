import pyautogui as pag

# disable the fail-safe if PAUSE function shows an error, add the following line at the start of your code
pag.FAILSAFE = False

# Genral Functions :-
print("x and y : ",pag.position()) # current mouse x and y.

# The onScreen() function tells us whether the point with coordinates x and y exists on the screen:
print(pag.onScreen(500, 600))
print(pag.onScreen(0, 10000))

# The size() function finds the height and width (resolution) of a screen.
print("The size is ",pag.size())

# moveTo() function that moves the mouse cursor on the screen based on the coordinates we provide as parameters.
pag.moveTo(0, 0)
# PAUSE property; it basically pauses the execution of the script for the given amount of time. 
pag.PAUSE = 5
pag.moveTo(100, 500) 
pag.PAUSE = 2
pag.moveTo(500, 500)

# moveRel() function with the parameters (100, 100, 2) the new position of your move cursor would be (200, 200
pag.moveRel(100, 100, 2)

'''
The click() function is used to imitate mouse click operations. 
    pag.click(x, y, clicks, interval, button)

    x: the x-coordinate of the point to reach
    y: the y-coordinate of the point to reach
    clicks: the number of clicks that you would like to do when the cursor gets to that point on screen
    interval: the amount of time in seconds between each mouse click i.e. if you are doing multiple mouse clicks
    button: specify which button on the mouse you would
'''
pag.click(100, 100, 5, 2, 'right')

# Also Use These Functions 
pag.rightClick(500,500)    # x,y
pag.doubleClick(200,300)   # x,y
pag.tripleClick(150,260)   # x,y
pag.middleClick(400,500)   # x,y

# mouseDown and mouseUp functions
pag.mouseDown(x=300, y=600, button='left')
pag.mouseUp(x=500, y=100, button='left')

# The last mouse function we are going to cover is scroll. 
# pag.scroll(amount_to_scroll, x=x_movement, y=y_movement)
pag.scroll(100, 120, 120)