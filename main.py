# Imports
import keyboard


# Variables
global i
i = 0
maxI = 999999


# Function
def send():
    global i
    update()
    keyboard.send('enter')
    i = 0
    return

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
    if i <= 10: i = 0
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
    if i <= 100: i = 0
    else: i -= 100
    update()
    return


# Hotkeys
keyboard.register_hotkey('w', increase)
keyboard.register_hotkey('s', decrease)
keyboard.register_hotkey('d', increaseTen)
keyboard.register_hotkey('a', decreaseTen)
keyboard.register_hotkey('e', increaseHundred)
keyboard.register_hotkey('q', decreaseHundred)
keyboard.register_hotkey('space', send)


# -
def main():
    global i
    print(i)
    if keyboard.is_pressed('enter'):
        i = 0
        update()
    
    elif keyboard.is_pressed('backspace'):
        i = 0
        update()

    elif keyboard.is_pressed('escape'):
        import sys
        sys.exit()


while True: main()
        

