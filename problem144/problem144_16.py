A, B, H, M = list(map(int, input().split()))

m = 360/60 * M
h = 360/12 * (H + M/60)
deg = abs(h-m)
if deg>180: deg = 360-deg

import math

Csq = A**2 + B**2 - 2*A*B*math.cos(math.radians(deg))
print('{:.10f}'.format(math.sqrt(Csq)))

