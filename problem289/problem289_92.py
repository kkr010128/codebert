import bisect as bs
import math as m
a,b,x = map(int,input().split())
l = 0
r = m.pi/2
for _ in range(10000):
    s = (l+r)/2
    ts = m.tan(s)
    if a*ts < b:
        boundary = a*a*b-a*a*a*ts/2
        if x > boundary:
            r = s
        else:
            l = s
    else:
        boundary = a*b*b/(ts*2)
        if x > boundary:
            r = s
        else:
            l = s
print(l*180/m.pi)