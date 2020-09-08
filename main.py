import random
import math 
import matplotlib.pyplot as plt

points_in = 0
total_points = 0
x_in = []
y_in = []
x_out = []
y_out = []

for i in range(10000000):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)


    dist = math.sqrt(pow(x, 2) + pow(y, 2))

    total_points += 1
    if dist <= 1:
        points_in += 1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)

plt.plot(x_in, y_in, 'ro')
plt.plot(x_out, y_out, 'bo')
plt.axis([-1, 1, -1, 1])
plt.show()

pi = 4* (points_in / total_points)
print(pi)

