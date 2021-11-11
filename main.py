# Imports
import keyboard
from sys import exit

# Variables
global i
i = 0
maxI = 999999


# Function
def send():
    global i
    update()
    keyboard.send('enter')
    reset()
    return

def reset():
    global i
    i = 0
    update()    

def _backspace():
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')
    keyboard.send('backspace')

def update():
    global i
    _backspace()
    keyboard.write(str(i))
    return

def increase():
    global i
    if not i >= maxI: i += 1
    update()
    return

def decrease():
    global i
    if not i <= 0: i -= 1
    update()
    return

def increaseTen():
    global i    
    if i >= maxI-10: i = maxI
    else: i += 10
    update()
    return

def decreaseTen():
    global i
    if i <= 10: reset()
    else: i -= 10
    update()
    return

def increaseHundred():
    global i
    if i >= maxI-100: i = maxI
    else: i += 100
    update()
    return

def decreaseHundred():
    global i
    if i <= 100: reset()
    else: i -= 100
    update()
    return


# Hotkeys
keyboard.register_hotkey('e', increase)
keyboard.register_hotkey('q', decrease)
keyboard.register_hotkey('d', increaseTen)
keyboard.register_hotkey('a', decreaseTen)
keyboard.register_hotkey('w', increaseHundred)
keyboard.register_hotkey('s', decreaseHundred)
keyboard.register_hotkey('space', send)
keyboard.register_hotkey('backspace', reset)
keyboard.register_hotkey('escape', exit)


# -
def main():
    print(i)


while True: main()
        

