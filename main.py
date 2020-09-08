import random
import math 
import matplotlib.pyplot as plt

points_in = 0
total_points = 0
x_in = []
y_in = []
x_out = []
y_out = []

for i in range(10000000): #choose number of iterations  

    x = random.uniform(-1, 1) #generate x coordinate
    y = random.uniform(-1, 1) #generate y coordinate

    dist = math.sqrt(pow(x, 2) + pow(y, 2)) #get the distance from the origin

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

# square_area = (2*r)^2
# circle_area = pi*r^2

pi = 4* (points_in / total_points) #get the pi value by the areas relation
print(pi)

