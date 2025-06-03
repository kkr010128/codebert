import math
def kochCurve(d, p1, p2):
    if d <= 0:
        return
    s = [(2.0*p1[0]+1.0*p2[0])/3.0, (2.0*p1[1]+1.0*p2[1])/3.0]
    t = [(1.0*p1[0]+2.0*p2[0])/3.0, (1.0*p1[1]+2.0*p2[1])/3.0]
    u = [(t[0]-s[0])*math.cos(math.radians(60))-(t[1]-s[1])*math.sin(math.radians(60))+s[0], (t[0]-s[0])*math.sin(math.radians(60))+(t[1]-s[1])*math.cos(math.radians(60))+s[1]]
    kochCurve(d-1, p1, s)
    print(s[0], s[1])
    kochCurve(d-1, s, u)
    print(u[0], u[1])
    kochCurve(d-1, u, t)
    print(t[0], t[1])
    kochCurve(d-1, t, p2)
n = int(input())
s = [0.00000000, 0.00000000]
e = [100.00000000, 0.00000000]
print(s[0],s[1])
if n != 0:
    kochCurve(n,s,e)
print(e[0],e[1])
