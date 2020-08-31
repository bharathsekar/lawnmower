import RPi.GPIO as GPIO
from time import sleep


class RelayControlledVehicle:
    def __init__(self):
        self.name = "RelayControlledVehicle"
        self.initialize()

    def __del__(self):
        self.cleanup()
    
    def initialize(self):
        self.forwardPin=22
        self.reversePin=23
        self.leftTurnPin=24
        self.rightTurnPin=25
        self.moveForwardPins = (self.forwardPin,self.rightTurnPin)
        self.moveReversePins = (self.reversePin,self.leftTurnPin)
        self.turnRightForwardPins = (self.forwardPin,self.rightTurnPin)
        self.turnLeftForwardPins = (self.forwardPin,self.leftTurnPin)
        self.turnRightReversePins = (self.reversePin,self.leftTurnPin)
        self.turnLeftReversePins = (self.reversePin,self.rightTurnPin)
        self.allPins = (self.forwardPin,self.reversePin,self.leftTurnPin,self.rightTurnPin)
        self.initializeGPIO()
        
    
    def initializeGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.forwardPin,GPIO.OUT)
        GPIO.setup(self.reversePin,GPIO.OUT)
        GPIO.setup(self.leftTurnPin,GPIO.OUT)
        GPIO.setup(self.rightTurnPin,GPIO.OUT)
    
    def forward(self,duration=100):
        self.stop()
        print("Moving relay controlled forward")
        GPIO.output(self.moveForwardPins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.moveForwardPins,GPIO.LOW)

    def reverse(self,duration=0):
        self.stop()
        GPIO.output(self.moveReversePins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.moveReversePins,GPIO.LOW)
    
    def turnRight(self,duration):
        self.stop()
        GPIO.output(self.turnRightForwardPins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.turnRightForwardPins,GPIO.LOW)

    def turnLeft(self,duration):
        self.stop()
        GPIO.output(self.turnLeftForwardPins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.turnLeftForwardPins,GPIO.LOW)
    
    def reverseLeft(self,duration):
        self.stop()
        GPIO.output(self.turnLeftReversePins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.turnLeftReversePins,GPIO.LOW)

    def reverseRight(self,duration):
        self.stop()
        GPIO.output(self.turnRightReversePins,GPIO.HIGH)
        if duration == None or duration <= 0:
            return
        sleep(duration)
        GPIO.output(self.turnRightReversePins,GPIO.LOW)
    
    def stop(self):
        GPIO.output(self.allPins,GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()