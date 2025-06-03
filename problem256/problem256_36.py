import math

a,b = map(int,input().split())
if b>a:
    a,b = b,a
l = (a*b)//(math.gcd(a,b))
print(l)