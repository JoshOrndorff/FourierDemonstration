import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

number = int(raw_input("How many harmonics should I plot?  "))

amplitudes = []
for i in range(number):
	n = 2 * i + 1
	amplitudes.append(4 / (n * np.pi))
	
sum = np.zeros(x.size)

for i in range(number):
	n = 2 * i + 1
	currenty = amplitudes[i] * np.sin(n * x)
	plt.plot(x, currenty)
	sum += currenty

plt.plot(x, sum, 'k', label="sum")
plt.plot([0, 0, np.pi, np.pi, 2*np.pi, 2*np.pi], [0, 1, 1, -1, -1, 0], 'k--', label="square")
plt.legend()
plt.xlim([-.1, 6.4])

plt.show()