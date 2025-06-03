import numpy as np
import math

a, b, h, m = map(int, input().split())
pi = np.pi

a_angle = (60*h+m)/720*2*pi
b_angle = (m/60)*2*pi

angle = a_angle - b_angle

ans = math.sqrt(a**2 + b**2 - 2*a*b*np.cos(angle))
print(ans)
