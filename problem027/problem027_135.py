# coding=utf-8
import math

def koch(p1, p2, n):
    if n == 0:
        return None
    p1_x = p1[0]
    p1_y = p1[1]
    p2_x = p2[0]
    p2_y = p2[1]

    s_x = (1/3) * (2*p1_x + p2_x)
    s_y = (1/3) * (2*p1_y + p2_y)
    t_x = (1/3) * (p1_x + 2*p2_x)
    t_y = (1/3) * (p1_y + 2*p2_y)

    u_x = s_x + (1/2)*(t_x-s_x) + (-math.sqrt(3)/2)*(t_y-s_y)
    u_y = s_y + (math.sqrt(3)/2)*(t_x-s_x) + (1/2)*(t_y-s_y)

    koch([p1_x, p1_y], [s_x, s_y], n-1)
    print("%.8f %.8f" %(s_x, s_y))
    koch([s_x, s_y], [u_x, u_y], n-1)
    print("%.8f %.8f" %(u_x, u_y))
    koch([u_x, u_y], [t_x, t_y], n-1)
    print("%.8f %.8f" %(t_x, t_y))
    koch([t_x, t_y], [p2_x, p2_y], n-1)


n = int(input())
p1 = [0, 0]
p2 = [100, 0]
print("%.8f %.8f" %(p1[0], p1[1]))
koch(p1, p2, n)
print("%.8f %.8f" %(p2[0], p2[1]))