#! Python3.9
# Imports
from keyboard import send as keyboard_send, write as keyboard_write, register_hotkey as keyboard_register_hotkey
from os import system as os_system
from sys import platform as sys_platform, exit as sys_exit

# Variables
running = True
global i
i = 0
minI = 0
maxI = 999999
incAmount = 1
timeoutInc = 0.3
timeoutEnter = 1

# Classes
class controls:
	sendValue = 'space'
	increaseValue = 'e'
	decreaseValue = 'q'

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

def _backspace():
	for _ in range(len(str(i))):
		keyboard_send('backspace')
	keyboard_send('backspace')
	keyboard_send('backspace')
	return

def update():
	global i, temp
	_backspace()
	keyboard_write(f'{i}')
	if i >= maxI: i = maxI
	return

def increase():
	global i
	if not i >= maxI: i += incAmount
	update()
	return

def decrease():
	global i
	if not i <= 0: i -= incAmount
	update()
	return


# Hotkeys
spaceTime = timeoutEnter
keyboard_register_hotkey(controls.increaseValue, increase, suppress=timeoutInc)
keyboard_register_hotkey(controls.decreaseValue, decrease, suppress=timeoutInc)
keyboard_register_hotkey(controls.sendValue, send, suppress=spaceTime) # He he he
keyboard_register_hotkey('escape', close) # Once the "escape" key is pressed, stops the application completely.


# -
if sys_platform == 'win32':
	clearCommand = 'cls'
elif sys_platform != 'win32':
	clearCommand = 'clear'

while running:
	print(f'Current Value: {i}')
