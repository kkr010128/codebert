import math

def kock(n,p1x,p1y,p2x,p2y):
    if(n==0):
        return

    sx = (2*p1x+p2x)/3.0
    sy = (2*p1y+p2y)/3.0
    tx = (p1x+2*p2x)/3.0
    ty = (p1y+2*p2y)/3.0

    ux = (tx-sx)*math.cos(math.radians(60)) - (ty-sy)*math.sin(math.radians(60)) + sx
    uy = (tx-sx)*math.sin(math.radians(60)) + (ty-sy)*math.cos(math.radians(60)) + sy

    kock(n-1,p1x,p1y,sx,sy)
    print(sx,sy)
    kock(n-1,sx,sy,ux,uy)
    print(ux,uy)
    kock(n-1,ux,uy,tx,ty)
    print(tx,ty)
    kock(n-1,tx,ty,p2x,p2y)


n = int(input())
print(0,0)
kock(n,0,0,100,0)
print(100,0)
