import RPi.GPIO as GPIO
from time import sleep

class Motors:
    def __init__(self, Lpin1, Lpin2, Lpin3, Lpin4, Rpin1, Rpin2, Rpin3, Rpin4):
        self.Lpin1 = Lpin1
        self.Lpin2 = Lpin2
        self.Lpin3 = Lpin3
        self.Lpin4 = Lpin4
        
        self.Rpin1 = Rpin1
        self.Rpin2 = Rpin2
        self.Rpin3 = Rpin3
        self.Rpin4 = Rpin4
              
        self.state = 0 # 0 = stopped, 1 = backward , 2 = backward, 3 = clockwise, 4 = counter-clockwise
        
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(Lpin1, GPIO.OUT)
        GPIO.setup(Lpin2, GPIO.OUT)
        GPIO.setup(Lpin3, GPIO.OUT)
        GPIO.setup(Lpin4, GPIO.OUT)
        
        GPIO.setup(Rpin1, GPIO.OUT)
        GPIO.setup(Rpin2, GPIO.OUT)
        GPIO.setup(Rpin3, GPIO.OUT)
        GPIO.setup(Rpin4, GPIO.OUT)
        
        self.coil1(0)
        self.coil2(0)
        self.coil3(0)
        self.coil4(0)
    
    def coil1(self, state): # left
        if state == 1:
            GPIO.output(self.Lpin2, GPIO.LOW)
            GPIO.output(self.Lpin1, GPIO.HIGH)
        else:
            GPIO.output(self.Lpin1, GPIO.LOW)
            GPIO.output(self.Lpin2, GPIO.HIGH)
    
    def coil2(self, state):
        if state == 1:
            GPIO.output(self.Lpin4, GPIO.LOW)
            GPIO.output(self.Lpin3, GPIO.HIGH)
        else:
            GPIO.output(self.Lpin3, GPIO.LOW)
            GPIO.output(self.Lpin4, GPIO.HIGH)
            
    def coil3(self, state): # right
        if state == 1:
            GPIO.output(self.Rpin2, GPIO.LOW)
            GPIO.output(self.Rpin1, GPIO.HIGH)
        else:
            GPIO.output(self.Rpin1, GPIO.LOW)
            GPIO.output(self.Rpin2, GPIO.HIGH)
    
    def coil4(self, state):
        if state == 1:
            GPIO.output(self.Rpin4, GPIO.LOW)
            GPIO.output(self.Rpin3, GPIO.HIGH)
        else:
            GPIO.output(self.Rpin3, GPIO.LOW)
            GPIO.output(self.Rpin4, GPIO.HIGH)
        
    def move(self, direction, speed):
        if direction == 2:
            self.coil1(1)
            self.coil2(0)
            self.coil3(1)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(1)
            self.coil2(1)
            self.coil3(0)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(1)
            self.coil3(0)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(0)
            self.coil3(1)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            
        elif direction == 1:
            self.coil1(1)
            self.coil2(0)
            self.coil3(1)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(0)
            self.coil3(1)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(1)
            self.coil3(0)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(1)
            self.coil2(1)
            self.coil3(0)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            
        elif direction == 3:
            self.coil1(1)
            self.coil2(0)
            self.coil3(1)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(1)
            self.coil2(1)
            self.coil3(1)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(1)
            self.coil3(0)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(0)
            self.coil3(0)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            
        elif direction == 4:
            self.coil1(1)
            self.coil2(0)
            self.coil3(1)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(0)
            self.coil3(0)
            self.coil4(0)
            sleep(1.050 - abs(speed))
            self.coil1(0)
            self.coil2(1)
            self.coil3(0)
            self.coil4(1)
            sleep(1.050 - abs(speed))
            self.coil1(1)
            self.coil2(1)
            self.coil3(1)
            self.coil4(1)
            sleep(1.050 - abs(speed))
        
        else:
            self.coil1(0)
            self.coil2(0)
            self.coil3(0)
            self.coil4(0)

            
        self.state = direction
        
motors = Motors(11, 12, 13, 15, 16, 18, 22, 7)

while True:
    motors.move(1, 1)