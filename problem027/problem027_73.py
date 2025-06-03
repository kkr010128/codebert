import math

def koch(n, ax, ay, bx, by):
    if n == 0: return ;
    
    sin = math.sin(math.radians(60))
    cos = math.cos(math.radians(60))
    
    sx = (2.0 * ax + 1.0 * bx) / 3.0
    sy = (2.0 * ay + 1.0 * by) / 3.0
    tx = (1.0 * ax + 2.0 * bx) / 3.0
    ty = (1.0 * ay + 2.0 * by) / 3.0
    ux = (tx - sx) * cos - (ty - sy) * sin + sx
    uy = (tx - sx) * sin + (ty - sy) * cos + sy
    
    koch(n-1, ax, ay, sx, sy)
    print(str(sx)+ " " + str(sy))
    koch(n-1, sx, sy, ux, uy)
    print(str(ux)+ " " + str(uy))
    koch(n-1, ux, uy, tx, ty)
    print(str(tx)+ " " + str(ty))
    koch(n-1, tx, ty, bx, by)

if __name__ == '__main__':
    n = int(input())
    ax = 0.00000000
    ay = 0.00000000
    bx = 100.00000000
    by = 0.00000000
    
    print(str(ax) + " " + str(ay))
    koch(n, ax, ay, bx, by)
    print(str(bx)+ " " + str(by))
