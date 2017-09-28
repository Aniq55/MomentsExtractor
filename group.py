# import matplotlib.pyplot as plt
import numpy as np


TOTAL_FRAMES= 38599
WIDTH= 200
THRESHOLD= 80

x= np.zeros(TOTAL_FRAMES)

file= open("meta.txt", "r")
for line in file:
	x1,x2= map(int, line.split('--'))
	for t in range(x1,x2+1):
		x[t]=1


# plt.stem(list(range(TOTAL_FRAMES)), x, 'red')
# plt.hold(True)


x2= np.zeros(TOTAL_FRAMES)

for t in range(TOTAL_FRAMES - WIDTH):
	intensity= np.sum(x[t:t+WIDTH])
	if intensity>THRESHOLD:
		x2[t:t+WIDTH]= 0.5

# plt.stem(list(range(TOTAL_FRAMES)), x2)


x3=x2
for t in range(200,len(x2)-200):
	if x2[t]==0.5:
		x3[t-200:t]=0.25
		x3[t:t+200]=0.25

prev= x3[0]

MARK_BEGIN= []
MARK_END= []
for this_frame in range(1, TOTAL_FRAMES):
	if prev== 0 and x3[this_frame]== 0.25:
		MARK_BEGIN.append(this_frame)
	if prev==0.25 and x3[this_frame]== 0:
		MARK_END.append(this_frame)
	prev= x3[this_frame]


# plt.stem(list(range(TOTAL_FRAMES)), x3, 'red')


file2= open("output.txt", "w")

samples= len(MARK_END)
for j in range(samples):
	a= MARK_BEGIN[j]/25
	b= MARK_END[j]/25
	file2.write(str(int(a/60))+':'+str(int(a%60)) +' - '+ str(int(b/60))+':'+str(int(b%60)) +'\n')	
