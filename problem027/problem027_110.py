import math

def plot(x,y):
    print(f"{x:.8f} {y:.8f}")

def koch(n,x1,y1,x2,y2):
    if n==0:
        plot(x1,y1)
        return
    ax=(2*x1+x2)/3
    ay=(2*y1+y2)/3
    bx=(x1+2*x2)/3
    by=(y1+2*y2)/3
    cx=(bx-ax)*(1/2)-(by-ay)*(math.sqrt(3)/2)+ax
    cy=(bx-ax)*(math.sqrt(3)/2)+(by-ay)*(1/2)+ay
    koch(n-1,x1,y1,ax,ay)
    koch(n-1,ax,ay,cx,cy)
    koch(n-1,cx,cy,bx,by)
    koch(n-1,bx,by,x2,y2)
    
n=int(input())
koch(n,0,0,100,0)
plot(100,0)

