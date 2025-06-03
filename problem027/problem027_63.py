import math

def koch(d,x1,y1,x2,y2):
    if d == 0:
        return

    xs = (2*x1+x2)/3
    ys = (2*y1+y2)/3
    xt = (x1+2*x2)/3
    yt = (y1+2*y2)/3

    xu = (xt-xs)*math.cos(math.pi/3) - (yt-ys)*math.sin(math.pi/3) + xs
    yu = (xt-xs)*math.sin(math.pi/3) + (yt-ys)*math.cos(math.pi/3) + ys


    koch(d-1,x1,y1,xs,ys)
    print(xs,ys)
    koch(d-1,xs,ys,xu,yu)
    print(xu,yu)
    koch(d-1,xu,yu,xt,yt)
    print(xt,yt)
    koch(d-1,xt,yt,x2,y2)
    
n = int(input())
print(0.00000000,0.00000000)
koch(n,0.0,0.0,100.0,0.0)
print(100.00000000,0.00000000)