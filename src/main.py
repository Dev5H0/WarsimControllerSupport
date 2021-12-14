# Imports
from keyboard import send as keyboard_send, write as keyboard_write, register_hotkey as keyboard_register_hotkey, is_pressed as keyboard_is_pressed
from configparser import  ConfigParser as configparser_ConfigParser
from os import system as os_system
from sys import platform as sys_platform, exit as sys_exit


# Variables
global app_close,running,i,minI,maxI,incMain,incA,incB,incrementerAmount,currentInc,currentIncText,incText,timeoutInc,timeoutEnter
app_close = False
running = True
i = 0
minI = 0
maxI = 999999
incMain = 1
incA = 10
incB = 10
incrementerAmount = 5
currentInc = incA
currentIncText = 'incA'
incText = 'incrementerA'
timeoutInc = 0.1
timeoutEnter = 1


# Classes
class config:
    def __init__(self):
        self.parse = config.parse

    config = configparser_ConfigParser()
    config.read('./src/config.ini')
    cat = config['CONTROLS']
    def parse(keyword:str, cat=cat):
        return str(cat[keyword.lower()])

class controls:
    sendValue = config.parse('sendValue')
    resetValue = config.parse('resetValue')
    increaseValue = config.parse('increaseValue')
    decreaseValue = config.parse('decreaseValue')
    increaseValueInc = config.parse('increaseValueInc')
    decreaseValueInc = config.parse('decreaseValueInc')
    incrementerAmount = (config.parse('incrementerAmount'))
    switchIncrementer = config.parse('switchIncrementer')
    resetIncrementer = config.parse('resetIncrementer')
    increaseIncrementer = config.parse('increaseIncrementer')
    decreaseIncrementer = config.parse('decreaseIncrementer')
    pause = config.parse('pause')
    close = config.parse('quit')

# Functions
def online(func:function):
    if running == True: func()
    return 

def pause():
    global running
    if running == True: running = False
    elif running == False: running = True
    return 

def close():
    global app_close
    app_close = True
    sys_exit()

def clear():
    os_system(clearCommand)
    return 

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
    return 

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
    currentInc += incrementerAmount
    update()
    return 

def decreaseInc():
    global currentInc
    if currentInc <= incrementerAmount: currentInc = incrementerAmount
    else: currentInc -= incrementerAmount
    update()
    return 

def resetInc():
    global currentInc
    currentInc = incrementerAmount
    return 


def switchInc():
    global currentIncText, currentInc, incText, incA, incB
    if currentIncText == 'incA':
        incA = currentInc
        incText = 'incrementerB'
        currentInc = incB
        currentIncText = 'incB'
    elif currentIncText == 'incB':
        incB = currentInc
        incText = 'incrementerA'
        currentInc = incA
        currentIncText = 'incA'
    update()
    return

# Hotkeys
spaceTime = timeoutEnter # He he he(llo), spacetime. 
keyboard_register_hotkey(controls.increaseValue, online, (increaseMain), suppress=timeoutInc) # Increase value. 
keyboard_register_hotkey(controls.decreaseValue, online, (decreaseMain), suppress=timeoutInc) # Decrease value. 
keyboard_register_hotkey(controls.increaseValueInc, online, (increaseSecondary), suppress=timeoutInc) # Increase value by incrementer's value. 
keyboard_register_hotkey(controls.decreaseValueInc, online, (decreaseSecondary), suppress=timeoutInc) # Decrease value by incrementer's value. 
keyboard_register_hotkey(controls.increaseIncrementer, online, (increaseInc), suppress=timeoutInc) # Increase the current incrementer's value. 
keyboard_register_hotkey(controls.decreaseIncrementer, online, (decreaseInc), suppress=timeoutInc) # Decrease the current incrementer's value. 
keyboard_register_hotkey(controls.switchIncrementer, online, (switchInc)) # Switch the incrementer. 
keyboard_register_hotkey(controls.resetIncrementer, online, (reset)) # Reset the current incrementer's value. 
keyboard_register_hotkey(controls.sendValue, online, args=(send), suppress=spaceTime) # Send current value. 
keyboard_register_hotkey(controls.resetValue, online, args=(reset), suppress=spaceTime) # Reset value to zero. 
keyboard_register_hotkey(controls.pause, pause) # Pause the program. 
keyboard_register_hotkey(controls.close, close) # Quit the program. 


# -
if sys_platform == 'win32':
    clearCommand = 'cls'
elif sys_platform == ('linux' or 'linux2'):
    clearCommand = 'clear'

def main():
    global running
    print()
    print(f'Current Value: {i}; Current Incrementer: {currentIncText},{currentInc}')

while not app_close:
    if running:
        pass

close()
sys_exit()
