

import math

def kock(n,p1x,p1y,p2x,p2y):
    if n==0:
        pass
    else:
        sx=(2*p1x+p2x)/3
        sy=(2*p1y+p2y)/3
        tx=(p1x+2*p2x)/3
        ty=(p1y+2*p2y)/3

        ux=(tx-sx)*math.cos(math.pi*1/3)-(ty-sy)*math.sin(math.pi*1/3)+sx
        uy=(tx-sx)*math.sin(math.pi*1/3)+(ty-sy)*math.cos(math.pi*1/3)+sy

        kock(n-1,p1x,p1y,sx,sy)
        print(sx,sy)
        kock(n - 1, sx, sy, ux, uy)
        print(ux,uy)
        kock(n - 1, ux, uy, tx, ty)
        print(tx,ty)
        kock(n - 1, tx, ty, p2x, p2y)

n=int(input().strip())

zero=0.0
hundred=100.0
print(zero,zero)
kock(n,0,0,100,0)
print(hundred,zero)