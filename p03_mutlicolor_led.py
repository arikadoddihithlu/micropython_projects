
import machine
import os
import time

def multicolor():
    blue = machine.Pin(10, machine.Pin.OUT)
    red = machine.Pin(11, machine.Pin.OUT)
    green = machine.Pin(9, machine.Pin.OUT)
    sleeptime=1
    for x in range(2):
       blue.value(x)
       time.sleep(sleeptime)
       for y in range(2):
           red.value(y)
           time.sleep(sleeptime)
           for z in range(2):
             green.value(z)
             time.sleep(sleeptime)
       
    
        


    