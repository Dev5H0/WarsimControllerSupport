# Imports
import keyboard
from sys import exit

# Variables
global i
i = 0
defI = 0
maxI = 999999
incA = 1
incB = 10
incC = 100
timeoutInc = 0.1
timeoutEnter = 1
# Function
def send():
    global i
    update()
    keyboard.send('enter')
    reset()
    return

def reset():
    global i
    i = defI
    update()
    return

def _backspace():
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    return

def update():
    global i
    _backspace()
    keyboard.write(str(i))
    return

def increase():
    global i
    if not i >= maxI: i += incA
    update()
    return

def decrease():
    global i
    if not i <= 0: i -= incA
    update()
    return

def increaseTen():
    global i    
    if i >= maxI-incB: i = incB
    else: i += incB
    update()
    return

def decreaseTen():
    global i
    if i <= incB: reset()
    else: i -= incB
    update()
    return

def increaseHundred():
    global i
    if i >= maxI-incC: i = maxI
    else: i += incC
    update()
    return

def decreaseHundred():
    global i
    if i <= incC: reset()
    else: i -= incC
    update()
    return


# Hotkeys
spaceTime = timeoutEnter
keyboard.register_hotkey('e', increase, suppress=timeoutInc)
keyboard.register_hotkey('q', decrease, suppress=timeoutInc)
keyboard.register_hotkey('d', increaseTen, suppress=timeoutInc)
keyboard.register_hotkey('a', decreaseTen, suppress=timeoutInc)
keyboard.register_hotkey('w', increaseHundred, suppress=timeoutInc)
keyboard.register_hotkey('s', decreaseHundred, suppress=timeoutInc)
keyboard.register_hotkey('space', send, suppress=spaceTime) # He he he 
keyboard.register_hotkey('backspace', reset, suppress=spaceTime) # He he he he he he he hello (world)
keyboard.register_hotkey('escape', exit)


# -
while True: print(i)
