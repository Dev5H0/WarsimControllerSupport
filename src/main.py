# Imports
from keyboard import send as keyboard_send, write as keyboard_write, register_hotkey as keyboard_register_hotkey, is_pressed as keyboard_is_pressed
from sys import exit as sys_exit


# Variables
global i
i = 0
minI = 0
maxI = 999999
incMain = 1
incA = 10
incB = 10
currentInc = incA
_currentInc = 'incA'
incrementer = 5
incrementerB = 20
timeoutInc = 0.1
timeoutEnter = 1
incText = 'incrementerA'

# Classes
class controls:
    send = None



# Function
def send():
    global i
    update()
    _backspace()
    keyboard_write(f'{i}')
    keyboard_send('enter')
    reset()
    update()
    return

def reset():
    global i
    i = minI
    update()
    return

def check():
    global i
    if i >= maxI-incB: i = maxI 


def _backspace():
    for _ in range(len(str(i))):
        keyboard_send('backspace')
    for _ in range(len(str(incText))):
        keyboard_send('backspace')
    for _ in range(len(str(currentInc))):
        keyboard_send('backspace')
        for _ in range(6):
            keyboard_send('backspace')
    return

def update():
    global i, temp
    _backspace()
    keyboard_write(f'{i}; {incText}:{currentInc}')
    if i >= maxI: i = maxI
    return

def increaseMain():
    global i
    if not i >= maxI: i += incMain
    update()
    return

def decreaseMain():
    global i
    if not i <= 0: i -= incMain
    update()
    return

def increaseSecondary():
    global i
    if i >= maxI-currentInc: i = currentInc
    else: i += currentInc
    update()
    return

def decreaseSecondary():
    global i
    if i <= currentInc: reset()
    else: i -= currentInc
    update()
    return

def increaseInc():
    global currentInc
    currentInc += incrementer
    update()
    return 

def decreaseInc():
    global currentInc
    if currentInc <= incrementer: currentInc = incrementer
    else: currentInc -= incrementer
    update()
    return 

def switchInc():
    global _currentInc, currentInc, incText, incA, incB
    if _currentInc == 'incA': 
        incA = currentInc
        incText = 'incrementerB'
        currentInc = incB
        _currentInc = 'incB'
    elif _currentInc == 'incB': 
        incB = currentInc
        incText = 'incrementerA'
        currentInc = incA
        _currentInc = 'incA'
    update()
    return

# Hotkeys
spaceTime = timeoutEnter
keyboard_register_hotkey('e', increaseMain, suppress=timeoutInc)
keyboard_register_hotkey('q', decreaseMain, suppress=timeoutInc)
keyboard_register_hotkey('d', increaseSecondary, suppress=timeoutInc)
keyboard_register_hotkey('a', decreaseSecondary, suppress=timeoutInc)
keyboard_register_hotkey('w', increaseInc, suppress=timeoutInc)
keyboard_register_hotkey('s', decreaseInc, suppress=timeoutInc)
keyboard_register_hotkey('r', switchInc)
keyboard_register_hotkey('space', send, suppress=spaceTime) # He he he 
keyboard_register_hotkey('backspace', reset, suppress=spaceTime) # He he he he he he he hello (world)


# -
def main():
    while True: 
            print(f'Current Value: {i}; Current Incrementer: {_currentInc},{currentInc}')
            if keyboard_is_pressed('escape'): sys_exit()


from sys import platform as sys_platform
if sys_platform == 'win32':
    try:
        from win32event import CreateMutex as win32event_CreateMutex
        from win32api import GetLastError as win32api_GetLastError
        from winerror import ERROR_ALREADY_EXISTS as winerror_ERROR_ALREADY_EXISTS
        win32event_CreateMutex(None, 1, 'mutex')
        if win32api_GetLastError() == winerror_ERROR_ALREADY_EXISTS: sys_exit()
        else: main()
    except: pass
elif sys_platform == ('linux' or 'linux2'): 
    try: 
        from pidfile import PIDFile as pidfile_PIDFile, AlreadyRunningError as pidfile_AlreadyRunningError
        try: 
            with pidfile_PIDFile(): main()
        except pidfile_AlreadyRunningError: pass
    except: pass
else: main()
