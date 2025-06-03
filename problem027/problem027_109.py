import math 
c = math.cos(math.radians(60))
s = math.sin(math.radians(60))

def koch(d,p1,p2):
    if d == 0:
        return 
    sx = (2 * p1[0] + p2[0]) / 3
    sy = (2 * p1[1] + p2[1]) / 3

    tx = (p1[0] + p2[0] * 2) / 3
    ty = (p1[1] + p2[1] * 2) / 3

    dx = tx - sx
    dy = ty - sy

    ux = dx * c - dy * s + sx
    uy = dx * s + dy * c + sy

    koch(d-1,p1,(sx,sy))
    print("{0:.8f} {1:.8f}".format(sx,sy))

    koch(d-1,(sx,sy),(ux,uy))
    print("{0:.8f} {1:.8f}".format(ux,uy))

    koch(d-1,(ux,uy),(tx,ty))
    print("{0:.8f} {1:.8f}".format(tx,ty))

    koch(d-1,(tx,ty),p2)

n = int(input())
print("{0:.8f} {1:.8f}".format(0,0))
koch(n,(0,0),(100,0))
print("{0:.8f} {1:.8f}".format(100,0))
