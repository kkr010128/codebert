import math

data =map(float, raw_input().split(" "))

dx = data[2] - data[0]
dy = data[3] - data[1]

print math.sqrt(dx**2+dy**2)