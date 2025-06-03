a,b,x = map(int,input().split())

import math

d = x/(a**2)

c = b-d
e = c*2
if e<=b:
    f = (e**2+a**2)**(1/2)
    g = (f**2+a**2-e**2)/(2*f*a)
    print(math.degrees(math.acos(g)))
else:
    e = 2*x/(a*b)
    #print(e)
    a = b
    f = (e**2+a**2)**(1/2)
    g = (f**2+a**2-e**2)/(2*f*a)
    print(90-(math.degrees(math.acos(g))))