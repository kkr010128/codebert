from math import cos,sin, pi
n = int(input())
def  koch(n, l, r):
    if n == 0:
        return
    s = ((2*l[0] + r[0])/3, (2*l[1] + r[1])/3)
    t = ((l[0] + 2*r[0])/3, (l[1] + 2*r[1])/3)
    u = ((t[0] - s[0]) * cos(pi/3) - (t[1] - s[1]) * sin(pi/3) + s[0], 
         (t[0] - s[0]) * sin(pi/3) + (t[1] - s[1]) * cos(pi/3) + s[1])
    koch(n - 1, l, s)
    print(s[0], s[1])
    koch(n - 1, s, u)
    print(u[0], u[1])
    koch(n - 1, u, t)
    print(t[0], t[1])
    koch(n - 1, t, r)

print(0, 0)
koch(n, (0, 0), (100, 0))
print(100, 0)