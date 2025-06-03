a, b, x = map(int, input().split())
if x > (a**2)*b/2:
    t = 2*((a**2)*b-x)/(a**3)
else:
    t = a*(b**2)/(2*x)

import math
ans = math.degrees(math.atan(t))
print(ans)
