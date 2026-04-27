import random
import matplotlib.pyplot as plt

x = 0
loc = []

for i in range(1000):
    x+=-1 if random.random() < 0.5 else +1
    loc.append(x)

plt.plot(loc)
plt.xlabel('Step')
plt.ylabel('Position')
plt.title('1D Random Walk (Single Person)')
plt.show()