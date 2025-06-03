
a,b=list(map(int,input().split()))

from fractions import gcd

res=a*b/gcd(a,b)
print(int(res))

