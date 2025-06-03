import math
a, b, h, m = map(int,input().split())
ms = m//60
ma = m%60
h = h + ms
ha =h%12 + ma/60
rh = ha*math.pi/6
rm = ma*math.pi/30
x = math.cos(rh - rm)
ans = math.sqrt(a**2 + b**2 - 2*a*b*x)
print(ans)