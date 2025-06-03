import math
def koch(d, p1, p2):
    if d == 0:
        return

    sx = (2*p1[0]+1*p2[0])/3
    sy = (2*p1[1]+1*p2[1])/3
    s = (sx, sy)
    tx = (1*p1[0]+2*p2[0])/3
    ty = (1*p1[1]+2*p2[1])/3
    t = (tx, ty)
    rad = math.radians(60)
    ux = (t[0]-s[0])*math.cos(rad)-(t[1]-s[1])*math.sin(rad)+s[0]
    uy = (t[0]-s[0])*math.sin(rad)+(t[1]-s[1])*math.cos(rad)+s[1]
    u = (ux, uy)

    koch(d-1, p1, s)
    print(s[0], s[1])
    koch(d-1, s, u)
    print(u[0], u[1])
    koch(d-1, u, t)
    print(t[0], t[1])
    koch(d-1, t, p2)

d = int(input())
p1 = (0, 0)
p2 = (100, 0)
print(p1[0], p1[1])
koch(d, p1, p2)
print(p2[0], p2[1])
