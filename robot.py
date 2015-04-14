import RPi.GPIO as GPIO
import time
import metroGPIO as io
import os

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
#This function must be called if using Metropolia IO board
io.initMetroPins()
def QuitIt():
	sys.exit()
# Turn all out put pins off
clearPins()
def action(key):
    global delay
    if key == 'w':
        print ("Forward")
        GPIO.output(io.OUT2, True)
        GPIO.output(io.OUT3, True)
        time.sleep(delay)
        GPIO.output(io.OUT2, False)
        GPIO.output(io.OUT3, False)

    if key == 's':
        print ("Reverse")
        GPIO.output(io.OUT4, True)
        GPIO.output(io.OUT1, True)
        time.sleep(delay)
        GPIO.output(io.OUT4, False)
        GPIO.output(io.OUT1, False)

    if key == 'a':
        print ("Left Pivot")
        GPIO.output(io.OUT2, True)
        GPIO.output(io.OUT4, True)
        time.sleep(delay)
        GPIO.output(io.OUT2, False)
        GPIO.output(io.OUT4, False)

    if key == 'd':
        print ("Right Pivot")
        GPIO.output(io.OUT3, True)
        GPIO.output(io.OUT1, True)
        time.sleep(delay)
        GPIO.output(io.OUT3, False)
        GPIO.output(io.OUT1, False)

    if key == 'l':
        delay = delay + 0.1
        print ("Delay Up: " + str(delay))

    if key == 'k':
        delay = delay - 0.1
        print ("Delay Dw: " + str(delay))

    if key == 'q':
        print ("Quit")
        QuitIt()

delay = 0.2

getch = _Getch()

try:
## Test the output: Change the while condition if you want to run this
    while True:
       action(getch())

#The GPIO.cleanup() function should be called at the end of your code always when using GPIO pins
except KeyboardInterrupt:
	pass

GPIO.cleanup()
print("Program has exited successfully!")

#end file


