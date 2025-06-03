import math
import numpy as np
pi = math.pi

a, b, x = map(int, input().split())
if x >= a**2*b/2:
    print(180/pi*np.arctan(2*(a**2*b-x)/a**3))
else:
    print(180/pi*np.arctan(a*b**2/(2*x)))