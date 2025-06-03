import math

def koch(d,p1x,p1y,p2x,p2y):
    if d == 0:
        return 0
    
    sin = math.sin(math.radians(60))
    cos = math.cos(math.radians(60))
    ax = (2 * p1x + 1 * p2x)/3 
    ay = (2 * p1y + 1 * p2y)/3 
    bx = (1 * p1x + 2 * p2x)/3 
    by = (1 * p1y + 2 * p2y)/3
    ux = (bx - ax)* cos - (by - ay)*sin + ax 
    uy = (bx - ax)* sin + (by - ay)*cos + ay

    koch(d-1,p1x,p1y,ax,ay)
    print(ax,ay)
    koch(d-1,ax,ay,ux,uy)
    print(ux,uy)
    koch(d-1,ux,uy,bx,by)
    print(bx,by)
    koch(d-1,bx,by,p2x,p2y)

d = int(input())
print(0,0)
koch(d,0,0,100,0)
print(100,0)
