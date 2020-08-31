from Vehicle.Vehicle import Vehicle
from Camera import Camera
from time import sleep
from datetime import datetime
import os
import sys

def createDir():
    mydir = os.path.join(
        os.getcwd(), 'data',
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(mydir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    return mydir

def scrap():
    print ("Starting Vehicle Navigation")
    camera = Camera(25,640,432)
    camera.storeImage("out.jpg")
    vehicle = Vehicle()
    print ("Moving forward")
    vehicle.forward()
    sleep(1)
    print ("Reversing..")
    vehicle.reverse()
    sleep(1)


def moveForwardAndCaptureImages(direction,steps):
    vehicle = Vehicle()
    camera = Camera(25,1920,1088)
    try:
        mydir = createDir()
    except Exception as exp:
        print("Error in creating directory")
        return
    counter=0
    fileNameFormat = "{:03d}"
    
    while(counter < steps):
        try:
            counter += 1
            if (direction == "forward"):
                vehicle.forward(0.02)
            else:
                vehicle.reverse(0.02)
            filename = os.path.join(mydir, fileNameFormat.format(counter) + ".png")
            camera.storeImage(filename)
        except KeyboardInterrupt:
            print("Stopping the vehicle and camera capture")
            vehicle.stop()
            sleep(1)
            sys.exit(0)
    vehicle.stop()


if __name__ == "__main__":
    steps = 1
    direction = "forward"
    try:
        direction = sys.argv[1]
        steps = int(sys.argv[2])
    except:
        print("Exception occurred in parsing args")
        pass
    print ("Direction: " + direction  + ", Steps: " + str(steps))
    moveForwardAndCaptureImages(direction,steps)
