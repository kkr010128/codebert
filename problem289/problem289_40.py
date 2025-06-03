import math
a, b, x = map(int, input().split())
ans = 0

if a*a*b/2 < x:
    t = 2*x/(a*a) - b
    ans =  math.degrees(math.atan((b-t)/a))
else:
    t = 2*x/(a*b)
    ans = math.degrees(math.atan(b/t))

print(ans)