import math

class Point:
    def __init__(self, num_x, num_y):
        self.x = num_x
        self.y = num_y

def kock(n, p1, p2):
    if n == 0:
        return

    s = Point(0, 0)
    t = Point(0, 0)
    u = Point(0, 0)

    s.x = (2 * p1.x + p2.x) / 3.0
    s.y = (2 * p1.y + p2.y) / 3.0
    t.x = (p1.x + p2.x * 2) / 3.0
    t.y = (p1.y + p2.y * 2) / 3.0
    u.x = (t.x - s.x) * math.cos(math.pi / 3) - (t.y - s.y) * math.sin(math.pi / 3) + s.x
    u.y = (t.x - s.x) * math.sin(math.pi / 3) + (t.y - s.y) * math.cos(math.pi / 3) + s.y

    kock(n - 1, p1, s)
    print "%.8f %.8f" % (s.x, s.y)
    kock(n - 1, s, u)
    print "%.8f %.8f" % (u.x, u.y)
    kock(n - 1, u, t)
    print "%.8f %.8f" % (t.x, t.y)
    kock(n - 1, t, p2)

n = input()

p1 = Point(0, 0)
p2 = Point(100, 0)

print "%.8f %.8f" % (p1.x, p1.y)
kock(n, p1, p2)
print "%.8f %.8f" % (p2.x, p2.y)