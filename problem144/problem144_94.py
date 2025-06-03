import math
A, B, H, M = map(int, input().split())

wa = 360/12
wb = 360/1
t = H + M/60
theta = math.radians((wa*t)%360 - (wb*t)%360)
print(math.sqrt(A**2 + B**2 -2*A*B*math.cos(theta)))