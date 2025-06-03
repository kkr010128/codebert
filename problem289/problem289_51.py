import math
a,b,x = map(int,input().split())
if x <= b*a*a*1/2:
    dum = 2*x/(a*b)
    ans = 90-(math.degrees(math.atan(dum/b)))
else:
    x -= b*a*a*1/2
    dum = b-(x*2/(a*a))
    ans = math.degrees(math.atan(dum / a))
print(ans)