"""
object_recognizer.py authored by Google Code Next
This program uses the Google Cloud Vision AI API to return the object that has the highest confidence score based on a camera input frame (.png)
Run the code in Thonny on the Raspberry Pi with a Camera module attached.
"""

import os, io
from google.cloud import vision
import cv2
from time import sleep
import pprint 


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GCVision.json' #the credetials to talk to the API.
client = vision.ImageAnnotatorClient()
print("starting object recognizer...")

object_to_find = 0

def get_object_from_cloud(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


def get_image_from_frame(cap):
    ret, frame = cap.read()
    file = 'frame.png'
    cv2.imwrite(file,frame)
    cv2.imshow('frame',frame) #show camera output
    return file

def start_camera():
    global object_to_find
    os.system('sudo modprobe bcm2835-v4l2') #Force the Raspberry Pi to use the the Picamera, which CV2 will need to capture each frame.

    cap = cv2.VideoCapture(0)
    print("Starting camera")

    while True:
        
        img = get_image_from_frame(cap)
        key = cv2.waitKey(0) #press 0 to move through frames
        object_to_find = get_object_from_cloud(img)

        print(object_to_find)

        if key == ord('q'): #press q to quit
            break
    
    cap.release() #release the object when the app quits.
    cv2.destroyAllWindows()


start_camera()
