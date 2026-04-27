import random
import matplotlib.pyplot as plt
import math

sumdist = [0] * 1000

for j in range(500):
    x = 0
    for i in range(1000):
        x += 1 if random.random() < 0.5 else -1
        sumdist[i] += abs(x)

avg = [d / 500 for d in sumdist]

steps = range(1000)
root_n = [math.sqrt(n) for n in steps]

plt.plot(steps, avg, label='Average distance')
plt.plot(steps, root_n, label='sqrt(N)')
plt.xlabel('Step')
plt.ylabel('Distance from origin')
plt.title('Random Walk: Average Distance vs √N')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()