import math

d = int(input())

class point:
    def __init__(self, arg_x, arg_y):
        self.x = arg_x
        self.y = arg_y

p1 = point(0, 0)
p2 = point(100, 0)

def koch(d, p1, p2):
    pi = math.pi
    cos60 = math.cos(pi/3)
    sin60 = math.sin(pi/3)
    if d == 0:
        return
    else:
        s = point((2*p1.x + 1*p2.x)/3, (2*p1.y + 1*p2.y)/3)
        t = point((1*p1.x + 2*p2.x)/3, (1*p1.y + 2*p2.y)/3)
        u = point(s.x + cos60*(t.x-s.x) - sin60*(t.y-s.y), s.y + sin60*(t.x-s.x) + cos60*(t.y-s.y))
        koch(d-1, p1, s)
        print(s.x, s.y)
        koch(d-1, s, u)
        print(u.x, u.y)
        koch(d-1, u, t)
        print(t.x, t.y)
        koch(d-1, t, p2)

print(p1.x, p1.y)
koch(d, p1, p2)
print(p2.x, p2.y)
