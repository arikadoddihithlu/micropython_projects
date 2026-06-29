
import machine
import time

class trafficlights:
    def __init__(self):
        self.red = machine.Pin(10, machine.Pin.OUT)
        self.yellow = machine.Pin(11, machine.Pin.OUT)
        self.green = machine.Pin(9, machine.Pin.OUT)
        self.pedestrians=machine.Pin(12,machine.Pin.OUT)
        self.redtime=2
        self.yellowtime=1
        self.greentime=3

    def lightsequence(self):
        self.red.value(0)
        self.yellow.value(0)
        self.green.value(1)
        time.sleep(self.greentime)
        
        self.red.value(1)
        self.yellow.value(0)
        self.green.value(0)
        self.pedestrians.value(1)
        for x in range(self.redtime*5):
             if x%2==0:
                  self.pedestrians.value(1)
                  time.sleep(1/5.0)
             else:
                  self.pedestrians.value(0)
                  time.sleep(1/5.0)
             
#time.sleep(self.redtime)
    

        self.red.value(0)
        self.yellow.value(1)
        self.green.value(0)
        self.pedestrians.value(0)
        time.sleep(self.greentime)