import math

a,b,c=map(float,input().split())

if c<90:
    e=c*math.pi/180
    S=a*b*1/2*math.sin(e)
    t=a**2+b**2-2*a*b*math.cos(e)
    r=math.sqrt(t)
    L=a+b+r
    h=b*math.sin(e)
    print(S)
    print(L)
    print(h)

if c==90:
    e=c*math.pi/180
    S=a*b*1/2*math.sin(e)
    t=a**2+b**2-2*a*b*math.cos(e)
    r=math.sqrt(t)
    L=a+b+r
    h=b
    print(S)
    print(L)
    print(h)

if c>90:
    e=c*math.pi/180
    d=180*math.pi/180
    f=d-e
    S=a*b*1/2*math.sin(e)
    t=a**2+b**2-2*a*b*math.cos(e)
    r=math.sqrt(t)
    L=a+b+r
    h=b*math.sin(f)
    print(S)
    print(L)
    print(h)
