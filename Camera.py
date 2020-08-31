# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class Camera:
    def __init__(self,fps,width,height):
        self.fps = fps
        self.width = width
        self.height = height
        self.initialize()
    
    def __del__(self):
        return
    
    def initialize(self):
        self.camera = PiCamera()
        self.camera.resolution = (self.width, self.height)
        self.camera.framerate = self.fps
        self.rawCapture = PiRGBArray(self.camera, size=(self.width, self.height))
        # allow the camera to warmup
        time.sleep(0.1)

    def captureImage(self):
        self.rawCapture.truncate(0)
        self.camera.capture(self.rawCapture, format="bgr")
        image = self.rawCapture.array
        return image

    def storeImage(self,fileName):
        cv2.imwrite(fileName,self.captureImage())