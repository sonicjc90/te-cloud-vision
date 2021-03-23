#This Package is for Team Edge Term 3 

import os, io
from google.cloud import vision
import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import pprint 

#Add the Google Cloud Vision credentials to the environemnt.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GCVision.json'

#Declare the client object. 
client = vision.ImageAnnotatorClient()
object_to_id #leave empty for now 


def get_image_from_frame(cap):
    """
    Each frame will return a png file saved as 'frame'. 
    This file will be overwritten with each cycle.
    The code below is similar to the livestream app we built in Term 2.
    """
    ret, frame = cap.read()
    file = 'frame.png'
    cv2.imwrite(file,frame)
    cv2.imshow('frame',frame) #show camera output
    return file

def start_camera():
    """
    Start the camera. Make sure the Raspberry Pi recognizes the Picamera as the main interface for CV2.
    """
    os.system('sudo modprobe bcm2835-v4l2') 
    
    cap = cv2.VideoCapture(0) # Use the CV2 library's video capture function. 0 is the index of the main device camera.
    print("Starting camera")

    while True:
        
        img = get_image_from_frame(cap)
        key = cv2.waitKey(0) #press 0 to move through frames

        if key == ord('q'): #press q to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()
   
