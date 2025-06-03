# encoding: utf-8


import sys
import math

_input = sys.stdin.readlines()
depth = int(_input[0])
sin_60, cos_60 = math.sin(math.pi / 3), math.cos(math.pi / 3)


class Point(object):
    def __init__(self, x=0.0, y=0.0):
        """
        initialize the point
        """
        self.x = float(x)
        self.y = float(y)


def koch_curve(d, p1, p2):
    if not d:
        # print('end')
        return None

    # s, t, u = Point(), Point, Point()
    s = Point()
    t = Point()
    u = Point()
    s.x = (2 * p1.x + p2.x) / 3
    s.y = (2 * p1.y + p2.y) / 3

    t.x = (p1.x + 2 * p2.x) / 3
    t.y = (p1.y + 2 * p2.y) / 3

    u.x = (t.x - s.x) * cos_60 - (t.y - s.y) * sin_60 + s.x
    u.y = (t.x - s.x) * sin_60 + (t.y - s.y) * cos_60 + s.y

    koch_curve(d - 1, p1, s)
    print(format(s.x, '.8f'), format(s.y, '.8f'))

    koch_curve(d - 1, s, u)
    print(format(u.x, '.8f'), format(u.y, '.8f'))

    koch_curve(d - 1, u, t)
    print(format(t.x, '.8f'), format(t.y, '.8f'))

    koch_curve(d - 1, t, p2)


if __name__ == '__main__':
    p1_start, p2_end = Point(x=0, y=0), Point(x=100, y=0)
    print(format(p1_start.x, '.8f'), '', format(p1_start.y, '.8f'))
    koch_curve(depth, p1_start, p2_end)
    print(format(p2_end.x, '.8f'), '', format(p2_end.y, '.8f'))