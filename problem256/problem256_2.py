from math import gcd
a,b = map(int,input().split())
lcm = a*b/gcd(a,b)
print(int(lcm))