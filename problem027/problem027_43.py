import math
n = int(input())

def koch(n, p1, p2):
    if n == 0:
        return

    sx = (2*p1['x'] + 1*p2['x'])/3
    sy = (2*p1['y'] + 1*p2['y'])/3
    tx = (1*p1['x'] + 2*p2['x'])/3
    ty = (1*p1['y'] + 2*p2['y'])/3
    ux = (tx - sx)*math.cos(math.radians(60)) - (ty - sy)*math.sin(math.radians(60)) + sx
    uy = (tx - sx)*math.sin(math.radians(60)) + (ty -sy)*math.cos(math.radians(60)) + sy
    
    s = {'x':sx, 'y':sy}
    t = {'x':tx, 'y':ty}
    u = {'x':ux, 'y':uy}

    koch(n-1,p1,s)
    print('{} {}'.format(s['x'],s['y']))
    koch(n-1, s, u)
    print('{} {}'.format(u['x'],u['y']))
    koch(n-1, u, t)
    print('{} {}'.format(t['x'],t['y']))
    koch(n-1,t,p2)

p1 = {'x':float(0),'y':float(0)}
p2 = {'x':float(100),'y':float(0)}
print('{} {}'.format(p1['x'],p1['y']))
koch(n, p1, p2)
print('{} {}'.format(p2['x'],p2['y']))

