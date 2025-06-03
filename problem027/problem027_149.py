import math

c60 = math.cos(math.radians(60))
s60 = math.sin(math.radians(60))

def koch(d, p1, p2):
    if d == 0:
        return
    
    sx = (p2[0] + 2 * p1[0]) / 3
    sy = (p2[1] + 2 * p1[1]) / 3
    tx = (p2[0] * 2 + p1[0]) / 3
    ty = (p2[1] * 2 + p1[1]) / 3
    ux = (tx - sx) * c60 - (ty - sy) * s60 + sx
    uy = (tx - sx) * s60 + (ty - sy) * c60 + sy
    
    koch(d-1, p1, (sx, sy))
    print("{0:.5f} {1:.5f}".format(sx, sy))
 
    koch(d-1, (sx, sy), (ux, uy))
    print("{0:.5f} {1:.5f}".format(ux, uy))
 
    koch(d-1, (ux, uy), (tx, ty))
    print("{0:.5f} {1:.5f}".format(tx, ty))
    
    koch(d-1, (tx, ty), p2)

n = int(input())

print("0 0")
koch(n, (0, 0), (100, 0))
print("100 0") 
