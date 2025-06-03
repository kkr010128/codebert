import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

for line in sys.stdin:
    a, b= map(int, line.split())
    if a < b:
        a, b = b, a
    g = gcd(a,b)
    print g, a*b/g