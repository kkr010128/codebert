from math import cos, sin, pi

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def kock(n, p1, p2):
    if n == 0:
        return

    s = Coordinate((2*p1.x+p2.x)/3, (2*p1.y+p2.y)/3)
    t = Coordinate((p1.x+2*p2.x)/3, (p1.y+2*p2.y)/3)
    ux = (t.x-s.x)*cos(pi/3) - (t.y-s.y)*sin(pi/3) + s.x
    uy = (t.x-s.x)*sin(pi/3) + (t.y-s.y)*cos(pi/3) + s.y
    u = Coordinate(ux, uy)
    
    kock(n-1, p1, s)
    print("%f %f"%(s.x, s.y))
    kock(n-1, s, u)
    print("%f %f"%(u.x, u.y))
    kock(n-1, u, t)
    print("%f %f"%(t.x, t.y))
    kock(n-1, t, p2)
    
n = int(input())
p1 = Coordinate(0, 0)
p2 = Coordinate(100, 0)

print("%f %f"%(p1.x, p2.y))
kock(n, p1, p2)
print("%f %f"%(p2.x, p2.y))
