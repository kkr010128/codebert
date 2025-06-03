
[a,b,x] = list(map(int,input().split()))

import math
S = x/a

if S > (a*b)/2:
    c = (2*S)/a - b
    out = math.degrees(math.atan((b-c)/a))
else:
    c = (2*S)/b
    out = math.degrees(math.atan(b/c))

print(out)
