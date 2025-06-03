n = int(input())

def koch(n,x1,y1,x2,y2):
    if n == 0:
        print(x1,y1)
    else:
        a = 3**(1/2)/2
        p1 = koch(n-1,x1,y1,(2*x1+x2)/3,(2*y1+y2)/3)
        if abs(y1 - y2) <= 10**(-4):
            s = koch(n-1,(2*x1+x2)/3,(2*y1+y2)/3,(x1+x2)/2,y1+(x2-x1)*a/3)
            u = koch(n-1,(x1+x2)/2,y1+(x2-x1)*a/3,(x1+2*x2)/3,(y1+2*y2)/3)
        else:
            if x1 < x2 and y1 < y2:
                s = koch(n-1,(2*x1+x2)/3,(2*y1+y2)/3,x1,(y1+2*y2)/3)
                u = koch(n-1,x1,(y1+2*y2)/3,(x1+2*x2)/3,(y1+2*y2)/3)
            elif x1 < x2 and y1 > y2:
                s = koch(n-1,(2*x1+x2)/3,(2*y1+y2)/3,x2,(2*y1+y2)/3)
                u = koch(n-1,x2,(2*y1+y2)/3,(x1+2*x2)/3,(y1+2*y2)/3)
            elif x1 > x2 and y1 < y2:
                s = koch(n-1,(2*x1+x2)/3,(2*y1+y2)/3,x2,(2*y1+y2)/3)
                u = koch(n-1,x2,(2*y1+y2)/3,(x1+2*x2)/3,(y1+2*y2)/3)
            else:
                s = koch(n-1,(2*x1+x2)/3,(2*y1+y2)/3,x1,(y1+2*y2)/3)
                u = koch(n-1,x1,(y1+2*y2)/3,(x1+2*x2)/3,(y1+2*y2)/3)
        t = koch(n-1,(x1+2*x2)/3,(y1+2*y2)/3,x2,y2)
        return p1,s,u,t

X = koch(n,0,0,100,0)
print(100,0)

