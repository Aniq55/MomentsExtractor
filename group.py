'''
Author: Github/@Aniq55
'''

import numpy as np


TOTAL_FRAMES= 38599
WIDTH= 200
THRESHOLD= 80


#############
## MARKING ##
#############

x= np.zeros(TOTAL_FRAMES)

file= open("meta.txt", "r")
for line in file:
	x1,x2= map(int, line.split('--'))
	for t in range(x1,x2+1):
		x[t]=1


##############
## GROUPING ##
##############

x2= np.zeros(TOTAL_FRAMES)

for t in range(TOTAL_FRAMES - WIDTH):
	intensity= np.sum(x[t:t+WIDTH])
	if intensity>THRESHOLD:
		x2[t:t+WIDTH]= 0.5


###################
## VISUALIZATION ##
###################

# import matplotlib.pyplot as plt
# plt.hold(True)
# plt.stem(list(range(TOTAL_FRAMES)), x, 'red')
# plt.stem(list(range(TOTAL_FRAMES)), x2)


############
## LIMITS ##
############

prev= x2[0]
MARK_BEGIN= []
MARK_END= []

for this_frame in range(1, TOTAL_FRAMES):
	if prev== 0 and x2[this_frame]== 0.5:
		MARK_BEGIN.append(this_frame)
	if prev==0.5 and x2[this_frame]== 0:
		MARK_END.append(this_frame)
	prev= x2[this_frame]


###############
## EXPANSION ##
###############

t_begin=[]
t_end= []
samples= len(MARK_END)
for j in range(samples):
	t_begin.append(MARK_BEGIN[j]/25 +5)
	t_end.append(MARK_END[j]/25 + 20)


#############
## MERGING ##
#############

j=1
L=0
while j< samples- L-1:
	if t_begin[j]< t_end[j-1]+5:
		del(t_begin[j])
		del(t_end[j-1])
		L=1
	j=j+1


############
## OUTPUT ##
############

file2= open("output.txt", "w")
samples= len(MARK_END)
for j in range(samples-L-1):
	a= t_begin[j]
	b= t_end[j]
	s_a= int(a%60)
	s_b= int(b%60)
	x= "%02d:%02d - %02d:%02d \n" %(a/60,s_a, b/60,s_b)	
	file2.write(x)
