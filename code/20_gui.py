## Controlling keyboard and mouse with GUI automation


import pyautogui
import mouseinfo
import pygetwindow as gw

# screen reso ----------------
wh = pyautogui.size()
wh
wh[0]
wh.width

# moving the mouse ---------------
for i in range(3):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# move relative to current posiition
for i in range(3):
    pyautogui.move(100, 0, duration=0.25)  # moves right
    pyautogui.move(0, 100, duration=0.25)  # moves down
    pyautogui.move(-100, 0, duration=0.25)  # negative opposite - left
    pyautogui.move(0, -100, duration=0.25)  # negative opposite - up

# get mouse position
pyautogui.position()
pyautogui.position()[0]
pyautogui.position().x

# move to position and click
pyautogui.click(10, 5) # Move mouse to (10, 5) and click.

# scroll mouse
pyautogui.scroll(200)

# plan mouse movement
mouseinfo.MouseInfoWindow()
# pyautogui.mouseInfo()

# get screenshot
pyautogui.screenshot()

# get pixel colours to check for consistency before clicking on mouse
pyautogui.pixel(0, 0)
pyautogui.pixel(50,200)

# match pixel colours
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

# image recognition
b = pyautogui.locateOnScreen('../data/bookmark_star.png')
b

# locate all images
list(pyautogui.locateAllOnScreen('../data/bookmark_star.png'))

# click on image
try:
    location = pyautogui.locateOnScreen('../data/bookmark_star.png')
except:
    print('Image could not be found.')

pyautogui.click(location)  # or enter the coordinates


# get active window ------------------------------------------------------------

fw = gw.getActiveWindow()
fw
# str(fw)
fw.title
fw.size
fw.left, fw.top, fw.right, fw.bottom
fw.topleft
fw.area
pyautogui.click(fw.left + 10, fw.top + 20)

# other ways of obtaining windows
# pyautogui.getAllWindows()
# pyautogui.getWindowsAt(x, y)
# pyautogui.getWindowsWithTitle(title) 
# pyautogui.getActiveWindow()

# manipulating window --------------------------------------------------------

fw = gw.getActiveWindow()
fw.width
fw.width = 2000  # resize
fw.topleft = (800,400)  # moves window

# other functions
# fw.isMaxmized
# fw.isMinmized
# fw.isActive
# fw.maximize()
# fw.restore()
# fw.minimize()
# fw.activate()
# fw.close()

# controlling keyboard --------------------------------------------------------

# keyboard key strings
pyautogui.KEYBOARD_KEYS

# write
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

# press down and release
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# hotkey combi - copy
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

# alternatively - press in order and release in reverse
pyautogui.hotkey('ctrl', 'c') 

# setting up gui automation scripts -------------------------------------------

# sleep
pyautogui.sleep(3)

# countdown
pyautogui.countdown(10)

print('Starting in ', end=''); pyautogui.countdown(3)

# display message boxes -------------------------------------------------------

# alert
pyautogui.alert('This is a message.', 'Important')
pyautogui.confirm('Do you want to continue?')
pyautogui.prompt("What is your cat's name?")
pyautogui.password('What is the password?')