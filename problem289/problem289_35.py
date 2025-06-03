A,B,X = map(int,input().split())
from math import atan2, degrees, radians, tan

b = degrees(atan2(B,A))

def is_ok(d):
    if d > b:
        h = B * tan(radians(90-d))
        return X <= A*B*h/2
    else:
        h = B - A * tan(radians(d))
        return X <= A*A*(h+B)/2
ok = 0
ng = 90
for _ in range(100):
    m = (ok+ng)/2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)