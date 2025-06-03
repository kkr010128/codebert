a, b, x = map(int, input().split())

from math import pi, tan, radians
# import math
l = 0
r = 180

for i in range(200000):
    
    m = (l+r)/2
    
    if b * tan(radians(180.0/2-m)) <= a:
        d = b * tan(radians(180.0/2-m)) * b * a / 2
    else:
        d = b*a*a - tan(radians(m))*a*a*a/2
    
    if d == x:
        print(m)
        exit(0)
    elif d > x:
        l = m
    else:
        r = m

print(m)
