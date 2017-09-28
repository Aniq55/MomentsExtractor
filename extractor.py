import numpy as np
import cv2

vid= cv2.VideoCapture('videos/05_05.mp4')

TOTAL_FRAMES= int(vid.get(7)) #38599
# TOTAL_FRAMES= 5000
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


prev= detect[0]

MARK_BEGIN= []
MARK_END= []
for this_frame in range(1, TOTAL_FRAMES):
	if prev== False and detect[this_frame]== True:
		MARK_BEGIN.append(this_frame)
	if prev==True and detect[this_frame]== False:
		MARK_END.append(this_frame)
	prev= detect[this_frame]

# print(MARK_BEGIN)
# print(MARK_END)



file= open("meta.txt", "w")


THRESHOLD= 0

samples= len(MARK_END)
for j in range(samples):
	duration= MARK_END[j]-MARK_BEGIN[j]
	if duration> THRESHOLD:
		file.write(str(MARK_BEGIN[j])+' -- '+str(MARK_END[j])+'\n')	

file.close()

vid.release()
cv2.destroyAllWindows()