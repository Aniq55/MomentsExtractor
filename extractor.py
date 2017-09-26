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
print activityFrame

prev= detect(0)

MARK_BEGIN= []
MARK_END= []
for this_frame in range(1, TOTAL_FRAMES):
	if prev=False and this_frame=True:
		MARK_BEGIN.append(this_frame)
	if prev= True and this_frame= False:
		MARK_END.append(this_frame)

print(MARK_BEGIN)
print(MARK_END)


# Grouping




vid.release()
cv2.destroyAllWindows()