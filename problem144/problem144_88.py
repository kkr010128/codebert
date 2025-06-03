import math
a, b, h, m = map(int,input().split())

a_s = (30 * h) % 360 + 0.5 * m
b_s = (6*m)

s = max(a_s,b_s) - min(a_s,b_s)
ans = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(s)))
print(ans)