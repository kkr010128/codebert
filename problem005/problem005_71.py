import sys

def gcd(a,b):
    r= b % a
    while r != 0:
        a,b = r,a
        r = b % a
    return a

def lcm(a,b):
    return int(a*b/gcd(a,b))

for line in sys.stdin:
    a,b = sorted(map(int, line.rstrip().split(' ')))
    print("{} {}".format(gcd(a,b),lcm(a,b)))