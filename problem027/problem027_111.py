import math
 
def koch(n, x1, y1, x2, y2):
    if n == 0:
        return
   
    angle = math.radians(60)
   
    sx = (2*x1 + x2)/3
    sy = (2*y1 + y2)/3
    tx = (2*x2 + x1)/3
    ty = (2*y2 + y1)/3
    ux = (tx - sx)*math.cos(angle) - (ty - sy)*math.sin(angle) + sx
    uy = (tx - sx)*math.sin(angle) + (ty - sy)*math.cos(angle) + sy
   
    koch(n-1, x1, y1, sx, sy)
    print sx, sy
    koch(n-1, sx, sy, ux, uy)
    print ux, uy
    koch(n-1, ux, uy, tx, ty)
    print tx, ty
    koch(n-1, tx, ty, x2, y2)
   
n = input()
   
p1x = 0.0
p1y = 0.0
p2x = 100.0
p2y = 0.0
   
print p1x, p1y
koch(n, p1x, p1y, p2x, p2y)
print p2x, p2y