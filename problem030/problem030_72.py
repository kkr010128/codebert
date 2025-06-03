import math
data = list(map(float, input().split()))
a, b, theta = data[0], data[1], data[2]/180*math.pi
data[1] = (a**2+b**2-2*a*b*math.cos(theta)) ** 0.5 + a + b
data[2] = b * math.sin(theta)
data[0] = a * data[2] / 2
for i in range(3):
    print(data[i])

