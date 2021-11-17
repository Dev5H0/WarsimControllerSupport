# Imports
from keyboard import send as keyboard_send, write as keyboard_write, register_hotkey as keyboard_register_hotkey, is_pressed as keyboard_is_pressed
from configparser import  ConfigParser as configparser_ConfigParser
#from threading import Timer as threading_Timer
from os import system as os_system
from sys import platform as sys_platform, exit as sys_exit


# Variables
running = True
global i
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


# Functions
def close():
    global running
    running = False
    sys_exit()

def clear():
    os_system(clearCommand)

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
    currentInc += incrementerAmount
    update()
    return 

def decreaseInc():
    global currentInc
    if currentInc <= incrementerAmount: currentInc = incrementerAmount
    else: currentInc -= incrementerAmount
    update()
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
spaceTime = timeoutEnter
keyboard_register_hotkey(controls.increaseValue, increaseMain, suppress=timeoutInc)
keyboard_register_hotkey(controls.decreaseValue, decreaseMain, suppress=timeoutInc)
keyboard_register_hotkey(controls.increaseValueInc, increaseSecondary, suppress=timeoutInc)
keyboard_register_hotkey(controls.decreaseValueInc, decreaseSecondary, suppress=timeoutInc)
keyboard_register_hotkey(controls.increaseIncrementer, increaseInc, suppress=timeoutInc)
keyboard_register_hotkey(controls.decreaseIncrementer, decreaseInc, suppress=timeoutInc)
keyboard_register_hotkey(controls.switchIncrementer, switchInc)
keyboard_register_hotkey(controls.sendValue, send, suppress=spaceTime) # He he he 
keyboard_register_hotkey(controls.resetValue, reset, suppress=spaceTime) # He he he he he he he hello (world)
keyboard_register_hotkey('escape', close) # Once the "escape" key is pressed, stops the application completely. 


# -
if sys_platform == 'win32':
    clearCommand = 'cls'
elif sys_platform == ('linux' or 'linux2'): 
    clearCommand = 'clear'

def main():
    global running
#    threading_Timer(0.1, main).start()
    clear()
    print(f'Current Value: {i}; Current Incrementer: {currentIncText},{currentInc}')

main()