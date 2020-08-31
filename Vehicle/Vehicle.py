import RPi.GPIO as GPIO
from time import sleep
from RelayControlledVehicle import RelayControlledVehicle

class Vehicle:
    def __init__(self):
        self.name = "Vehicle"
        self.vehicle = None
        self.initialize()

    def __del__(self):
        self.cleanup()
    
    def initialize(self):
        self.vehicleType = "RelayControlled" #Read from config and set tis
        
        if self.vehicleType == "RelayControlled":
            self.vehicle = RelayControlledVehicle()
        else:
            return
    
    def forward(self,duration=100):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.forward(duration)

    def reverse(self,duration=0):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.reverse(duration)
    
    def turnRight(self,duration):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.turnRight(duration)

    def turnLeft(self,duration):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.turnLeft(duration)
    
    def reverseLeft(self,duration):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.reverseLeft(duration)

    def reverseRight(self,duration):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.reverseRight(duration)
    
    def stop(self):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.stop()

    def cleanup(self):
        if self.vehicle == None:
            print("Vehicle not initialized")
            return
        self.vehicle.cleanup()
