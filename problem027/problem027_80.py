d = int(input().rstrip())

import math
sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))


def make_koch(d, p1, p2):
    s = ((p1[0]*2 + p2[0]) / 3, (p1[1]*2 + p2[1]) / 3)
    t = ((p1[0] + p2[0]*2) / 3, (p1[1] + p2[1]*2) / 3)
    u = ((t[0] - s[0]) * cos60 - (t[1] - s[1])*sin60 + s[0], (t[0] - s[0]) * sin60 + (t[1] - s[1]) * cos60 + s[1])
    if d == 0:
        return [p1]
    elif d == 1:
        return [p1, s, u, t]
    else:
        return make_koch(d-1, p1, s) + make_koch(d-1, s, u) + make_koch(d-1, u, t) + make_koch(d-1, t, p2)
result_list = make_koch(d, (0, 0), (100, 0))

for result in result_list:
    print(result[0], result[1])
print("100 0")
        
        
        
        
