import matplotlib.pyplot as plt
file= open("output.txt", "r")

for line in file:
	x1,x2= map(int, line.split('--'))
	plt.stem(list(range(x1,x2)),[1]*(x2-x1))

plt.show()