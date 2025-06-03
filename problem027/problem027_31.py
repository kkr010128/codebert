import math
def kochcurve(n,p1x,p1y,p2x,p2y):
    if n==0:
        print("%5f %5f"%(p2x,p2y))
        return
    sx=(p2x-p1x)/3.0+p1x
    sy=(p2y-p1y)/3.0+p1y
    tx=(p2x-p1x)*2.0/3+p1x
    ty=(p2y-p1y)*2.0/3+p1y
    ux=math.cos(math.pi/3)*(tx-sx)-math.sin(math.pi/3)*(ty-sy)+sx
    uy=math.sin(math.pi/3)*(tx-sx)+math.cos(math.pi/3)*(ty-sy)+sy
    kochcurve(n-1,p1x,p1y,sx,sy)
    kochcurve(n-1,sx,sy,ux,uy)
    kochcurve(n-1,ux,uy,tx,ty)
    kochcurve(n-1,tx,ty,p2x,p2y)
    

n=input()
p1x=0.0
p1y=0.0
p2x=100.0
p2y=0.0
print("%5f %5f"%(p1x,p1y))
kochcurve(n,p1x,p1y,p2x,p2y)