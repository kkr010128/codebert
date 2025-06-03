import math

n=input()
m=math.radians(60)

def kock(n, p1x, p1y, p2x, p2y):

    
    if(n == 0):
        return

    sx=(2*p1x+1*p2x)/3
    sy=(2*p1y+1*p2y)/3
    tx=(1*p1x+2*p2x)/3
    ty=(1*p1y+2*p2y)/3

    ux=(tx-sx)*math.cos(m)-(ty-sy)*math.sin(m)+sx
    uy=(tx-sx)*math.sin(m)+(ty-sy)*math.cos(m)+sy


    kock(n-1, p1x, p1y, sx, sy)
    print round(sx,8),round(sy, 8)
    kock(n-1, sx, sy, ux, uy)
    print round(ux, 8),round(uy, 8)
    kock(n-1, ux, uy, tx, ty)
    print round(tx, 8),round(ty, 8)
    kock(n-1, tx, ty, p2x, p2y)
    

p1x = 0.00000000
p1y = 0.00000000
p2x = 100.00000000
p2y = 0.00000000
 
print p1x, p1y
kock(n, p1x, p1y, p2x, p2y)
print p2x, p2y