import math
a,b,x = map(int,input().split())
S = a*a*b
if 2*x>=S:
    tmp = 2 * (S - x) / (a**3)
else:
    tmp = a * b * b / (2 * x)
print(math.degrees(math.atan(tmp)))
