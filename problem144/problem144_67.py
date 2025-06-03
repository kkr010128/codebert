import math

A,B,H,M = map(int,input().split())
x = H*60+M
y = x/2
z = 6*M
a = abs(y-z)
if a > 180:
    a = 360 - a
c_2 = A**2 + B**2 - 2*A*B*(math.cos(math.radians(a)))
print(math.sqrt(c_2))
