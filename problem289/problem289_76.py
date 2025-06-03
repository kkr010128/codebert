
from math import atan, sqrt, degrees

a,b,x = map(int, input().split())

ans = 0

if x <= a*a*b/2:
    ans = degrees(atan(a*b*b/(2*x)))
else:
    ans = degrees(atan((2*b-2*x/(a*a))/a))

print(ans)