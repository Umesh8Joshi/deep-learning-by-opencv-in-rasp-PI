""" Object or dust detection with OpenCV
	identifying objects by assigining class
	at the end of execution data will predict
	class of object
"""

from imutil.video import VideoStream
from imutil.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

#constructing argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
				help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
				help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
				help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

CLASSES = ["dust", "pop-corn", "cat", "chair", "table","toy"]
COLOR = np.random.uniform(0,255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readdNetFromCaffe(args["prototxt"], args["model"])

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
 
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)
 
	# pass the blob through the network and obtain the detections and  predictions
	net.setInput(blob)
	detections = net.forward()

		cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
	# update the FPS counter
	fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()

"""
	test result

	$ python real_time_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel
[INFO] loading model...
[INFO] starting video stream...
[INFO] elapsed time: 54.70
[INFO] approx. FPS: 0.90

"""