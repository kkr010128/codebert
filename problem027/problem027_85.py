import sys
input = sys.stdin.readline

import math
cos60 = math.cos(math.radians(60))
sin60 = math.sin(math.radians(60))

n =  int(input())

def koch(d, p, q):#p,qはリストでp[0]がx座標、p[1]がy座標
    if d == 0:
        return
    s=[0,0]
    t=[0,0]
    u=[0,0]
    s[0] = (2 * p[0] + q[0]) / 3
    s[1] = (2 * p[1] + q[1]) / 3
    t[0] = (p[0] + 2 * q[0]) / 3
    t[1] = (p[1] + 2 * q[1]) / 3
    u[0] = (t[0] - s[0]) * cos60 - (t[1] - s[1]) * sin60 + s[0]
    u[1] = (t[0] - s[0]) * sin60 + (t[1] - s[1]) * cos60 + s[1]
    
    koch(d-1, p, s)
    print(s[0], s[1])
    koch(d-1, s, u)
    print(u[0], u[1])
    koch(d-1, u, t)
    print(t[0], t[1])
    koch(d-1, t, q)

a = [0, 0]
b = [100, 0]

print(a[0], a[1])
koch(n, a, b)
print(b[0], b[1])
