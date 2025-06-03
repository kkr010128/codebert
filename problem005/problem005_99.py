import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

for s in sys.stdin:
    a, b = map(int, s.split())
    print "%d %d"%(gcd(a, b), lcm(a, b))