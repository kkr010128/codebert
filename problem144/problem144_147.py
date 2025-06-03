a, b, h, m = map(int,input().split())
angle = 30*h - 5.5*m

import math
ans = (a*a + b*b - 2*a*b*math.cos(math.radians(angle)))**0.5
print(ans)