import matplotlib.pyplot as plt
import numpy as np


file= open("meta.txt", "r")
TOTAL_FRAMES= 38599
WIDTH= 200
THRESHOLD= 80

x= np.zeros(TOTAL_FRAMES)

for line in file:
	x1,x2= map(int, line.split('--'))
	for t in range(x1,x2+1):
		x[t]=1

plt.stem(list(range(TOTAL_FRAMES)), x, 'red')
# plt.show()

plt.hold(True)

x2= np.zeros(TOTAL_FRAMES)

for t in range(TOTAL_FRAMES - WIDTH):
	intensity= np.sum(x[t:t+WIDTH])
	if intensity>THRESHOLD:
		x2[t:t+WIDTH]= 0.5

plt.stem(list(range(TOTAL_FRAMES)), x2)

plt.show()