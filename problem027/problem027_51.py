n = int(input())

P = [(0.0,0.0), (100.0, 0)]

import copy
import math
sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))
for _ in range(n):
    next_p = []
    for p1, p2 in zip(P[:-1], P[1:]):
        l = (p1[0]*2/3+p2[0]*1/3, p1[1]*2/3+p2[1]*1/3) 
        r = (p1[0]*1/3+p2[0]*2/3, p1[1]*1/3+p2[1]*2/3)
        x = cos60*(r[0]-l[0])-sin60*(r[1]-l[1])+l[0]
        y = sin60*(r[0]-l[0])+cos60*(r[1]-l[1])+l[1]
        next_p.append(p1)
        next_p.append(l)
        next_p.append((x, y))
        next_p.append(r)
    next_p.append(P[-1])
    P = copy.copy(next_p)

for p in P:
    print(p[0], p[1])
        
    
