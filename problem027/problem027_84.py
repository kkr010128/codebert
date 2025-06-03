import math
n = int(input())

class point:
    x = 0
    y = 0

def kock(k, p1, p2):
    s = point()
    t = point()
    u = point()
    if k == 0:
        return
    s.x = (2*p1.x+p2.x)/3
    s.y = (2*p1.y+p2.y)/3
    t.x = (p1.x+2*p2.x)/3
    t.y = (p1.y+2*p2.y)/3
    u.x = (t.x-s.x)*math.cos(math.radians(60))-(t.y-s.y)*math.sin(math.radians(60))+s.x
    u.y = (t.x-s.x)*math.sin(math.radians(60))+(t.y-s.y)*math.cos(math.radians(60))+s.y
    kock(k-1, p1, s)
    print(s.x, s.y)
    kock(k-1, s, u)
    print(u.x, u.y)
    kock(k-1, u, t)
    print(t.x, t.y)
    kock(k-1, t, p2)


a = point()
b = point()
b.x = 100
print(a.x, a.y)
kock(n, a, b)
print(b.x, b.y)
