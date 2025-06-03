import math
x1,y1,x2,y2 = map(float, input().split())
a1 = (x2-x1)**2
a2 = (x1-x2)**2
b1 = (y2-y1)**2
b2 = (y1-y2)**2
if x1<x2:
    if y1<y2:
        print(math.sqrt(a1+b1))
    else:
        print(math.sqrt(a1+b2))
else:
    if y1<y2:
        print(math.sqrt(a2+b1))
    else:
        print(math.sqrt(a2+b2))
