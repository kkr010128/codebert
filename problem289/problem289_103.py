a, b, x = map(int, input().split())
vol = a*a*b
half=a*a*b/2
if x> half:
    t = (vol-x)*2/a/a
    tan = t/a
else:
    t= x*2/b/a
    tan=b/t
import math
ans =math.degrees(math.atan(tan))
print(ans)