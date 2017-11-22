"""
	Setting camera with raspberry pi by using opencv
	opencv is open source image processing library
"""

"""
	for first time use connect vga camera to raspberry pi
	and perform following scripts in terminal

	for accessing configuration

	$sudo raspi-config
	enable camera in pop up setting

	to test the camera use following code
	$raspistill -o output.jpg
	if jpg comes then it is working perfectly

	accessing by using python
	$source ~/.profile
	$workon cv
	$pip install "picamera[array]"
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#initialise the camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)

camera.capture(rawCapturem format="bgr")
image = rawCapture.array

#display image on screen and wait for keypress
cv2.imshow("Image", image)
cv2.waitKey(0)