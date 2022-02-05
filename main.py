# Imports
from keyboard import send as keyboard_send, write as keyboard_write, register_hotkey as keyboard_register_hotkey
from os import system as os_system
from sys import platform as sys_platform, exit as sys_exit
running:bool = True

# Classes
class value:
	current:int = 0
	min:int = 0
	max:int = 999999
	increase:int = 1

class timeout:
	increment:float = 0.3
	send:float = 1

class controls:
	value_send = 'space'
	value_increase = 'e'
	value_decrease = 'q'

# Functions
def close():
	global running
	running = False
	sys_exit()

def clear():
	os_system(clear_command)

def send():
	update()
	_backspace()
	keyboard_write(f'{value.current}')
	keyboard_send('enter')
	reset()
	update()
	return

def reset():
	value.current = value.min
	update()
	return

def _backspace():
	for _ in range(len(str(value.current))): keyboard_send('backspace')
	keyboard_send('backspace') # Just in case.
	return

def update():
	_backspace()
	keyboard_write(f'{value.current}')
	if value.current >= value.max: value.current = value.max
	return

def increase():
	if not value.current >= value.max: value.current += value.increase
	update()
	return

def decrease():
	if not value.current <= 0: value.current -= value.increase
	update()
	return


# Hotkeys
keyboard_register_hotkey(controls.value_increase, increase, suppress=timeout.increment) # If key assinged to 'value_increase' is pressed, call function 'increase'.
keyboard_register_hotkey(controls.value_decrease, decrease, suppress=timeout.increment) # If key assinged to 'value_decrease' is pressed, call function 'decrease'.
keyboard_register_hotkey(controls.value_send, send, suppress=timeout.send) # If key assinged to 'value_send' is pressed, call function 'send'.
keyboard_register_hotkey('escape', close) # If key "escape" is pressed, stops the application.


# -
if sys_platform == 'win32': clear_command = 'cls' # If the currently running operating system is Windows, the text 'cls' will be assinged the variable 'clear_command', otherwise the text 'clear' will be assigned.
elif sys_platform != 'win32': clear_command = 'clear'

while running: print(f'Current Value: {value.current}') # Running "pass" slows the program down immensly. :/
