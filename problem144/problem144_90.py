import sys
import math
A,B,H,M = list(map(int, input().split()))


a = (H/12+M/720) * 360
b = M/60 * 360

a = a-b
if a > 180:
    a = 360 - a
    

c = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(math.radians(a))))
print(c)
