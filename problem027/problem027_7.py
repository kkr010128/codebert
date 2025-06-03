import math
n = int(input())
edge_s = (0.0, 0.0)
edge_e = (100.0, 0.0)

def print_tuple(tup):
    print("%.8f %.8f"%(tup[0],tup[1]))

def koch(start, end, n):
    if(n == 0):
        return
    s = ((2*start[0] + end[0]) / 3, (2*start[1] + end[1])/3)
    t = ((start[0] + 2*end[0]) / 3, (start[1] + 2*end[1])/3)
    u = (s[0] +  (t[0]-s[0])*math.cos(math.pi/3)-(t[1]-s[1])*math.sin(math.pi/3), s[1] + (t[0]-s[0]) * math.sin(math.pi/3) + (t[1]-s[1]) * math.cos(math.pi/3))
    n -= 1
    koch(start, s, n)
    print_tuple(s)
    koch(s, u, n)
    print_tuple(u)
    koch(u, t, n)
    print_tuple(t)
    koch(t, end, n)
print_tuple(edge_s)
koch(edge_s, edge_e, n)
print_tuple(edge_e)

