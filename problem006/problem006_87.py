import math

x,y = int(input()),100
for i in range(x):
    y = math.ceil(y*1.05)

print(y*1000)