N = int(input())
from math import sin, cos, pi
th = pi/3
def koch(d, p1, p2):
    if d == 0:
        return
    s = [0, 0]
    t = [0, 0]
    u = [0, 0]
    
    s[0] = (2 * p1[0] + p2[0])/3
    s[1] = (2 * p1[1] + p2[1])/3

    t[0] = (2 * p2[0] + p1[0])/3
    t[1] = (2 * p2[1] + p1[1])/3

    u[0] = (t[0] - s[0]) * cos(th) - (t[1] - s[1]) * sin(th) + s[0]
    u[1] = (t[0] - s[0]) * sin(th) + (t[1] - s[1]) * cos(th) + s[1]

    koch(d-1, p1, s)
    print(*s)

    koch(d-1, s, u)
    print(*u)

    koch(d-1, u, t)
    print(*t)

    koch(d-1, t, p2)

p_start = [0.0, 0.0]
p_end = [100.0, 0.0]
print(*p_start)
koch(N, p_start, p_end)
print(*p_end)
