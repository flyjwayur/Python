import RPi.GPIO as GPIO
import metroGPIO as io
import os
import time
io.initMetroPins()
bits=[[False,False,False],[False,False,True],[False,True,False],[False,True,True],[True,False,False],[True,False,True],[True,True,False],[True,True,True]]
def L1(alist):
        return alist[0]or alist[1]or alist[2]
def L2(alist):
        return alist[0]or alist[1]
def L3(alist):
        return alist[0]or (alist[1]and alist[2])
def L4(alist):
        return alist[0]
def L5(alist):
        return (alist[0]and alist[1])or (alist[2]and alist[0])
def L6(alist):
        return alist[0]and alist[1]
def L7(alist):
        return alist[0]and alist[1]and alist[2]
def L8(alist):
        return not(alist[0]and alist[1]and alist[2])
def tester(biglist):
        for x in biglist:
                GPIO.output(io.OUT1,L1(x))
                GPIO.output(io.OUT2,L2(x))
                GPIO.output(io.OUT3,L3(x))
                GPIO.output(io.OUT4,L4(x))
                GPIO.output(io.OUT5,L5(x))
                GPIO.output(io.OUT6,L6(x))
                GPIO.output(io.OUT7,L7(x))
                GPIO.output(io.OUT8,L8(x))
                time.sleep(1)
tester(bits)
GPIO.cleanup()
	
            
