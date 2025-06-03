from math import sin, cos, pi

def koch_curve(d, p1, p2):
    if d == 0:
        return

    s = [None, None]
    u = [None, None]
    t = [None, None]
    
    s[0] = (2*p1[0] + p2[0])/3
    s[1] = (2*p1[1] + p2[1])/3
    t[0] = (p1[0] + 2*p2[0])/3
    t[1] = (p1[1] + 2*p2[1])/3
    u[0] = (t[0] - s[0])*cos(1/3*pi) - (t[1] - s[1])*sin(1/3*pi) + s[0]
    u[1] = (t[0] - s[0])*sin(1/3*pi) + (t[1] - s[1])*cos(1/3*pi) + s[1]

    koch_curve(d-1, p1, s)
    print(s[0], s[1])
    koch_curve(d-1, s, u)
    print(u[0], u[1])
    koch_curve(d-1, u, t)
    print(t[0],t[1])
    koch_curve(d-1, t, p2)

num = int(input())
print(0.0, 0.0)
koch_curve(num, [0.0, 0.0], [100.0, 0.0])
print(100.0, 0.0)
