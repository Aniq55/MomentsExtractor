import numpy as np
import cv2

vid= cv2.VideoCapture('videos/05_05.mp4')

TOTAL_FRAMES= vid.get(7)
FPS= vid.get(5)

cascadeUpperBody = cv2.CascadeClassifier("cascades/haarcascade_upperbody.xml")

detect= []
np.array(detect, np.bool)

CURRENT_FRAME=0
while(vid.isOpened() and CURRENT_FRAME<TOTAL_FRAMES):
	ret, frame = vid.read()
	CURRENT_FRAME= vid.get(1)
	gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	bodies= cascadeUpperBody.detectMultiScale(gray)	
	c= len(bodies)
	if c>0:
		detect.append(True)
	else:
		detect.append(False)
	

# Analysis

# print(detect)
activityFrame= detect.index(True)+1
print activityFrame

# Grouping




vid.release()
cv2.destroyAllWindows()