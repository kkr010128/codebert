import math
n = int(input())

A = []
def koch(d, p1, p2):
    rot = math.radians(60)
    if d == 0:
        return 0
    else:
        s = ((2.0 * p1[0] + p2[0]) / 3.0, (2.0 * p1[1] + p2[1]) / 3.0)
        t = ((2.0 * p2[0] + p1[0]) / 3.0, (2.0 * p2[1] + p1[1]) / 3.0)
        ux = (t[0] - s[0]) * math.cos(rot) - (t[1] - s[1]) * math.sin(rot) + s[0]
        uy = (t[0] - s[0]) * math.sin(rot) + (t[1] - s[1]) * math.cos(rot) + s[1]
        u = (ux, uy)
        koch(d-1, p1, s) 
        print(s[0], s[1])
        koch(d-1, s, u)
        print(u[0], u[1])
        koch(d-1, u, t)
        print(t[0], t[1])
        koch(d-1, t, p2)

p1 = (0.0, 0.0)
p2 = (100.0, 0.0)
print(p1[0], p1[1])
koch(n, p1, p2)
print(p2[0], p2[1])
