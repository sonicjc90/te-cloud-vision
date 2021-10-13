# te-cloud-vision
Google Cloud Vision API example for the Raspberry Pi. Used in Code Next's Team Edge program, Term 3.

This program uses the Google Cloud Vision AI API to return the object that has the highest confidence score based on a camera input frame (.png)
Run the code in Thonny on the Raspberry Pi with a Camera module attached.

Public users will have to set up their own service accounts and generate their own private keys with [Google Cloud Vision API](https://cloud.google.com/vision/docs/setup). 

Raspberry Pi users must also install OpenCV to connect to a PiCamera. Follow [this guide](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) to install all the dependencies and set up a Raspberry Pi. 
