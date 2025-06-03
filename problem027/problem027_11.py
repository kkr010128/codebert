import math
dig_six = math.radians(60)

def koch(d, p1, p2):
    if d == 0:
        return d
    #calc s, u, t from p1, p2
    s_x = (2*p1[0]+1 * p2[0]) / 3
    s_y = (2*p1[1]+1 * p2[1]) / 3
    s = (s_x, s_y)
    t_x = (1*p1[0]+2 * p2[0]) / 3
    t_y = (1*p1[1]+2 * p2[1]) / 3
    t = (t_x, t_y)
    u_x = (t_x - s_x)*math.cos(dig_six) - (t_y - s_y)*math.sin(dig_six) + s_x
    u_y = (t_x - s_x)*math.sin(dig_six) + (t_y - s_y)*math.cos(dig_six) + s_y
    u = (u_x, u_y)
    
    koch(d-1, p1, s)
    print (' '.join([str(x) for x in s]))
    koch(d-1, s, u)
    print (' '.join([str(x) for x in u]))
    koch(d-1, u, t)
    print (' '.join([str(x) for x in t]))
    koch(d-1, t, p2)

if __name__ == '__main__':
    iterate = int(input())
    p1 = (0.0, 0.0)
    p2 = (100.0, 0.0)
    print (' '.join([str(x) for x in p1]))
    koch(iterate, p1, p2)
    print (' '.join([str(x) for x in p2]))
