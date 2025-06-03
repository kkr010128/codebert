import sys

def gcd(a, b):
    "?????§??¬?´???°????±???????"
    if a < b:
        c = a
        a = b
        b = c
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    return g * (a // g) * (b // g)

for line in sys.stdin:
    a, b = map(int, line.split())
    print("%d %d" % (gcd(a, b), lcm(a, b)))