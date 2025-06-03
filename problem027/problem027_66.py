def koch(n, ax, ay, bx, by):
    if n == 0:
        return
    
    th = math.pi * 60.0 / 180.0
    
    xx = (2.0 * ax + bx)/3.0
    xy = (2.0 * ay + by)/3.0
    zx = (ax + 2.0 * bx)/3.0
    zy = (ay + 2.0 * by)/3.0
    yx = (zx - xx)*math.cos(th) - (zy - xy)*math.sin(th) + xx
    yy = (zx - xx)*math.sin(th) + (zy - xy)*math.cos(th) + xy
    
    koch(n-1, ax, ay, xx, xy)
    print xx,xy
    koch(n-1, xx, xy, yx, yy)
    print yx,yy
    koch(n-1, yx, yy, zx, zy)
    print zx,zy
    koch(n-1, zx, zy, bx, by)
    
import math
n = int(raw_input())
ax = 0.0
ay = 0.0
bx = 100.0
by = 0.0

print ax,ay
koch(n, ax, ay, bx, by)
print bx,by