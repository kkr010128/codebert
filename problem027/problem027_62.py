import math as m
def plot(x,y):
    print(f'{x:.8f} {y:.8f}')
def koch(n,x1,y1,x2,y2):
    if n==0:
        plot(x1,y1)
        return
    sx=(2*x1+x2)/3
    sy=(2*y1+y2)/3
    tx=(x1+2*x2)/3
    ty=(y1+2*y2)/3
    ux=(tx-sx)*m.cos(m.radians(60))-(ty-sy)*m.sin(m.radians(60))+sx
    uy=(tx-sx)*m.sin(m.radians(60))+(ty-sy)*m.cos(m.radians(60))+sy
    koch(n-1,x1,y1,sx,sy)
    koch(n-1,sx,sy,ux,uy)
    koch(n-1,ux,uy,tx,ty)
    koch(n-1,tx,ty,x2,y2)
n=int(input())
koch(n,0,0,100,0)
plot(100,0)
