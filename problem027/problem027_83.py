import math
import collections

N = int(input())
Point = collections.namedtuple('Point', ['x', 'y'])


def koch(d, p1, p2):
    if d == 0:
        return
    th = math.pi * 60 / 180
    s = Point(x=(2 * p1.x + p2.x) / 3, y=(2 * p1.y + p2.y) / 3)
    t = Point(x=(p1.x + 2 * p2.x) / 3, y=(p1.y + 2 * p2.y) / 3)
    u = Point(x=(t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x,
              y=(t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y)
    koch(d - 1, p1, s)
    print('{:.8f} {:.8f}'.format(s.x, s.y))
    koch(d - 1, s, u)
    print('{:.8f} {:.8f}'.format(u.x, u.y))
    koch(d - 1, u, t)
    print('{:.8f} {:.8f}'.format(t.x, t.y))
    koch(d - 1, t, p2)


p1 = Point(x=0, y=0)
p2 = Point(x=100, y=0)
print('{:.8f} {:.8f}'.format(p1.x, p1.y))
koch(N, p1, p2)
print('{:.8f} {:.8f}'.format(p2.x, p2.y))

