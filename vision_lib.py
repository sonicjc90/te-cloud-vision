#This Package is for Team Edge Term 3 

import os, io
from google.cloud import vision
import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import pprint 


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GCVision.json'
client = vision.ImageAnnotatorClient()
object_to_id #leave empty for now 

def get_image_from_frame(cap):
    ret, frame = cap.read()
    file = 'frame.png'
    cv2.imwrite(file,frame)
    cv2.imshow('frame',frame) #show camera output
    return file

def start_camera():

    os.system('sudo modprobe bcm2835-v4l2') 

    cap = cv2.VideoCapture(0)
    print("Starting camera")

    while True:
        
        img = get_image_from_frame(cap)
        key = cv2.waitKey(0) #press 0 to move through frames

        if key == ord('q'): #press q to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    



print("vision library launched successfully")