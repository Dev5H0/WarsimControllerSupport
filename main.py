# Imports
import keyboard


# Variables
global i
i = 0
maxI = 99


# Function
def send():
    global i
    update()
    keyboard.send('enter')
    i = 0
    return

def update():
    global i
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.write(str(i))
    return

def increase():
    update()
    global i
    if not i >= maxI: i += 1
    return

def decrease():
    update()
    global i
    if not i <= 0: i -= 1
    return

def increaseTen():
    update()
    global i    
    if i >= maxI-10: i = maxI
    else: i += 10
    return

def decreaseTen():
    update()
    global i
    if i < 10: i = 0
    else: i -= 10
    return


# Hotkeys
keyboard.register_hotkey('up', increase)
keyboard.register_hotkey('down', decrease)
keyboard.register_hotkey('left', increaseTen)
keyboard.register_hotkey('right', decreaseTen)
keyboard.register_hotkey('space', send)


# -
def main():
    if keyboard.is_pressed('enter'):
        i = 0
    
    elif keyboard.is_pressed('backspace'):
        i = 0
        

