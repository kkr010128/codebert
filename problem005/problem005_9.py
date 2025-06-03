def gcd(a,b):
    while True:
        if a > b:
            a %= b
        else:
            b %= a
        if a == 0 or b == 0:
            return max(a,b)

def lcm(a,b,g):
    return int(a*b/g)
from sys import stdin
for l in stdin:
    a,b = list(map(int,l.split()))
    g = gcd(a,b)
    print ("%s %s"%(g,lcm(a,b,g)))