import sys
from math import sin, cos, radians
input = sys.stdin.readline
deg = radians(60)

def Koch(n, p1_x, p1_y, p2_x, p2_y):
    if n != 0:
        s_x = (2 * p1_x + p2_x) / 3
        s_y = (2 * p1_y + p2_y) / 3
        t_x = (p1_x + 2 * p2_x) / 3
        t_y = (p1_y + 2 * p2_y) / 3
        u_x = (t_x - s_x) * cos(deg) - (t_y - s_y) * sin(deg) + s_x
        u_y = (t_x - s_x) * sin(deg) + (t_y - s_y) * cos(deg) + s_y
        Koch(n - 1, p1_x, p1_y, s_x, s_y)
        print('{:.8f} {:.8f}'.format(s_x, s_y))
        Koch(n - 1, s_x, s_y, u_x, u_y)
        print('{:.8f} {:.8f}'.format(u_x, u_y))
        Koch(n - 1, u_x, u_y, t_x, t_y)
        print('{:.8f} {:.8f}'.format(t_x, t_y))
        Koch(n - 1, t_x, t_y, p2_x, p2_y)
    else:
        return

n = int(input())
p1_x, p1_y = 0, 0
p2_x, p2_y = 100, 0
print('{:.8f} {:.8f}'.format(p1_x, p1_y))
Koch(n, p1_x, p1_y, p2_x, p2_y)
print('{:.8f} {:.8f}'.format(p2_x, p2_y))

